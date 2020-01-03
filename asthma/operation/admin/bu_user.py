#!/usr/bin/python
# encoding=utf8
import traceback
from bb_logger.logger import Logger
from models.db_models import User
from common.utils.db import build_rows_result, update_record, build_one_result
from operation.operation_utils import getPasswordCrypt
from common.utils.http import getValueWithDefault


def getUserList(db, args):
    page = getValueWithDefault(args, 'page', 1)
    pageSize = getValueWithDefault(args, 'pageSize', 1000)
    disabled = getValueWithDefault(args, 'disabled', None)

    try:
        query = db.session.query(
            User.id, User.name, User.fullname, User.email, User.disabled, User.role_id)
        if disabled is not None:
            query = query.filter(User.disabled == disabled)

        offset = (page - 1) * pageSize
        total = query.count()
        rows = query.order_by(User.id).offset(offset).limit(pageSize).all()
        items = ['id', 'name', 'fullname', 'email', 'disabled', 'role_id']
        data = build_rows_result(rows, items)

        rst = {
            'code': 'SUCCESS',
            'data': {
                'total': total,
                'users': data
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


def createUser(db, args):
    data = args['data']
    try:
        record = User(
            name=data['name'],
            fullname=getValueWithDefault(data, 'fullname', ''),
            # 创建用户时disabled必须是0
            disabled=0,
            email=getValueWithDefault(data, 'email', ''),
            password=getPasswordCrypt(data['password']),
            role_id=data['role_id']
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


def getUserOne(db, user_id):
    try:
        record = db.session.query(
            User.id, User.name, User.fullname, User.email, User.disabled, User.role_id) \
            .filter(User.id == user_id) \
            .first()
        if record is None:
            rst = {
                'code': 'FAILURE',
                'message': 'get user one failed, not exist'
            }
        else:
            items = ['id', 'name', 'fullName', 'email', 'disabled', 'roleId']
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


def getCurrentUser(db, user_name):
    try:
        record = db.session.query(
            User.id, User.name, User.fullname, User.email, User.disabled, User.role_id) \
            .filter(User.name == user_name) \
            .first()
        if record is None:
            rst = {
                'code': 'FAILURE',
                'message': 'get user one failed, not exist'
            }
        else:
            items = ['id', 'name', 'fullName', 'email', 'disabled', 'roleId']
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


def updateUser(db, args, user_id):
    data = args['data']
    try:
        record = db.session.query(User).filter(User.id == user_id).first()
        if record is None:
            rst = {
                'code': 'FAILURE',
                'message': 'update user one failed, not exist'
            }
        else:
            items = ['name', 'org_code', 'fullname', 'email', 'disabled', 'role_id']
            password = data.get('password', None)
            update_record(record, items, data)
            # update password
            if password is not None and password != '':
                record.password = getPasswordCrypt(password)
            # db.session.add(record)
            db.session.commit()

            rst = {
                'code': 'SUCCESS',
                'data': {
                    'id': user_id,
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


def deleteUserOne(db, user_id):
    try:
        record = db.session.query(User).filter(User.id == user_id).first()
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
                    'id': user_id,
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
