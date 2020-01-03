#!/usr/bin/python
# encoding=utf8
import traceback
from bb_logger.logger import Logger
from models.db_models import RiskComment
from common.utils.db import build_rows_result, update_record, build_one_result
from common.utils.http import getValueWithDefault


def getRiskCommentList(db, args):
    page = getValueWithDefault(args, 'page', 1)
    pageSize = getValueWithDefault(args, 'pageSize', 1000)
    disabled = getValueWithDefault(args, 'disabled', None)

    try:
        query = db.session.query(
            RiskComment.id, RiskComment.level, RiskComment.threshold, RiskComment.comment)
        
        offset = (page - 1) * pageSize
        total = query.count()
        rows = query.order_by(RiskComment.id).offset(offset).limit(pageSize).all()
        items = ['id', 'level', 'threshold', 'comment']
        data = build_rows_result(rows, items)

        rst = {
            'code': 'SUCCESS',
            'data': {
                'total': total,
                'comments': data
            }
        }
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
        rst = {
            'code': 'FAILURE',
            'message': 'Failed'
        }
    return rst


def createRiskComment(db, args):
    data = args['data']
    print(data)
    try:
        record = RiskComment(
            level=data['level'],
            threshold=data['threshold'],
            comment = data['comment']
        )
        db.session.add(record)
        db.session.commit()

        rst = {
            'code': 'SUCCESS',
            'data': {
                'id': record.id,
            }
        }
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
        db.session.rollback()
        rst = {
            'code': 'FAILURE',
            'message': 'Failed'
        }
    return rst


def getRiskCommentOne(db, risk_comment_id):
    try:
        record = db.session.query(
            RiskComment.id, RiskComment.level, RiskComment.threshold, RiskComment.comment) \
            .filter(RiskComment.id == risk_comment_id) \
            .first()
        if record is None:
            rst = {
                'code': 'FAILURE',
                'message': 'get user one failed, not exist'
            }
        else:
            items = ['id', 'level', 'threshold', 'comment']
            data = build_one_result(record, items)
            rst = {
                'code': 'SUCCESS',
                'data': data
            }
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
        rst = {
            'code': 'FAILURE',
            'message': 'Failed'
        }
    return rst


def updateRiskCommentOne(db, args, risk_comment_id):
    data = args['data']
    try:
        record = db.session.query(RiskComment).filter(RiskComment.id == risk_comment_id).first()
        if record is None:
            rst = {
                'code': 'FAILURE',
                'message': 'update user one failed, not exist'
            }
        else:
            items = ['level', 'threshold', 'comment']
            update_record(record, items, data)
            # update password
            # db.session.add(record)
            db.session.commit()

            rst = {
                'code': 'SUCCESS',
                'data': {
                    'id': risk_comment_id,
                }
            }
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
        db.session.rollback()
        rst = {
            'code': 'FAILURE',
            'message': 'Failed'
        }
    return rst


def deleteRiskCommentOne(db, risk_comment_id):
    try:
        record = db.session.query(RiskComment).filter(RiskComment.id == risk_comment_id).first()
        if record is None:
            rst = {
                'code': 'FAILURE',
                'message': 'delete user one failed, not exist'
            }
        else:
            db.session.delete(record)
            db.session.commit()

            rst = {
                'code': 'SUCCESS',
                'data': {
                    'id': risk_comment_id,
                }
            }
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
        db.session.rollback()
        rst = {
            'code': 'FAILURE',
            'message': 'Failed'
        }
    return rst
