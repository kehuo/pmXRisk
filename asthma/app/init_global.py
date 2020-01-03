#!/usr/bin/python
# encoding=utf8
global global_var
global_var = {}

import os
import sys
import pymysql
from model_config import pre_global_init_func, post_global_init_func
from operation.operation_init_func import init_operation
from app.global_init_func import init_db

pymysql.install_as_MySQLdb()
folder = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

# global init func
init_funcs_map = [
    init_db
]


def init_global(app):
    global_var['version'] = app.config['VERSION']
    global_var['description'] = app.config['SERVICE_DESC']
    global_var['service'] = app.config['SERVICE_NAME']
    global_var['db_host'] = app.config['DB_HOST']
    global_var['models'] = app.config['MODELS'].split(',')
    global_var['PYMYSQL_HOST'] = app.config['PYMYSQL_HOST']
    global_var['PYMYSQL_PORT'] = app.config['PYMYSQL_PORT']
    global_var['PYMYSQL_USER'] = app.config['PYMYSQL_USER']
    global_var['PYMYSQL_PASSWORD'] = app.config['PYMYSQL_PASSWORD']
    global_var['PYMYSQL_DBNAME'] = app.config['PYMYSQL_DBNAME']

    # add model init func
    # pre
    init_funcs = []
    for model in global_var['models']:
        model = model.strip()
        func = pre_global_init_func.get(model, None)
        if func is None:
            continue
        init_funcs.extend(func)

    init_funcs.extend(init_funcs_map)

    # post
    for model in global_var['models']:
        model = model.strip()
        func = post_global_init_func.get(model, None)
        if func is None:
            continue
        init_funcs.extend(func)

    for func in init_funcs:
        ok, err_msg = func(app, global_var)
        if not ok:
            print('failed to init params: ', err_msg, func)
            sys.exit(0)
    return
