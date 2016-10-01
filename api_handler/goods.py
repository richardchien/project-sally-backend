import json

from sqlalchemy import desc
from database import Session
from models import Goods
from util import default_all, default_one


def all(limit):
    return default_all(Goods, desc(Goods.add_dt), limit)


def one(id):
    return default_one(Goods, id)


def add(info):
    s = Session()

    try:
        # check if goods with the same title exist
        q = s.query(Goods).filter(Goods.title == info.get('title'))
        if q.count() > 0:
            # exist
            goods = q.one()
            if goods.for_sale:
                # the existing one is for sale, meaning duplicated goods
                raise Exception

            # update the info, and make the goods for sale
            info['for_sale'] = True
            result = json.loads(update(q.one().id, info))
            result['id'] = goods.id
        else:
            # does not exist, then create a new one
            goods = Goods(**info)
            s.add(goods)
            s.commit()
            result = {'ok': True, 'id': goods.id}
    except Exception:
        result = {'ok': False}

    s.close()
    return json.dumps(result)


def update(id, info):
    s = Session()

    try:
        # check if goods exist
        q = s.query(Goods).filter(Goods.id == id)
        if q.count() < 1:
            # not exist
            raise Exception

        if 'price' in info:
            # changing price, should record the old price
            info['old_price'] = q.one().price

        # update it
        q.update(info)
        s.commit()

        result = {'ok': True}
    except Exception:
        result = {'ok': False}

    s.close()
    return json.dumps(result)


def delete(id):
    s = Session()

    try:
        # check if goods with the same title exist
        q = s.query(Goods).filter(Goods.id == id)
        if q.count() < 1:
            # not exist
            raise Exception

        if not q.one().for_sale:
            # not for sale, meaning already deleted
            raise Exception

        # make this category not for sale
        q.update({'for_sale': False})
        s.commit()

        result = {'ok': True}
    except Exception:
        result = {'ok': False}

    s.close()
    return json.dumps(result)
