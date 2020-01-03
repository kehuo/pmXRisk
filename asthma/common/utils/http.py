from flask import json, Response
from flask_restful import abort
import base64
import json


def encoding_resp_utf8(data):
    json_response = json.dumps(data, ensure_ascii=False)
    response = Response(json_response, content_type="application/json; charset=utf-8")
    return response


def format_base64_str(source):
    mod_length = len(source) % 4
    for i in range(0, 4 - mod_length, 1):
        source += '='
    result = base64.b64decode(source)
    return result


def has_error(rst):
    if type(rst) is dict and ('errMsg' in rst or 'error_msg' in rst or 'message' in rst):
        return True
    return False


def process_exception(code, message):
    return abort(code, message=message)


def build_error_response(err_code, err_msg):
    rst = {
        "code": err_code,
        "message": err_msg
    }
    return process_exception(err_code, rst)


def build_failed_response(msg):
    rst = {
        "code": msg['code'],
        "message": msg['errMsg'],
        "error": msg.get('errInfo', '')
    }
    return encoding_resp_utf8(rst)


def app_url(version, model, name):
    name = '/{}/{}{}'.format(version, model, name)
    return name


def getValueWithDefault(aMap, key, defaultVal=None):
    v = aMap.get(key, defaultVal)
    if v is None:
        v = defaultVal
    return v


def build_error_msg(msg):
    description = error_dict.get(msg['errMsg'], None)
    if description is not None:
        msg['errMsg'] = '{}: {}'.format(msg['errMsg'], description)

    rst = {
        "code": msg['code'],
        "message": msg['errMsg'],
        "error": msg.get('errInfo', '')
    }

    return encoding_resp_utf8(rst)
