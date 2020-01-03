#!/usr/bin/python
# encoding=utf8
import traceback
from sqlalchemy import or_
from datetime import datetime
from bb_logger.logger import Logger
from models.db_models import City
from common.utils.db import build_rows_result, update_record, build_one_result
from common.utils.http import getValueWithDefault


def getCityList(db, args):
    keyword = getValueWithDefault(args, 'keyword', None)
    page = getValueWithDefault(args, 'page', 1)
    pageSize = getValueWithDefault(args, 'pageSize', 1000)
    disabled = getValueWithDefault(args, 'disabled', None)

    try:
        query = db.session.query(
            City.id, City.city_code, City.name_en, City.name_zh, City.province_zh)
        if not keyword is None:
            query = query.filter(or_(City.name_zh==keyword,
                                     City.name_en==keyword,
                                     City.province_zh==keyword,
                                     City.province_en==keyword))
        offset = (page - 1) * pageSize
        total = query.count()
        rows = query.order_by(City.id).offset(offset).limit(pageSize).all()
        items = ['id', 'city_code', 'name_en', 'name_zh', 'province_zh']
        data = build_rows_result(rows, items)

        rst = {
            'code': 'SUCCESS',
            'data': {
                'total': total,
                'cities': data
            }
        }
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
        rst = {
            'code': 'FAILURE',
            'message': 'Get city list failed.'
        }
    return rst


def createCity(db, args):
    data = args['data']
    try:
        record = City(
            city_code=data['city_code'],
            name_en=data['name_en'],
            name_zh=data['name_zh'],
            province_zh=data['province_zh'],
            province_en=getValueWithDefault(data, 'province_en', ''),
            latitude=getValueWithDefault(data, 'latitude', ''),
            longitude=getValueWithDefault(data, 'longitude', ''),
            created_at=getValueWithDefault(data, 'created_at', datetime.now()),
            updated_at=getValueWithDefault(data, 'updated_at', datetime.now())
        )
        db.session.add(record)
        db.session.commit()

        rst = {
            'code': 'SUCCESS',
            'data': {
                'id': record.id,
            }
        }
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
        db.session.rollback()
        rst = {
            'code': 'FAILURE',
            'message': 'Failed'
        }
    return rst


def getCityOne(db, city_id):
    try:
        record = db.session.query(
            City.id, City.city_code, City.name_en, City.name_zh, City.province_zh) \
            .filter(City.id == city_id) \
            .first()
        if record is None:
            rst = {
                'code': 'FAILURE',
                'message': 'get city one failed, not exist'
            }
        else:
            items = ['id', 'city_code', 'name_en', 'name_zh', 'province_zh']
            data = build_one_result(record, items)
            rst = {
                'code': 'SUCCESS',
                'data': data
            }
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
        rst = {
            'code': 'FAILURE',
            'message': 'Failed'
        }
    return rst



def updateCity(db, args, city_id):
    data = args['data']
    try:
        record = db.session.query(City).filter(City.id == city_id).first()
        if record is None:
            rst = {
                'code': 'FAILURE',
                'message': 'update city one failed, not exist'
            }
        else:
            items = ['city_code', 'name_en', 'name_zh', 'province_en', 'province_zh', 'latitude', 'longitude']
            updated_at = data.get('updated_at', datetime.now())
            update_record(record, items, data)

            db.session.commit()

            rst = {
                'code': 'SUCCESS',
                'data': {
                    'id': city_id
                }
            }
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
        db.session.rollback()
        rst = {
            'code': 'FAILURE',
            'message': 'Failed'
        }
    return rst


def deleteCityOne(db, city_id):
    try:
        record = db.session.query(City).filter(City.id == city_id).first()
        if record is None:
            rst = {
                'code': 'FAILURE',
                'message': 'delete city one failed, not exist'
            }
        else:
            db.session.delete(record)
            db.session.commit()

            rst = {
                'code': 'SUCCESS',
                'data': {
                    'id': city_id,
                }
            }
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        Logger.service(err, 'error')
        db.session.rollback()
        rst = {
            'code': 'FAILURE',
            'message': 'Failed'
        }
    return rst

