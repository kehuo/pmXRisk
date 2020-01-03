from flask_restful import reqparse, abort, Api, Resource
from app.system import Info, Ping, HealthChecks
from common.utils.http import app_url
from app.init_global import global_var
from model_route_config import route_init_func

# 2019-08-09
# models = ['climate','operation']
models = global_var['models']


def global_route(api, version, model):
    api.add_resource(Info, app_url(version, model, '/'))
    api.add_resource(Ping, app_url(version, model, '/ping'))
    api.add_resource(HealthChecks, app_url(version, model, '/healthchecks'))


model_func_map = [
    ['system', global_route]
]


def init_route(api, api_version):
    for model in models:
        func = route_init_func.get(model, None)
        if func is None:
            print('failed to get model function')
            continue
        model_func_map.append([model, func])

    # init model route
    for func in model_func_map:
        func[1](api, api_version, func[0])
    return
