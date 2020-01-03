import traceback
import time
from flask_restful import reqparse, abort, Api, Resource
from app.check_utils import db_check
from app.init_global import global_var


class Info(Resource):
    def get(self):
        rst = {
            'name': global_var['description'],
            'version':  global_var['version']
        }
        return rst


class Ping(Resource):
    def get(self):
        return {'response': 'ok'}


check_func_map = [[db_check, global_var['db'],  'database', global_var['db_host']]]


class HealthChecks(Resource):
    def get(self):
        rst = {
            'result': 'ok',
            'name': global_var['service'],
            'errorMsg': '',
            'version': global_var['version'],
            "dependencies": []
        }

        for func in check_func_map:
            status, message = func[0](func[1])
            dependence = {
                "name": func[2],
                "host": func[3],
                "type": "internal",
                "result": 'ok' if status else 'critical',
                "message": message
            }
            rst['dependencies'].append(dependence)
            if status is not True:
                rst['result'] = 'critical'
                rst['errorMsg'] += '[{}]: {};'.format(func[2], message)

        return rst

