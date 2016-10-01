import json

from datetime import datetime
from database import Session


def json_serial(obj):
    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError("Type not serializable")


def default_all(column, order_by, limit):
    s = Session()

    rows = s.query(column).order_by(order_by).limit(limit).all()

    result = []
    for row in rows:
        result.append(row.to_dict())

    s.close()
    return json.dumps(result, default=json_serial)


def default_one(column, id):
    s = Session()

    q = s.query(column).filter(column.id == id)
    if q.count() < 1:
        result = None
    else:
        result = q.one().to_dict()

    s.close()
    return json.dumps(result, default=json_serial)
