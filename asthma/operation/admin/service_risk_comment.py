#!/usr/bin/python
# encoding=utf8

from flask_restful import reqparse, Resource
from common.utils.http import encoding_resp_utf8, build_failed_response
import operation.admin.bu_risk_comment as Utils
from app.init_global import global_var
from operation.operation_utils import check_permission
from flask_jwt_extended import ( get_jwt_identity, verify_jwt_in_request)


class RiskComments(Resource):
    @check_permission([1])
    def get(self, **auth):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, required=False, location='args')
        parser.add_argument('pageSize', type=int, required=False, location='args')
        args = parser.parse_args()

        rst = Utils.getRiskCommentList(global_var['db'], args)
        return encoding_resp_utf8(rst)

    @check_permission([1])
    def post(self, **auth):
        parser = reqparse.RequestParser()
        parser.add_argument('data', type=dict, required=True, location='json')
        args = parser.parse_args()

        rst = Utils.createRiskComment(global_var['db'], args)
        return encoding_resp_utf8(rst)


class RiskCommentOne(Resource):
    @check_permission([1])
    def get(self, risk_comment_id, **auth):
        rst = Utils.getRiskCommentOne(global_var['db'], risk_comment_id)
        return encoding_resp_utf8(rst)

    @check_permission([1])
    def put(self, risk_comment_id,**auth):
        parser = reqparse.RequestParser()
        parser.add_argument('data', type=dict, required=True, location='json')
        args = parser.parse_args()

        rst = Utils.updateRiskCommentOne(global_var['db'], args, risk_comment_id)
        return encoding_resp_utf8(rst)

    @check_permission([1])
    def delete(self, risk_comment_id, **auth):
        rst = Utils.deleteRiskCommentOne(global_var['db'], risk_comment_id)
        return encoding_resp_utf8(rst)

