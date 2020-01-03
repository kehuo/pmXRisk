import hashlib
from flask_jwt_extended import (create_access_token, create_refresh_token, get_jwt_identity, verify_jwt_in_request)
from functools import wraps
from models.db_models import User
from app.init_global import global_var


def getPasswordCrypt(password):
    myMd5 = hashlib.md5()
    myMd5.update(password.encode('utf-8'))
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest


def check_permission(user_roles):
    def decorator(function):
        @wraps(function)
        def wrap_function(*args, **auth):
            auth['permission'] = False
            try:
                verify_jwt_in_request()

            except Exception as e:
                return {'errorCode': 'BAUTH_TOKEN_MISSING', 'errorMessage': '请重新登录'}, 401
            current_user = get_jwt_identity()
            db = global_var['db']
            user = db.session.query(User).filter(User.name == current_user).first()
            if user:
                auth['logined'] = True
            else:
                return {'errorCode': 'BAUTH_TOKEN_MISSING', 'errorMessage': '请重新登录'}, 401

            if user.role_id in user_roles:
                auth['permission'] = True
                auth['role'] = user.role_id
                auth['userId'] = user.id
            else:
                return {'code': 'FAILURE', 'message': 'user has no privileges'}, 403
            return function(*args, **auth)

        return wrap_function

    return decorator

