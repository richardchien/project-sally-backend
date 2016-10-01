import api_handler as ah
import api_handler.category
import api_handler.goods
import api_handler.order

from flask import Flask, request

app = Flask(__name__)

api_ver = 'v1'


def api(location):
    return '/'.join(('', api_ver, location))


# Category

@app.route(api('category/all'), methods=['GET'])
def category_all():
    limit = request.args.get('limit')
    limit = int(limit) if limit else limit
    return ah.category.all(limit=limit)


@app.route(api('category/<int:cat_id>'), methods=['GET'])
def category_one(cat_id):
    return ah.category.one(id=cat_id)


@app.route(api('category/add'), methods=['POST'])
def category_add():
    return ah.category.add(info=request.json)


@app.route(api('category/<int:cat_id>/update'), methods=['POST'])
def category_update(cat_id):
    return ah.category.update(id=cat_id, info=request.json)


@app.route(api('category/<int:cat_id>/delete'), methods=['POST'])
def category_delete(cat_id):
    return ah.category.delete(id=cat_id)


# Goods


@app.route(api('goods/all'), methods=['GET'])
def goods_all():
    limit = request.args.get('limit')
    limit = int(limit) if limit else limit
    return ah.goods.all(limit=limit)


@app.route(api('goods/<int:goods_id>'), methods=['GET'])
def goods_one(goods_id):
    return ah.goods.one(id=goods_id)


@app.route(api('goods/add'), methods=['POST'])
def goods_add():
    return ah.goods.add(info=request.json)


@app.route(api('goods/<int:goods_id>/update'), methods=['POST'])
def goods_update(goods_id):
    return ah.goods.update(id=goods_id, info=request.json)


@app.route(api('goods/<int:goods_id>/delete'), methods=['POST'])
def goods_delete(goods_id):
    return ah.goods.delete(id=goods_id)


# Order


@app.route(api('order/all'), methods=['GET'])
def order_all():
    limit = request.args.get('limit')
    limit = int(limit) if limit else limit
    return ah.order.all(limit=limit)


@app.route(api('order/unhandled'), methods=['GET'])
def order_unhandled():
    limit = request.args.get('limit')
    limit = int(limit) if limit else limit
    return ah.order.unhandled(limit=limit)


@app.route(api('order/uncompleted'), methods=['GET'])
def order_uncompleted():
    limit = request.args.get('limit')
    limit = int(limit) if limit else limit
    return ah.order.uncompleted(limit=limit)


@app.route(api('order/completed'), methods=['GET'])
def order_completed():
    limit = request.args.get('limit')
    limit = int(limit) if limit else limit
    return ah.order.completed(limit=limit)


@app.route(api('order/closed'), methods=['GET'])
def order_closed():
    limit = request.args.get('limit')
    limit = int(limit) if limit else limit
    return ah.order.closed(limit=limit)


@app.route(api('order/<int:order_id>'), methods=['GET'])
def order_one(order_id):
    return ah.order.one(id=order_id)


@app.route(api('order/add'), methods=['POST'])
def order_add():
    return ah.order.add(info=request.json)


@app.route(api('order/<int:order_id>/update'), methods=['POST'])
def order_update(order_id):
    return ah.order.update(id=order_id, info=request.json)


@app.route(api('order/<int:order_id>/handle'), methods=['POST'])
def order_handle(order_id):
    return ah.order.handle(id=order_id)


@app.route(api('order/<int:order_id>/complete'), methods=['POST'])
def order_complete(order_id):
    return ah.order.complete(id=order_id)


@app.route(api('order/<int:order_id>/close'), methods=['POST'])
def order_close(order_id):
    return ah.order.close(id=order_id)


@app.route(api('order/<int:order_id>/delete'), methods=['POST'])
def order_delete(order_id):
    return ah.order.delete(id=order_id)


@app.route(api('order/<int:order_id>/rate'), methods=['POST'])
def order_rate(order_id):
    score = request.args.get('score')
    score = int(score) if score else score
    return ah.order.rate(id=order_id, score=score)


@app.route(api('order/sold-goods/<int:sold_goods_id>/rate'), methods=['POST'])
def order_rate_sold_goods(sold_goods_id):
    score = request.args.get('score')
    score = int(score) if score else score
    return ah.order.rate_sold_goods(id=sold_goods_id, score=score)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
