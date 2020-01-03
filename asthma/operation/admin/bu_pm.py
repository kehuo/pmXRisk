#!/usr/bin/python
# encoding=utf8
import traceback
from datetime import datetime, timedelta
import json
from sqlalchemy import or_, and_, func
from bb_logger.logger import Logger
from models.db_models import City, PM
from common.utils.db import build_rows_result
from common.utils.http import getValueWithDefault
from common.utils.time_utils import buildTimeCondition


def getPMList(db, args):
    page = getValueWithDefault(args, 'page', 1)
    pageSize = getValueWithDefault(args, 'pageSize', 1000)
    cityCode = getValueWithDefault(args, 'cityCode', None)
    startdate = getValueWithDefault(args, 'startdate', None)
    enddate = getValueWithDefault(args, 'enddate', None)

    try:
        # 默认返回所有城市, join City表
        query = db.session.query(
            PM.id, PM.pm_25, PM.pm_10, func.date_format(PM.pm_date, "%Y-%m-%d %H"),
            func.date_format(PM.updated_at, "%Y-%m-%d %H:%i:%s"),
            PM.city_code, City.name_zh, City.province_zh
        ) \
            .join(City, City.city_code == PM.city_code)
        if cityCode is not None:
            # 如果要查询某个城市，再过滤一层
            query = query.filter(PM.city_code == cityCode)
        timeCondition = buildTimeCondition(PM, startdate, enddate, tag='pm_date')
        if len(timeCondition) > 0:
            # 如果要查询某个时间段，再过滤一层
            query = query.filter(and_(*timeCondition))

        offset = (page - 1) * pageSize
        total = query.count()
        rows = query.order_by(PM.pm_date.desc()) \
            .offset(offset).limit(pageSize).all()
        items = ['id', 'pm_25', 'pm_10', 'pm_date', 'updated_at', 'city_code', 'city_name', 'province_name']
        data = build_rows_result(rows, items)

        rst = {
            'code': 'SUCCESS',
            'data': {
                'total': total,
                'pm_info': data
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
