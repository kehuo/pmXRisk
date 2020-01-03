#!/usr/bin/python
# encoding=utf8

from flask_restful import reqparse, Resource
from common.utils.http import encoding_resp_utf8, build_failed_response
import operation.admin.bu_weather as Utils
from app.init_global import global_var
from operation.operation_utils import check_permission
from flask_jwt_extended import ( get_jwt_identity, verify_jwt_in_request)


class WeatherInfos(Resource):
    @check_permission([1])
    def get(self, **auth):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, required=False, location='args')
        parser.add_argument('pageSize', type=int, required=False, location='args')
        parser.add_argument('cityCode', type=str, required=False, location='args')
        parser.add_argument('startdate', type=str, required=False, location='args')
        parser.add_argument('enddate', type=str, required=False, location='args')
        args = parser.parse_args()

        rst = Utils.getWeatherList(global_var['db'], args)
        return encoding_resp_utf8(rst)
