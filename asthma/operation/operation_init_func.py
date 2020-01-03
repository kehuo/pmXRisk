#!/usr/bin/python
# encoding=utf8
from datetime import timedelta
from flask_jwt_extended import JWTManager

def init_operation(app, global_var):
    ok = True
    err_msg = ''
    try:
        if isinstance(app.config['JWT_ACCESS_TOKEN_EXPIRES'], int):
            time = app.config['JWT_ACCESS_TOKEN_EXPIRES']
            app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=time)

            global_var['secretKey'] = app.config['SECRET_KEY']
            jwt = JWTManager(app)

    except Exception as e:
        ok = False
        print(ok)
        err_msg = "failed to init operation"
    return ok, err_msg

