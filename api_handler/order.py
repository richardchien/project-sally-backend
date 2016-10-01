import json

from functools import reduce
from datetime import datetime
from sqlalchemy import desc
from database import Session
from models import Order, SoldGoods, Goods
from util import json_serial, default_one


def fetch_all_by(limit, **filter_by):
    s = Session()

    rows = s.query(Order) \
        .filter_by(**filter_by) \
        .order_by(desc(Order.place_dt)) \
        .limit(limit) \
        .all()

    result = []
    for row in rows:
        result.append(row.to_dict())

    s.close()
    return json.dumps(result, default=json_serial)


def all(limit):
    return fetch_all_by(limit)


def unhandled(limit):
    return fetch_all_by(limit, handled=False, closed=False)


def uncompleted(limit):
    return fetch_all_by(limit, completed=False, closed=False)


def completed(limit):
    return fetch_all_by(limit, completed=True)


def closed(limit):
    return fetch_all_by(limit, closed=True)


def one(id):
    return default_one(Order, id)


def add(info):
    s = Session()

    try:
        if 'sold_goods' not in info:
            # info does not contain sold_goods
            raise Exception

        sold_goods = []
        for sg_info in info['sold_goods']:
            # create new sold goods object
            sg = SoldGoods(**sg_info)

            # query the corresponding goods
            q_goods = s.query(Goods).filter(Goods.id == sg.goods_id)
            if q_goods.count() < 1:
                raise Exception

            g = q_goods.one()
            if not g.for_sale:
                # goods is not for sale
                raise Exception

            q_goods.update({'stock_count': g.stock_count - sg.amount})
            sg.deal_price = g.price

            sold_goods.append(sg)

        # replace info['sold_goods'] with newly generated SoldGoods object list
        info['sold_goods'] = sold_goods

        # create new order
        order = Order(**info)

        # calculate total price
        if len(sold_goods) > 1:
            order.total_price = reduce(lambda x, y: x.deal_price * x.amount + y.deal_price * y.amount,
                                       sold_goods)
        else:
            order.total_price = sold_goods[0].deal_price * sold_goods[0].amount

        s.add(order)
        s.add_all(sold_goods)
        s.commit()

        result = {'ok': True, 'id': order.id}
    except Exception:
        result = {'ok': False}

    s.close()
    return json.dumps(result)


def update(id, info):
    s = Session()

    try:
        if 'sold_goods' in info:
            # drop sold_goods property
            # sold_goods cannot be changed after add an order
            raise Exception

        # check if the order exists
        q = s.query(Order).filter(Order.id == id)
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


def handle(id):
    s = Session()

    try:
        # check if the order exists
        q = s.query(Order).filter(Order.id == id)
        if q.count() < 1:
            # does not exist
            raise Exception

        order = q.one()

        if order.handled:
            # already handled
            raise Exception

        if order.closed:
            # already closed
            raise Exception

        info = {'handled': True,
                'handle_dt': datetime.now()}
        result = json.loads(update(id, info))
    except Exception:
        result = {'ok': False}

    s.close()
    return json.dumps(result)


def complete(id):
    s = Session()

    try:
        # check if the order exists
        q = s.query(Order).filter(Order.id == id)
        if q.count() < 1:
            # does not exist
            raise Exception

        order = q.one()

        if not order.handled:
            # haven't handled yet
            raise Exception

        if order.completed:
            # already completed
            raise Exception

        if order.closed:
            # already closed
            raise Exception

        info = {'completed': True,
                'complete_dt': datetime.now()}
        result = json.loads(update(id, info))

        if not result['ok']:
            # update failed
            raise Exception

        # increase sold_count of goods
        sold_goods = order.sold_goods
        for sg in sold_goods:
            q_goods = s.query(Goods).filter(Goods.id == sg.goods_id)
            g = q_goods.one()
            q_goods.update({'sold_count': g.sold_count + sg.amount})

        s.commit()

        result = {'ok': True}
    except Exception:
        result = {'ok': False}

    s.close()
    return json.dumps(result)


def close(id):
    s = Session()

    try:
        # check if the order exists
        q = s.query(Order).filter(Order.id == id)
        if q.count() < 1:
            # does not exist
            raise Exception

        order = q.one()

        if order.completed:
            # already completed
            raise Exception

        if order.closed:
            # already closed
            raise Exception

        info = {'closed': True,
                'close_dt': datetime.now()}
        result = json.loads(update(id, info))

        if not result['ok']:
            # update failed
            raise Exception

        # restore stock_count of goods
        sold_goods = order.sold_goods
        for sg in sold_goods:
            q_goods = s.query(Goods).filter(Goods.id == sg.goods_id)
            g = q_goods.one()
            q_goods.update({'stock_count': g.stock_count + sg.amount})

        s.commit()

        result = {'ok': True}
    except Exception:
        result = {'ok': False}

    s.close()
    return json.dumps(result)


def delete(id):
    return None


def rate(id, score):
    return None


def rate_sold_goods(id, score):
    return None
