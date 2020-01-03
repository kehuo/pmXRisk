#!/usr/bin/python
# encoding=utf8
from datetime import datetime
import traceback
from bb_logger.logger import Logger
from models.db_models import Weather, PM, RiskComment
from data.param import pm_formula_params
from climate.bu_logic.utils import build_weather_avg, count_pm_days, \
    asthma_formula, cal_probability, search_week_rawdata_by_cityname, build_pm_avg_list


def get_T_W(global_var, args):
    res = {}
    try:
        wk1, wk2 = search_week_rawdata_by_cityname(Weather, global_var, args)
        T_wk1, W_wk1 = build_weather_avg(wk1, 1)
        T_wk2, W_wk2 = build_weather_avg(wk2, 2)
        res['T_wk1'] = T_wk1
        res['T_wk2'] = T_wk2
        res['W_wk1'] = W_wk1
        res['W_wk2'] = W_wk2
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
    return res


def get_M(global_var, args):
    res = {}
    try:
        wk1, wk2 = search_week_rawdata_by_cityname(PM, global_var, args)
        # 这里计算一周内/ 2周内 每天的PM均值, 存储在以下4个列表中
        pm25_avg_list_wk1, pm10_avg_list_wk1 = build_pm_avg_list(wk1, datetime.now(), 1)
        pm25_avg_list_wk2, pm10_avg_list_wk2 = build_pm_avg_list(wk2, datetime.now(), 2)
        # 对上面的4个列表分别计算累计的超标天数
        M25_wk1, M10_wk1 = count_pm_days(pm25_avg_list_wk1, pm10_avg_list_wk1)
        M25_wk2, M10_wk2 = count_pm_days(pm25_avg_list_wk2, pm10_avg_list_wk2)
        res['M25_wk1'] = M25_wk1
        res['M10_wk1'] = M10_wk1
        res['M25_wk2'] = M25_wk2
        res['M10_wk2'] = M10_wk2
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
    return res


def cal_asthma_risk(global_var, args):
    db = global_var['db']
    # 获取哮喘模型所需参数 b, t, r, f, w, u
    p25_dict_wk1 = pm_formula_params['wk1']['pm_25']
    p10_dict_wk1 = pm_formula_params['wk1']['pm_10']

    p25_dict_wk2 = pm_formula_params['wk2']['pm_25']
    p10_dict_wk2 = pm_formula_params['wk2']['pm_10']

    # 获取哮喘模型所需的变量值 M, T, W, F, R, s
    # T_wk1, W_wk1, T_wk2, W_wk2 = get_T_W(global_var, args)
    try:
        TW_res = get_T_W(global_var, args)
        M_res = get_M(global_var, args)
        F = int(args['isFever'])
        # 这2个不显著变量，暂时设置为0
        R = 0
        s = 0
        # 一周的结果
        risk_pm25_wk1 = asthma_formula(p25_dict_wk1, M_res['M25_wk1'], TW_res['T_wk1'], TW_res['W_wk1'], F, R, s)
        risk_pm10_wk1 = asthma_formula(p10_dict_wk1, M_res['M10_wk1'], TW_res['T_wk1'], TW_res['W_wk1'], F, R, s)
        prob_pm25_wk1 = cal_probability(risk_pm25_wk1)
        prob_pm10_wk1 = cal_probability(risk_pm10_wk1)
        # 2周结果
        risk_pm25_wk2 = asthma_formula(p25_dict_wk2, M_res['M25_wk2'], TW_res['T_wk2'], TW_res['W_wk2'], F, R, s)
        risk_pm10_wk2 = asthma_formula(p10_dict_wk2, M_res['M10_wk2'], TW_res['T_wk2'], TW_res['W_wk2'], F, R, s)
        prob_pm25_wk2 = cal_probability(risk_pm25_wk2)
        prob_pm10_wk2 = cal_probability(risk_pm10_wk2)

        # 根据概率从risk_comment数据库中拿comment
        comment_pm25_wk1, comment_pm10_wk1, comment_pm25_wk2, comment_pm10_wk2 = "", "", "", ""
        if prob_pm25_wk1 is not None:
            comment_pm25_wk1 = db.session.query(RiskComment). \
                filter(prob_pm25_wk1 <= RiskComment.threshold).all()[0].comment
        if prob_pm10_wk1 is not None:
            comment_pm10_wk1 = db.session.query(RiskComment) \
                .filter(prob_pm10_wk1 <= RiskComment.threshold).all()[0].comment
        if prob_pm25_wk2 is not None:
            comment_pm25_wk2 = db.session.query(RiskComment) \
                .filter(prob_pm25_wk2 <= RiskComment.threshold).all()[0].comment
        if prob_pm10_wk2 is not None:
            comment_pm10_wk2 = db.session.query(RiskComment) \
                .filter(prob_pm10_wk2 <= RiskComment.threshold).all()[0].comment

        data = {}
        # 2019-08-05 周一下午 3：40 注释
        # 当前 v1 版本
        # 1 目前不需要显示risk，只需要显示prob，所以数据先只返回prob. 以后版本如果需要risk，再往 data 字典中加
        # 2 目前默认返回2周数据，但是可能以后需要分开，所以这里加入week=1和week=2.

        # 2019-08-07 注释
        # 和产品确认，目前厦大老师建议使用 PM25_prob 做为结果
        if args["week"] == 1:
            if not prob_pm25_wk1 is None:
                data['PM25_prob'] = prob_pm25_wk1
            if not prob_pm10_wk1 is None:
                data['PM10_prob'] = prob_pm10_wk1
            data['PM25_comment'] = comment_pm25_wk1
            data['PM10_comment'] = comment_pm10_wk1
            res = {"code": "SUCCESS", "data": data}
        elif args['week'] == 2 or args['week'] is None:
            if prob_pm25_wk2 is not None:
                data['PM25_prob'] = prob_pm25_wk2
            if prob_pm10_wk2 is not None:
                data['PM10_prob'] = prob_pm10_wk2
            data['PM25_comment'] = comment_pm25_wk2
            data['PM10_comment'] = comment_pm10_wk2
            res = {"code": "SUCCESS", "data": data}
        else:
            res = {"code": "FAILURE", "message": "week index not supported"}
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
        res = {
            'code': 'FAILURE',
            'message': 'Failed to cal asthma risk'
        }
    return res
