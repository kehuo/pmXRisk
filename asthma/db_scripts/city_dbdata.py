# 283个城市
from datetime import datetime
from flask import Flask
import os
import pymysql
import sys
sys.path.append("..")
from data.city_data import cities


db_app = Flask(__name__)
env_dist = os.environ
config_file = env_dist.get('CFG_PATH', '../service.conf')
db_app.config.from_pyfile(config_file, silent=True)
pymysql_config = {'host': db_app.config['PYMYSQL_HOST'],
                  "port": db_app.config['PYMYSQL_PORT'],
                  "user": db_app.config['PYMYSQL_USER'],
                  "password": db_app.config['PYMYSQL_PASSWORD'],
                  'db': db_app.config['PYMYSQL_DBNAME'],
                  'charset': db_app.config['PYMYSQL_CHARSET']}

def insert_city_db(cities, pymysql_config):
	# 创建 mysql 连接
	connection = pymysql.connect(**pymysql_config)
	cursor = connection.cursor()

	# 将每个城市存入 表中
	for i in cities:
		sql = "INSERT INTO city (city_code,\
									name_en,\
									name_zh,\
									province_en,\
									province_zh,\
									latitude,\
									longitude,\
									created_at,\
									updated_at)\
				VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
						(i['city_code'],
							i['name_en'],
							i['name_zh'],
							i['province_en'],
							i['province_zh'],
							i['latitude'],
							i['longitude'],
							datetime.now(),
							datetime.now())

		cursor.execute(sql)
		connection.commit()
	cursor.close()
	connection.close()


if __name__ == "__main__":
	print('该脚本用来向%s的 City 表插入城市记录' % db_app.config['PYMYSQL_HOST'])
	insert_city_db(cities=cities, pymysql_config=pymysql_config)
	print('写入成功')



