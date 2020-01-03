import datetime

def buildTimeCondition(TableClass, start, end, tag='updated_at'):
    filters = []
    date_format = '%Y-%m-%d'
    if not start is None:
        startTs = datetime.datetime.strptime(start, date_format)
        filters.append(getattr(TableClass, tag) >= startTs)

    if not end is None:
        endTs = datetime.datetime.strptime(end, date_format)
        endTs = endTs + datetime.timedelta(days=1)
        filters.append(getattr(TableClass, tag) <= endTs)
    return filters



def nowRelative(x, unit='days'):
    now = datetime.datetime.now()
    now = now - datetime.timedelta(days=x+1)
    return now
