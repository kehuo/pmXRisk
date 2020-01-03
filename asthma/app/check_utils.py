# coding=utf-8
import signal
import functools
import time
from sqlalchemy import sql

TIMEOUT = 5


class TimeoutError(Exception):
    pass


def timeout(seconds, error_message="timeout"):
    def decorated(func):
        result = ""

        def _handle_timeout(signum, frame):
            global result
            result = error_message
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            global result
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)

            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
                return result
            return result

        return functools.wraps(func)(wrapper)

    return decorated


@timeout(TIMEOUT)
def db_check(db):
    info = ''
    try:
        result = db.session.query(City.id).first()
        if result is not None:
            rst = True
        else:
            rst = False
            info = 'db check failed!'
    except Exception as e:
        rst = False
        info = str(e)
    return rst, info

