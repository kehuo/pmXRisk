#!/usr/bin/python
# encoding=utf8

# 从 serve.py 引入所需 db Model
from climate.serve import City, WeatherInfo, AsthmaRisk
from common.utils.http import app_url


def climate_route(api, version, model):
    # 城市列表
    api.add_resource(City, app_url(version, model, '/city'))

    # 城市的天气信息和PM指数
    api.add_resource(WeatherInfo, app_url(version, model, '/weather_info'))

    # 计算哮喘风险指数y与概率p
    api.add_resource(AsthmaRisk, app_url(version, model, '/risk'))

    return
