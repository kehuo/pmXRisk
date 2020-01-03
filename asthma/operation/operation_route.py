#!/usr/bin/python
# encoding=utf8

from operation.admin.service_auth import LogIn
from operation.admin.service_user import Users, UserOne, CurrentUser
from operation.admin.service_risk_comment import RiskComments, RiskCommentOne
from operation.admin.service_weather import WeatherInfos
from operation.admin.service_pm import PMInfos
from operation.admin.service_city import Cities, CityOne
from operation.admin.service_notification import Notifications
from common.utils.http import app_url


def operation_route(api, version, model):
    # 管理员登陆
    # access token 过期时间 6000s
    api.add_resource(LogIn, app_url(version, model, '/login'))

    # 获取所有用户列表, 创建用户
    api.add_resource(Users, app_url(version, model, '/user'))

    # 获取单个用户, 更新用户，删除用户
    api.add_resource(UserOne, app_url(version, model, '/user/<int:user_id>'))

    # 获取当前用户
    api.add_resource(CurrentUser, app_url(version, model, '/currentUser'))

    # 以下是comment的api
    # 获取risk_comment 风险评价表的所有数据
    api.add_resource(RiskComments, app_url(version, model, '/risk_comment'))

    # 获取 risk_comment 单个评价， 更新， 删除
    api.add_resource(RiskCommentOne, app_url(version, model, '/risk_comment/<int:risk_comment_id>'))

    # 获取weather表中某一个城市, 某个时间段的weather数据
    api.add_resource(WeatherInfos, app_url(version, model, '/weather'))

    # 获取weather表中某一个城市, 某个时间段的 pm 数据
    api.add_resource(PMInfos, app_url(version, model, '/pm'))

    # 获取 city 表中所有城市信息
    # POST 可以增加新城市
    # keyword 过滤
    api.add_resource(Cities, app_url(version, model, '/city'))

    # 获取 city 表中某一个城市的信息
    # 更新城市信息 PUT
    # 删除城市 DELETE
    api.add_resource(CityOne, app_url(version, model, '/city/<int:city_id>'))

    # 获取 error_notification 表中的所有信息
    api.add_resource(Notifications, app_url(version, model, '/notification'))


    return
