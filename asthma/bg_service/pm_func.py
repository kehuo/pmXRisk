from datetime import datetime
from requests import get


# v3 (当前使用)
def collect_pm_one(name_en, conn, cursor):
    """
    is_success: 标志位，如果抓取成功，最后返回 True，否则False
    """
    url = "https://api.waqi.info/feed/%s/?token=847e2ccb134222844bca49eaa9094ce5b18c9bf3" % name_en

    is_success = True
    errors = {"city": name_en,
              "errors": []}

    try:
        res = get(url, timeout=2.4).json()
    except Exception as e:
        is_success = False
        n1 = "%s调用API失败,连接超时" % (name_en)
        errors["errors"].append(n1)
        return is_success, errors

    # 如果请求成功，则抓取所需数据
    try:
        pm_25 = res['data']['iaqi']['pm25']['v']
        pm_10 = res['data']['iaqi']['pm10']['v']
        pm_date = res['data']['time']['s']
    except Exception as e:
        is_success = False
        n2 = "%s获取pm数据失败,完整响应:\n%s" % (name_en, str(res))
        errors["errors"].append(n2)
        return is_success, errors

    # 以上所有数据已经抓取完成，以下为写入数据库部分
    # 根据 pm_date 搜索 pm 表
    # 如果没有，那么新增一条记录 Insert;
    # 如果有，那么更新该条记录 Update.
    try:
        sql_select = "SELECT city_code FROM city where name_en='%s'" % name_en
        cursor.execute(sql_select)
        city_code = cursor.fetchone()[0]
        sql_search = "SELECT * from pm where pm_date='%s' and city_code='%s'" % (pm_date, city_code)
        if cursor.execute(sql_search) == 0:
            # 之前没有, 新增
            sql_insert = "INSERT INTO pm (city_code,\
                                            pm_date,\
                                            pm_25,\
                                            pm_10,\
                                            created_at,\
                                            updated_at)\
                        VALUES ('%s', '%s', '%s', '%s', '%s' ,'%s')" % (city_code,
                                                                        pm_date,
                                                                        pm_25,
                                                                        pm_10,
                                                                        datetime.now(),
                                                                        datetime.now())

            cursor.execute(sql_insert)
            conn.commit()
        else:
            # 已有,覆盖更新
            sql_update = "UPDATE pm SET pm_25='%s', pm_10='%s', updated_at='%s'\
                                    where pm_date='%s' and city_code='%s'" % (pm_25,
                                                                              pm_10,
                                                                              datetime.now(),
                                                                              pm_date,
                                                                              city_code)
            cursor.execute(sql_update)
            conn.commit()
    except Exception as e:
        is_success = False
        n3 = '%s写入数据库失败' % name_en
        errors["errors"].append(n3)
        return is_success, errors
    return is_success, errors
