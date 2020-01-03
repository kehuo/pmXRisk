#!/usr/bin/python
# encoding=utf8
import traceback
from datetime import datetime, timedelta
import json
from sqlalchemy import and_, or_, func
from common.utils.time_utils import buildTimeCondition
from models.db_models import Notification
from bb_logger.logger import Logger
from common.utils.db import build_rows_result, build_general_filter, update_record, build_one_result
from operation.operation_utils import getPasswordCrypt
from common.utils.http import getValueWithDefault


# 某一段时间内的报错信息
def getNotificationList(db, args):
    page = getValueWithDefault(args, 'page', 1)
    pageSize = getValueWithDefault(args, 'pageSize', 1000)
    level = getValueWithDefault(args, 'level', None)
    startdate = getValueWithDefault(args, 'startdate', None)
    enddate = getValueWithDefault(args, 'enddate', None)
    try:
        query = db.session.query(
            Notification.id, func.date_format(Notification.notification_date, "%y-%m-%d %H:%i:%s"),
            Notification.level_id,
            Notification.level_name,
            Notification.notification
        )
        timeCondition = buildTimeCondition(Notification, startdate, enddate, tag='notification_date')

        if len(timeCondition) > 0:
            query = query.filter(and_(*timeCondition))
        if not level is None:
            query = query.filter(Notification.level_id >= level)
        offset = (page - 1) * pageSize
        total = query.count()
        rows = query.order_by(Notification.notification_date.desc()) \
            .offset(offset).limit(pageSize).all()
        items = ['id', 'notification_date', 'level_id', 'level_name', 'notification']
        data = build_rows_result(rows, items)
        rst = {
            'code': 'SUCCESS',
            'data': {
                'total': total,
                'items': data
            }
        }
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
        rst = {
            'code': 'FAILURE',
            'message': 'Failed to get notification list'
        }
    return rst

