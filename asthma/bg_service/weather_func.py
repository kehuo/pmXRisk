from datetime import datetime
from requests import get
from data.param import wind_power_speed_map


def collect_weather_one(city_code, conn, cursor):
    # is_success是一个标志位，如果抓取成功，最后返回 True，否则 False
    is_success = True
    errors = {"city": city_code,
              "errors": []}

    # 服务网站: https://www.tianqiapi.com/user
    app_id = 67548155
    app_secret = "BGrju1UP"
    url = "https://www.tianqiapi.com/api/?version=v1&cityid=%s&appid=%s&appsecret=%s" % \
          (city_code, app_id, app_secret)

    try:
        res = get(url, timeout=1).json()
        data = res['data'][0]
    except Exception as e:
        is_success = False
        n1 = '%s调用weather API失败' % (city_code)
        errors["errors"].append(n1)
        return is_success, errors

    # 以下从res中获取数据. 对重要的部分 temperature, wind 单独做了 try_except处理, 对其他不重要数据, 一起try处理.
    # 1 从res中获取气温字段
    try:
        temperature_highest = int(data['tem1'].split("℃")[0])
        temperature_lowest = int(data['tem2'].split("℃")[0])
        # 均温的计算方式如下:
        # 1 如果08 14 20 02 4个标称点的数据都能拿到，那么用4个数据之和除以4，获取均温;
        # 2 如果有任何一个标称数据无法获取，那么用 highest 和 lowest 之和除以2， 获取均温.

        # step1 标称时间列表
        nominal_list = ["08", "14", "20", "02"]
        t = {}
        count = 0
        for i in nominal_list:
            for j in data["hours"]:
                query = j["day"].split("日")[1].split("时")[0]
                if query == i:
                    t[i] = int(j["tem"].split("℃")[0])
                    count += 1
                    break
        # step2 判断 4 个标称值是否都取到
        if count == 4:
            temperature_average = (t["08"] + t["14"] + t["20"] + t["02"]) / 4
        else:
            temperature_average = (temperature_highest + temperature_lowest) / 2

        # 以上气温已经处理完毕, 再获取其他字段
    except Exception as e:
        is_success = False
        n2 = '获取%stemperature信息失败,响应:\n%s' % (city_code, str(data))
        errors["errors"].append(n2)
        return is_success, errors

    # 2 从res中获取风速和风力等级
    try:
        for k, v in wind_power_speed_map.items():
            if k in data['win_speed']:
                wind_speed = wind_power_speed_map[k]
        wind_power = data['win_speed']
    except Exception as e:
        is_success = False
        n3 = '获取%s wind信息失败, 响应\n%s' % (city_code, str(data))
        errors["errors"].append(n3)
        return is_success, errors

    # 以下字段在一个try下处理
    try:
        # 3 湿度
        humidity = data['humidity']
        # 4 天气情况, 晴，阴，多云等
        weather_condition = data['wea']
        # 5 紫外线, 血糖， 穿衣
        # index[0] 紫外线
        # index[2] 血糖
        # index[3] 穿衣
        # index[5] 空气污染扩散指数 (暂时没抓取)
        ultraviolet = data['index'][0]['level']
        ultraviolet_description = data['index'][0]['desc']

        blood_sugar = data['index'][2]['level']
        blood_sugar_description = data['index'][2]['desc']

        dress = data['index'][3]['level']
        dress_description = data['index'][3]['desc']

        # 6 weather_date 这个字段记录当天的天气
        weather_date = data['date']
        # 7 星期
        week = data['week']
    except Exception as e:
        is_success = False
        n4 = '获取%s 其他weather信息失败,响应\n%s' % (city_code, str(data))
        errors["errors"].append(n4)
        return is_success, errors

    # 以上所有数据已经获取完毕, 以下为写入数据库的部分
    # 根据 weather_date 搜索数据库
    # 如果没有，那么新增 insert;
    # 如果有，那么更新 UPDATE.
    try:
        cursor.execute("select name_zh from city where city_code=%s" % city_code)
        name_zh = cursor.fetchone()[0]
        sql_search = "SELECT * from weather where weather_date='%s' and city_code=%s" % (weather_date, city_code)
        if cursor.execute(sql_search) == 0:
            # 新增
            sql_insert = "INSERT INTO weather (city_code,\
                                                weather_date,\
                                                week,\
                                                temperature_average,\
                                                temperature_highest,\
                                                temperature_lowest,\
                                                wind_power,\
                                                wind_speed,\
                                                humidity,\
                                                weather_condition,\
                                                ultraviolet,\
                                                ultraviolet_description,\
                                                blood_sugar,\
                                                blood_sugar_description,\
                                                dress, dress_description,\
                                                created_at,\
                                                updated_at)\
                        VALUES ('%s', '%s', '%s', '%s', '%s' ,'%s', '%s', '%s','%s', \
                                '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
                         (city_code,
                          weather_date,
                          week,
                          temperature_average,
                          temperature_highest,
                          temperature_lowest,
                          wind_power,
                          wind_speed,
                          humidity,
                          weather_condition,
                          ultraviolet,
                          ultraviolet_description,
                          blood_sugar,
                          blood_sugar_description,
                          dress,
                          dress_description,
                          datetime.now(),
                          datetime.now())
            cursor.execute(sql_insert)
            conn.commit()
        else:
            # 更新
            sql_update = "UPDATE weather SET temperature_average='%s', \
                                            temperature_highest='%s',\
                                            temperature_lowest='%s',\
                                            wind_power='%s',\
                                            wind_speed='%s',\
                                            humidity='%s',\
                                            weather_condition='%s',\
                                            ultraviolet='%s',\
                                            ultraviolet_description='%s',\
                                            blood_sugar='%s',\
                                            blood_sugar_description='%s',\
                                            dress='%s',\
                                            dress_description='%s',\
                                            updated_at='%s'\
                                    where weather_date='%s' and city_code='%s'" % (temperature_average,
                                                                                   temperature_highest,
                                                                                   temperature_lowest,
                                                                                   wind_power,
                                                                                   wind_speed,
                                                                                   humidity,
                                                                                   weather_condition,
                                                                                   ultraviolet,
                                                                                   ultraviolet_description,
                                                                                   blood_sugar,
                                                                                   blood_sugar_description,
                                                                                   dress,
                                                                                   dress_description,
                                                                                   datetime.now(),
                                                                                   weather_date,
                                                                                   city_code)
            cursor.execute(sql_update)
            conn.commit()
    except Exception as e:
        is_success = False
        n5 = '%s写入数据库失败' % city_code
        errors["errors"].append(n5)
        return is_success, errors
    return is_success, errors
