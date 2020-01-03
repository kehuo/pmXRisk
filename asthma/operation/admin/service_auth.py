#!/usr/bin/python
# encoding=utf8

from flask_restful import reqparse, Resource
from common.utils.http import encoding_resp_utf8
import operation.admin.bu_auth as AuthUtils
from app.init_global import global_var
from flask import Response
from flask_jwt_extended import (create_access_token, create_refresh_token, get_jwt_identity, verify_jwt_in_request)
import json


class LogIn(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('userName', type=str, required=True, location='json')
		parser.add_argument('password', type=str, required=True, location='json')
		args = parser.parse_args()

		rst = AuthUtils.login(global_var['db'], args)
		access_token = create_access_token(identity=args['userName'])
		resp = Response(json.dumps(rst, ensure_ascii=False), content_type="application/json; charset=utf-8")
		resp.set_cookie('_op_token_dv', access_token)
		resp.headers['x-bb-set-bauthtoken'] = access_token
		resp.headers['Access-Control-Expose-Headers'] = 'x-bb-set-bauthtoken'
		return resp


class LogOut(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('id', type=str, required=True, location='json')
		args = parser.parse_args()

		rst = AuthUtils.logout(global_var['db'], args)

		return encoding_resp_utf8(rst)
