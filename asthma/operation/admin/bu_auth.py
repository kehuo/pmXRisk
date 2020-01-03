#!/usr/bin/python
# encoding=utf8
import traceback
from bb_logger.logger import Logger
from models.db_models import User
from common.utils.db import build_one_result
from operation.operation_utils import getPasswordCrypt


def login(db, args):
    try:
        record = db.session.query(User) \
            .filter(User.name == args['userName']) \
            .filter(User.disabled == 0).first()
        if record is None:
            rst = {
                'code': 'FAILURE',
                'message': 'get user one failed, not exist'
            }
        else:
            record = db.session.query(
                User.id, User.name, User.fullname, User.email, User.disabled, User.role_id) \
                .filter(User.name == args['userName']) \
                .filter(User.password == getPasswordCrypt(args['password'])).first()
            if record is None:
                rst = {
                    "code": "FAILURE",
                    "message": "Incorrect Password"
                }
            else:
                items = ['id', 'name', 'fullname', 'email', 'disabled', 'role_id']
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


def logout(db, args):
    # TODO
    rst = {
        'code': 'SUCCESS',
        'data': args['id']
    }
    return rst
