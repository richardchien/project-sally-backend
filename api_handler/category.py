import json

from database import Session
from models import Category, Goods
from util import default_all, default_one


def all(limit):
    return default_all(Category, Category.id, limit)


def one(id):
    return default_one(Category, id)


def add(info):
    s = Session()

    try:
        # check if category with the same title exists
        q = s.query(Category).filter(Category.title == info.get('title'))
        if q.count() > 0:
            # exists
            cat = q.one()
            if cat.for_sale:
                # the existing category is for sale, meaning duplicated category
                raise Exception

            # update the info, and make the category for sale
            info['for_sale'] = True
            result = json.loads(update(q.one().id, info))
            result['id'] = cat.id
        else:
            # does not exist, then create a new one
            cat = Category(**info)
            s.add(cat)
            s.commit()
            result = {'ok': True, 'id': cat.id}
    except Exception:
        result = {'ok': False}

    s.close()
    return json.dumps(result)


def update(id, info):
    s = Session()

    try:
        # check if the category exists
        q = s.query(Category).filter(Category.id == id)
        if q.count() < 1:
            # does not exist
            raise Exception

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
        # check if category with the same title exists
        q = s.query(Category).filter(Category.id == id)
        if q.count() < 1:
            # does not exist
            raise Exception

        if not q.one().for_sale:
            # not for sale, meaning already deleted
            raise Exception

        # get all goods in this category
        goods = q.one().goods

        # make this category not for sale
        q.update({'for_sale': False})

        # make all goods in this category not for sale
        for g in goods:
            q = s.query(Goods).filter(Goods.id == g.id)
            q.update({'for_sale': False})

        s.commit()

        result = {'ok': True}
    except Exception:
        result = {'ok': False}

    s.close()
    return json.dumps(result)
