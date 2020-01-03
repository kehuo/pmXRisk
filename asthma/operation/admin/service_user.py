#!/usr/bin/python
# encoding=utf8

from flask_restful import reqparse, Resource
from common.utils.http import encoding_resp_utf8, build_failed_response

import operation.admin.bu_user as Utils

from app.init_global import global_var
from operation.operation_utils import check_permission
from flask_jwt_extended import ( get_jwt_identity, verify_jwt_in_request)


class Users(Resource):
    @check_permission([1])
    def get(self, **auth):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, required=False, location='args')
        parser.add_argument('pageSize', type=int, required=False, location='args')
        parser.add_argument('disabled', type=int, required=False, location='args')
        args = parser.parse_args()

        rst = Utils.getUserList(global_var['db'], args)
        return encoding_resp_utf8(rst)

    @check_permission([1])
    def post(self, **auth):
        parser = reqparse.RequestParser()
        parser.add_argument('data', type=dict, required=True, location='json')
        args = parser.parse_args()

        rst = Utils.createUser(global_var['db'], args)
        return encoding_resp_utf8(rst)


class UserOne(Resource):
    @check_permission([1])
    def get(self, user_id, **auth):
        rst = Utils.getUserOne(global_var['db'], user_id)
        return encoding_resp_utf8(rst)

    @check_permission([1])
    def put(self, user_id,**auth):
        parser = reqparse.RequestParser()
        parser.add_argument('data', type=dict, required=True, location='json')
        args = parser.parse_args()

        rst = Utils.updateUser(global_var['db'], args, user_id)
        return encoding_resp_utf8(rst)

    @check_permission([1])
    def delete(self, user_id, **auth):
        rst = Utils.deleteUserOne(global_var['db'], user_id)
        return encoding_resp_utf8(rst)


class CurrentUser(Resource):
    def get(self):
        try:
            verify_jwt_in_request()

        except Exception as e:
            return {'errorCode': 'Unauthorized Access Token', 'errorMessage': '无效的access token'}, 401
        current_user = get_jwt_identity()
        db = global_var['db']
        rst = Utils.getCurrentUser(global_var['db'], current_user)
        
        return encoding_resp_utf8(rst)
