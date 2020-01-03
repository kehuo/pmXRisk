#!/usr/bin/python
# encoding=utf8

from flask_sqlalchemy import SQLAlchemy


def init_db(app, global_var):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s:%s/%s' % (app.config['DB_USER'],
                                                                        app.config['DB_PASSWORD'],
                                                                        app.config['DB_HOST'],
                                                                        app.config['DB_PORT'],
                                                                        app.config['DB_NAME'])
    try:
        cnx = SQLAlchemy(app)
        global_var['db'] = cnx
    except Exception as e:
        return False, str(e)
    return True, ''
