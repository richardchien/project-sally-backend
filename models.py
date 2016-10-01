from sqlalchemy import Column, String, DateTime, Integer, Float, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


def base_to_dict(self):
    d = dict(self.__dict__)
    keys_to_del = [k for k in d.keys() if k.startswith('_')]
    for k in keys_to_del:
        d.pop(k)
    return d


Base = declarative_base()
Base.to_dict = base_to_dict


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, unique=True, autoincrement=True, primary_key=True, nullable=False)
    title = Column(String(100), unique=True, nullable=False)
    for_sale = Column(Boolean, nullable=False, default=True)

    goods = relationship('Goods')

    def to_dict(self):
        d = super(Category, self).to_dict()
        d['goods'] = [x.to_dict() for x in self.goods]
        return d


class Goods(Base):
    __tablename__ = 'goods'

    id = Column(Integer, unique=True, autoincrement=True, primary_key=True, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    barcode = Column(String(14), unique=True)
    title = Column(String(100), unique=True, nullable=False)
    price = Column(Float, nullable=False, default=0.0)
    old_price = Column(Float, nullable=False, default=0.0)
    sold_count = Column(Integer, nullable=False, default=0)
    stock_count = Column(Integer, nullable=False, default=0)
    rate = Column(Float, nullable=False, default=0.0)
    rate_count = Column(Integer, nullable=False, default=0)
    add_dt = Column(DateTime, nullable=False, default=func.now())
    pic = Column(String(255))
    for_sale = Column(Boolean, nullable=False, default=True)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, unique=True, autoincrement=True, primary_key=True, nullable=False)
    receiver_name = Column(String(20), nullable=False)
    receiver_addr = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    total_price = Column(Float, nullable=False, default=0.0)
    rate = Column(Float, nullable=False, default=0.0)
    handled = Column(Boolean, nullable=False, default=False)
    completed = Column(Boolean, nullable=False, default=False)
    place_dt = Column(DateTime, nullable=False, default=func.now())
    handle_dt = Column(DateTime)
    complete_dt = Column(DateTime)
    closed = Column(Boolean, nullable=False, default=False)
    close_dt = Column(DateTime)

    sold_goods = relationship('SoldGoods')

    def to_dict(self):
        d = super(Order, self).to_dict()
        d['sold_goods'] = [x.to_dict() for x in self.sold_goods]
        return d


class SoldGoods(Base):
    __tablename__ = 'sold_goods'

    id = Column(Integer, unique=True, autoincrement=True, primary_key=True, nullable=False)
    goods_id = Column(Integer, ForeignKey('goods.id'), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    deal_price = Column(Float, nullable=False, default=0.0)
    rate = Column(Float, nullable=False, default=0.0)
    amount = Column(Integer, nullable=False, default=1)
