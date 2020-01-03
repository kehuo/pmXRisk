# 该 serve.py 文件定义所有需要的资源 Resources
# 每个资源需要的逻辑函数都定义在 climate 文件夹下的 bu_logic.py 中

from flask_restful import reqparse, Api, Resource, request
from app.init_global import global_var
from common.utils.http import encoding_resp_utf8

from climate.bu_logic.get_city_list import get_city_list
from climate.bu_logic.build_weather_info import build_weather_info
from climate.bu_logic.cal_asthma_risk import cal_asthma_risk


class City(Resource):
    # get 所有城市列表
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('provinceZh', type=str, required=False, location='args')
        args = parser.parse_args()

        res = get_city_list(global_var)

        return encoding_resp_utf8(res)


class WeatherInfo(Resource):
    def get(self):
        # 解析请求
        parser = reqparse.RequestParser()
        # 城市中文名
        parser.add_argument('cityName', type=str, required=True, location='args')
        args = parser.parse_args()

        res = build_weather_info(global_var, args)

        return encoding_resp_utf8(res)


# http://html.rhhz.net/yyqxxb/html/20050343.htm
# 计算哮喘风险概率 y = p/(1-p)
class AsthmaRisk(Resource):
    def get(self):
        # 默认2周模型
        parser = reqparse.RequestParser()
        parser.add_argument('cityName', type=str, required=True, location='args')
        parser.add_argument('isFever', type=int, required=False, default=0, location='args')
        parser.add_argument('week', type=int, required=False, default=2, location='args')
        args = parser.parse_args()

        res = cal_asthma_risk(global_var, args)

        return encoding_resp_utf8(res)
