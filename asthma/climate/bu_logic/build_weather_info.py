import traceback
from common.utils.http import has_error
from climate.bu_logic.utils import search_weather_by_cityname, search_pm_by_cityname
from bb_logger.logger import Logger


def build_weather_info(global_var, args):
	res = {}
	try:
		weather_res = search_weather_by_cityname(global_var, args)
		if has_error(weather_res):
			return {"code": "FAILURE", "message": "Failed to search weather by city name"}

		pm_res = search_pm_by_cityname(global_var, args)
		if has_error(pm_res):
			return {"code": "FAILURE", "message": "Failed to search pm by city name"}

		tmp_dict = {args['cityName']: {"weather": weather_res, "pm": pm_res}}
		res['code'] = "SUCCESS"
		res['data'] = tmp_dict

	except Exception as e:
		traceback.print_exc()
		err = traceback.format_exc()
		Logger.service(err, 'error')
		res = {'code': 'FAILURE', 'message': 'build weather info Failed'}
	return res
