#!/usr/bin/python
# encoding=utf8
import traceback
from models.db_models import City
from bb_logger.logger import Logger


def get_city_list(global_var):
    """
    2019 08 02
    默认返回两部分数据:
    1 一个列表, 包含34个省份 ['甘肃', '湖南']
    2 一个列表, 列表中每个子项为一个省，是一个字典, 'sub'键是一个子列表, 其中所包括该省的市
    [
    {"name":'甘肃', "sub":["兰州", "陇南"]}, 
    {"name":"陕西", "sub":["宝鸡","西安"]}
    ]
    """

    db = global_var['db']
    try:
        # 获取所有省份
        all_provinces = db.session.query(City.province_zh).distinct().all()
        province_list = [i[0] for i in all_provinces]
        # 拿所有的城市数据
        all_cities = db.session.query(City.province_zh, City.name_zh).all()
        data = dict()
        data['provinces'] = province_list
        tmp = []
        for i in province_list:
            current_prov = dict()
            current_prov['name'] = i
            current_prov['sub'] = []
            for j in all_cities:
                if j.province_zh == i:
                    current_prov['sub'].append(j.name_zh)
            tmp.append(current_prov)

        data['cities'] = tmp
        res = {'code': 'SUCCESS', 'data': data, 'len':len(data['cities'])}
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
        res = {
            'code': 'FAILURE',
            'message': 'Failed to get city info'
        }
    return res
