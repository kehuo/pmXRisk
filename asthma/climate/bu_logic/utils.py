from datetime import datetime, timedelta
import traceback
from bb_logger.logger import Logger
from sqlalchemy import and_, or_, func
from models.db_models import City, Weather, PM
from random import choice
from data.param import pm_25_threshold, pm_10_threshold

"""
以下为 build_weather_info 所需的函数
1 search_weather_by_cityname
2 search_pm_by_cityname

以下为 cal_asthma_risk 所需函数
1 build_weather_avg >> 获得1周或者2周的 T 和 W 均值
2 build_pm_avg_list >> 获得1周或者2周内每天的 PM2.5, PM10 的均值的列表
3 count_pm_days >> 计算1周或者2周内 PM 累计超标天数， 即公式中的 M

4 search_week_rawdata_by_cityname >> 通过城市名找到city_code, 再根据city_code过滤1周或者2周内的rawdata初始数据
"""


def search_weather_by_cityname(global_var, args):
    """
    2019-10-14注释
    注意:
    1 数据库中, 对于每个城市，每天只存一条天气信息 (最近抓取的数据会覆盖上一次抓取的数据, 比如下午14点抓到的数据会覆盖掉13点的)
    2 cron tab 每天会抓 24 次, 如果全部抓取失败，则返回一个空字典 （当前规则: 宁可返回空字典, 也不返回错误的天气信息）
    比如10月14日，北京天气抓取24次全部失败，则数据库中没有这一天北京天气信息，那么返回一个空字典，而不是返回10月13日(昨天)的天气。
    """

    db = global_var['db']
    res = {}

    try:
        today_weather = None
        city = db.session.query(City).filter(City.name_zh == args['cityName']).first()
        weather_list = db.session.query(Weather).filter(Weather.city_code == city.city_code).all()

        for i in weather_list:
            # 只拿今天的数据
            if i.weather_date.date() == datetime.now().date():
                today_weather = i
                break

        if today_weather:
            res["current_time"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            res["temperature_average"] = float(today_weather.temperature_average)
            res['temperature_lowest'] = today_weather.temperature_lowest
            res['temperature_highest'] = today_weather.temperature_highest
            res['week'] = today_weather.week
            res['weather_condition'] = today_weather.weather_condition
            res['humidity'] = today_weather.humidity
            res['updated_at_minutes_ago'] = int((datetime.now() - today_weather.updated_at).seconds / 60)

    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
    return res


def search_pm_by_cityname(global_var, args):
    """
    2019-10-14注释
    1 对于同一个城市, 数据库中每天会存储很多条该城市的pm信息
    2 如果一天内所有的抓取都失败了, 那么数据库没有当天任何pm数据。这种情况，返回空字典，而不是返回昨天，甚至前天的错误数据
    """
    db = global_var['db']
    res = {}
    try:
        # step 1
        city = db.session.query(City).filter(City.name_zh == args['cityName']).first()
        current_time = datetime.now()
        oneday_ago = current_time - timedelta(days=1)
        pm_list = db.session.query(PM).filter(
            and_(PM.city_code == city.city_code, PM.pm_date.between(oneday_ago, current_time))).all()
        if len(pm_list) > 0:
            # 第一部分, 画曲线图需要的每小时的pm值
            for i in range(len(pm_list)):
                # 每个小时的值
                res[str(pm_list[i].pm_date)] = {}
                res[str(pm_list[i].pm_date)]['pm2.5'] = pm_list[i].pm_25
                res[str(pm_list[i].pm_date)]['pm10'] = pm_list[i].pm_10
            pm25_avg_today, pm10_avg_today = build_pm_avg_per_day(pm_list, split_num=4)
            res['pm_avg_today'] = {}
            res['pm_avg_today']['pm2.5'] = pm25_avg_today
            res['pm_avg_today']['pm10'] = pm10_avg_today
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
    return res


def build_pm_avg_per_day(pm_list, split_num=4):
    """
    pm_list: 一整天的初始数据
    split_num: 将一天分成几段, 默认是4段, 每段6小时
    """
    # 分时间段 ,默认4段，每段6小时
    day_split = list(map(lambda x: [int(24 / split_num) * x + i for i in range(int(24 / split_num))], range(split_num)))
    # 从pm_list中按 pm_date.hour ,将各时段数据存入 pm_avg_dict 中
    pm_sum_dict = {"pm_25": {}, "pm_10": {}}
    for i in range(len(day_split)):
        tmp_25, tmp_10 = [], []
        for j in pm_list:
            if j.pm_date.hour in day_split[i]:
                tmp_25.append(j.pm_25)
                tmp_10.append(j.pm_10)
        pm_sum_dict["pm_25"][i] = tmp_25
        pm_sum_dict["pm_10"][i] = tmp_10
    # 求每个时间段的均值, 存在 pm25_avg_dict, pm10_avg_dict
    pm25_avg_dict, pm10_avg_dict = {}, {}
    # pm2.5
    for k, v in pm_sum_dict["pm_25"].items():
        # 如果这个时间段有数据, 则正常求均值
        if len(v) > 0:
            pm25_avg_dict[i] = sum(v) / len(v)
        # 如果某个时间段没有任何数据, 那么暂时先将今天所有数据pm_list的均值做为替代
        elif len(v) == 0:
            pm25_avg_dict[i] = sum([j.pm_25 for j in pm_list]) / len(pm_list)
    # pm10
    for k, v in pm_sum_dict["pm_10"].items():
        # 如果这个时间段有数据, 则正常求均值
        if len(v) > 0:
            pm10_avg_dict[i] = sum(v) / len(v)
        # 如果某个时间段没有任何数据, 那么暂时先将今天所有数据pm_list的均值做为替代
        elif len(v) == 0:
            pm10_avg_dict[i] = sum([j.pm_10 for j in pm_list]) / len(pm_list)

    # step5 对于4个时间段的均值之和除以4，求每日均值
    pm25_avg_today = sum([i for i in pm25_avg_dict.values()]) / len(pm25_avg_dict)
    pm10_avg_today = sum([i for i in pm10_avg_dict.values()]) / len(pm10_avg_dict)
    return pm25_avg_today, pm10_avg_today


# 该函数根据city_name, 获取前一周和前两周的初始数据 rawdata
def search_week_rawdata_by_cityname(tableClass, global_var, args):
    wk1 = None
    wk2 = None

    db = global_var['db']
    current_time = datetime.now()
    wk1_ago = current_time - timedelta(days=7)
    wk2_ago = current_time - timedelta(days=14)
    city = db.session.query(City).filter(or_(City.name_zh == args["cityName"],
                                             City.name_en == args["cityName"])).first()
    if city is not None:
        city_code = city.city_code
        query = db.session.query(tableClass).filter(tableClass.city_code == city_code)
        if tableClass == Weather:
            wk1 = query.filter(tableClass.weather_date.between(wk1_ago, current_time)).all()
            wk2 = query.filter(tableClass.weather_date.between(wk2_ago, current_time)).all()
        elif tableClass == PM:
            wk1 = query.filter(tableClass.pm_date.between(wk1_ago, current_time)).all()
            wk2 = query.filter(tableClass.pm_date.between(wk2_ago, current_time)).all()

    return wk1, wk2


# 以下为计算 风险系数所需函数
def asthma_formula(param_d, M, T, W, F, R, s):
    if (M is None) or (T is None) or (W is None):
        return None
    res = param_d['b'] * M + \
          param_d['t'] * T + \
          param_d['w'] * W + \
          param_d['f'] * F + \
          param_d['r'] * R + \
          param_d['u'] * s

    return res


def cal_probability(y):
    p = None if y is None else y / (1 + y)
    return p


def build_weather_avg(data, week):
    """
    参数:
    data: 直接从数据库拿到的raw data, 即wk1 或 wk2 或 wk1_to_2
    week: 前1周或者前2周
    """
    T_avg = None
    W_avg = None
    if len(data) > 0:
        t_list = [float(i.temperature_average) for i in data]
        w_list = [float(i.wind_speed) for i in data]

        for i in range(7 * week - len(data)):
            t_list.append(choice(t_list))

        T_avg = sum(t_list) / len(t_list)
        W_avg = sum(w_list) / len(w_list)

    return T_avg, W_avg


def build_pm_avg_list(data, current_time, week):
    """
    参数:
    data: 从数据库拿到的初始结果，即 wk1, wk2
    current_time: 当前时间
    week = 计算1周的还是2周的结果

    处理均值的方式:
    将一天分成4个时间段，每个时间段先求均值，再用4个时间段的均值之和求每日均值
    """

    # PM 值每天会有很多记录(目前每小时会拿到一个)，所以先拿到一天内每个小时的pm2.5, 和pm10，计算每天的均值;
    # 再将每天的均值加起来，除以7或者14，计算一周内的均值

    # step 1
    # 先准备一个空的字典，里面有7个小空字典, 为拿一天内每小时的数据做准备
    # pm_dict = {"今天":{}, "一天前":{},..."6天前":{}}
    pm_dict = {}
    for i in range(7 * week):
        pm_dict[(current_time - timedelta(days=i)).day] = []

    # step2
    pm25_avg_list, pm10_avg_list = [], []
    # 先将wk1中每天的数据，分开分别放到 pm_dict[k]中
    for j in data:
        for k in pm_dict:
            if j.pm_date.day == k:
                pm_dict[k].append(j)
    # 对每天的数据调用 build_pm_avg_per_day
    for k, v in pm_dict.items():
        if len(pm_dict[k]) > 0:
            pm25_avg_today, pm10_avg_today = build_pm_avg_per_day(pm_dict[k])
            pm25_avg_list.append(pm25_avg_today)
            pm10_avg_list.append(pm10_avg_today)
    return pm25_avg_list, pm10_avg_list


# 该函数中， 2个threshold 按照标准定义，分别是35和50 微克每立方米.
# 若超过阈值，则一周内的超标天数加1
def count_pm_days(pm25_avg_list, pm10_avg_list):
    M25 = 0
    M10 = 0
    if len(pm25_avg_list) > 0:
        for i in pm25_avg_list:
            if i > pm_25_threshold:
                M25 += 1

    if len(pm10_avg_list) > 0:
        for j in pm10_avg_list:
            if j > pm_10_threshold:
                M10 += 1

    return M25, M10
