#!/usr/bin/python
# encoding=utf8

from flask_restful import reqparse, Resource
from common.utils.http import encoding_resp_utf8, build_failed_response

import operation.admin.bu_city as Utils

from app.init_global import global_var
from operation.operation_utils import check_permission
from flask_jwt_extended import ( get_jwt_identity, verify_jwt_in_request)


class Cities(Resource):
    @check_permission([1])
    def get(self, **auth):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, required=False, location='args')
        parser.add_argument('pageSize', type=int, required=False, location='args')
        parser.add_argument('keyword', type=str, required=False, location='args')

        args = parser.parse_args()

        rst = Utils.getCityList(global_var['db'], args)
        return encoding_resp_utf8(rst)

    @check_permission([1])
    def post(self, **auth):
        parser = reqparse.RequestParser()
        parser.add_argument('data', type=dict, required=True, location='json')
        args = parser.parse_args()

        rst = Utils.createCity(global_var['db'], args)
        return encoding_resp_utf8(rst)


class CityOne(Resource):
    @check_permission([1])
    def get(self, city_id, **auth):
        rst = Utils.getCityOne(global_var['db'], city_id)
        return encoding_resp_utf8(rst)

    @check_permission([1])
    def put(self, city_id, **auth):
        parser = reqparse.RequestParser()
        parser.add_argument('data', type=dict, required=True, location='json')
        args = parser.parse_args()

        rst = Utils.updateCity(global_var['db'], args, city_id)
        return encoding_resp_utf8(rst)

    @check_permission([1])
    def delete(self, city_id, **auth):
        rst = Utils.deleteCityOne(global_var['db'], city_id)
        return encoding_resp_utf8(rst)


