#!/usr/bin/python
# encoding=utf8

from datetime import datetime
from sqlalchemy import Column, String, Integer, Text, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, autoincrement=True, primary_key=True)
    city_code = Column(Integer, nullable=False, comment='聚合API城市code')
    name_en = Column(String(64), nullable=False, comment='城市拼音名')
    name_zh = Column(String(64), nullable=False, comment='城市中文名')
    province_en = Column(String(64), nullable=False, comment='城市所在省拼音名')
    province_zh = Column(String(64), nullable=False, comment='城市所在省中文名')
    latitude = Column(String(64), nullable=False, comment='城市所在纬度')
    longitude = Column(String(64), nullable=False, comment='城市所在经度')
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)


class Weather(Base):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True)
    city_code = Column(String(64))
    weather_date = Column(String(64), nullable=False, comment='这一天的天气')
    week = Column(String(64), nullable=False, comment='星期几')
    temperature_average = Column(String(64), nullable=False, comment='当天平均气温')
    temperature_lowest = Column(String(64), nullable=True, comment='最低气温')
    temperature_highest = Column(String(64), nullable=True, comment='最高气温')
    wind_power = Column(String(64), nullable=True, comment='风力等级')
    wind_speed = Column(String(64), nullable=False, comment='风速')
    humidity = Column(Integer, nullable=False, comment='湿度')
    weather_condition = Column(String(64), nullable=False, comment='阴晴, 小雨等天气信息weather info')
    ultraviolet = Column(String(64), nullable=False, comment='紫外线强度')
    ultraviolet_description = Column(String(128), nullable=False, comment='紫外线的建议和描述')
    blood_sugar = Column(String(64), nullable=False, comment='血糖指数')
    blood_sugar_description = Column(String(64), nullable=False, comment='血糖指数的建议和描述')
    dress = Column(String(64), nullable=False, comment='穿衣指数')
    dress_description = Column(String(64), nullable=False, comment='穿衣指数的建议和描述')
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
	

class PM(Base):
    __tablename__ = 'pm'
    id = Column(Integer, autoincrement=True, primary_key=True)
    city_code = Column(Integer, nullable=False, comment='聚合API城市code')
    pm_date = Column(String(64), nullable=False, comment='这一天的PM值')
    pm_25 = Column(Float, nullable=False)
    pm_10 = Column(Float, nullable=False, default='')
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    role_id = Column(Integer, nullable=False, default=0, comment='0普通,1管理员')
    name = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    fullname = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False)
    disabled = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    created_by = Column(Integer, nullable=False, default=0)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    updated_by = Column(Integer, nullable=False, default=0)



class RiskComment(Base):
    __tablename__ = 'risk_comment'
    id = Column(Integer, autoincrement=True, primary_key=True)
    level = Column(Integer, nullable=False, comment='风险概率对应的等级,默认每百分之二十为一级')
    threshold = Column(Float(6), nullable=False, comment='风险概率阈值')
    comment = Column(String(256), nullable=False, default='测试评论', comment='等级对应的评论')
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)


class Notification(Base):
    __tablename__ = 'notification'
    id = Column(Integer, autoincrement=True, primary_key=True)
    level_id = Column(Integer, nullable=False, comment='信息的严重等级id,分为012')
    level_name = Column(String(64), nullable=False, comment='信息的严重等级,success,warning,error')
    notification = Column(String(512), nullable=False, comment='报错信息')
    notification_date = Column(DateTime, nullable=False, default=datetime.now, comment='报错时间')
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

        
