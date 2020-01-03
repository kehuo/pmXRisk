import os
import traceback
from flask import Flask
import pymysql
from datetime import datetime
from time import sleep
from bg_service.weather_func import collect_weather_one
from bg_service.pm_func import collect_pm_one
from data.city_data import cities

bg_app = Flask(__name__)
config_file = os.environ.get('CFG_PATH', '../service.conf')
bg_app.config.from_pyfile(config_file, silent=True)
from app.init_global import global_var

global_var["WEATHER_SLEEP_SEC"] = bg_app.config["WEATHER_SLEEP_SEC"]
global_var["PM_SLEEP_SEC"] = bg_app.config["PM_SLEEP_SEC"]
pymysql_config = {'host': bg_app.config['DB_HOST'],
                  "port": bg_app.config['DB_PORT'],
                  "user": bg_app.config['DB_USER'],
                  "password": bg_app.config['DB_PASSWORD'],
                  'db': bg_app.config['DB_NAME'],
                  'charset': bg_app.config['PYMYSQL_CHARSET']}

func_map = {
    "weather": collect_weather_one,
    "pm": collect_pm_one
}


def collect_all(global_var, conn, cursor, collect_type):
    """
    collect_type: weather 或者 pm
    """
    failed_list = []

    print('\n %s------------开始收集%s--------------' % (collect_type, str(datetime.now())))
    for i in cities:
        is_success, errors = func_map[collect_type](i['city_code'], conn, cursor)
        if not is_success:
            failed_list.append(errors)

        sleep(global_var["%s_SLEEP_SEC" % collect_type.upper()])
    print('\n %s------------收集%s结束--------------' % (collect_type, str(datetime.now())))

    return failed_list


def main():
    conn = pymysql.connect(**pymysql_config)
    cursor = conn.cursor()
    try:
        weather_failed_list = collect_all(global_var, conn, cursor, collect_type="weather")
        pm_failed_list = collect_all(global_var, conn, cursor, collect_type="pm")

        if len(weather_failed_list) > 0:
            sql1 = "INSERT INTO notification (level_id, level_name, notification, notification_date) \
                   VALUES (%s, %s, %s, %s)"
            cursor.execute(sql1, (1, 'warning', str(weather_failed_list), datetime.now()))
            conn.commit()
        if len(pm_failed_list) > 0:
            sql2 = "INSERT INTO notification (level_id, level_name, notification, notification_date) \
                               VALUES (%s, %s, %s, %s)"
            cursor.execute(sql2, (1, 'warning', str(pm_failed_list), datetime.now()))
            conn.commit()
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        sql3 = "INSERT INTO notification (level_id, level_name, notification, notification_date) \
                               VALUES (%s, %s, %s, %s)"
        cursor.execute(sql3, (2, 'error', err, datetime.now()))
        conn.commit()

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
