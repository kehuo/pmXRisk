#!/usr/bin/python
# encoding=utf8
import traceback
from sqlalchemy import and_, func
from bb_logger.logger import Logger
from models.db_models import City, Weather
from common.utils.db import build_rows_result
from common.utils.http import getValueWithDefault
from common.utils.time_utils import buildTimeCondition


# weather数据
def getWeatherList(db, args):
    page = getValueWithDefault(args, 'page', 1)
    pageSize = getValueWithDefault(args, 'pageSize', 1000)
    cityCode = getValueWithDefault(args, 'cityCode', None)
    startdate = getValueWithDefault(args, 'startdate', None)
    enddate = getValueWithDefault(args, 'enddate', None)
    try:
        # 默认所有城市所有数据
        query = db.session.query(
            Weather.id, func.date_format(Weather.weather_date, "%Y-%m-%d"),
            Weather.temperature_average,
            Weather.wind_power, Weather.humidity, Weather.weather_condition,
            func.date_format(Weather.updated_at, "%Y-%m-%d"),
            Weather.city_code, City.name_zh, City.province_zh
        ) \
            .join(City, City.city_code == Weather.city_code)
        if not cityCode is None:
            # 如果参数有citycode，再做一次过滤
            query = query.filter(Weather.city_code == cityCode)
        timeCondition = buildTimeCondition(Weather, startdate, enddate, tag='weather_date')
        # 如果参数中还设置了开始和结束时间，再做一次
        if len(timeCondition) > 0:
            query = query.filter(and_(*timeCondition))
        offset = (page - 1) * pageSize
        total = query.count()
        rows = query.order_by(Weather.weather_date.desc()) \
            .offset(offset).limit(pageSize).all()
        items = ['id', 'weather_date', 'temperature_average', 'wind_power', 'humidity',
                 'weather_condition', 'updated_at', 'city_code', 'city_name', 'province_name']
        data = build_rows_result(rows, items)
        rst = {
            'code': 'SUCCESS',
            'data': {
                'total': total,
                'weather_info': data
            }
        }
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
        rst = {
            'code': 'FAILURE',
            'message': 'Failed to get weather info list'
        }
    return rst
