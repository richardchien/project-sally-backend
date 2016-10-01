## API v1

```
BASE_URL = "/v1"
```

### 商品类别

- `GET /category/all[?limit=]`, 获取所有商品分类

输出:

```json
[
    {
        "id": 1,
        "title": "休闲零食",
        "for_sale": true,
        "goods": [
            {
                "id": 1,
                "title": "方便面111g",
                "category_id": 1,
                "barcode": "",
                "price": 3.5,
                "old_price": 0.0,
                "sold_count": 23,
                "stock_count": 43,
                "rate": 3.9,
                "rate_count": 17,
                "add_dt": "2016-03-18 12:22:56",
                "pic": "http://img.r-c.im/12345.jpg",
                "for_sale": true
            },
            {
                "id": 2,
                "title": "火腿肠20g",
                "category_id": 1,
                "barcode": "9787040396618",
                "price": 2.0,
                "old_price": 2.3,
                "sold_count": 12,
                "stock_count": 30,
                "rate": 4.2,
                "rate_count": 8,
                "add_dt": "2016-03-18 12:30:22",
                "pic": "",
                "for_sale": true
            }
        ]
    },
    {
        "id": 2,
        "title": "糖果饼干",
        "for_sale": true,
        "goods": []
    }
]
```

- `GET /category/<int:cat_id>`, 获取特定 id 的类别信息

输出:

```json
{
    "id": 1,
    "title": "休闲零食",
    "for_sale": false,
    "goods": [
        {
            "id": 1,
            "title": "方便面111g",
            "category_id": 1,
            "barcode": "",
            "price": 3.5,
            "old_price": 0.0,
            "sold_count": 23,
            "stock_count": 43,
            "rate": 3.9,
            "rate_count": 17,
            "add_dt": "2016-03-18 12:22:56",
            "pic": "http://img.r-c.im/12345.jpg",
            "for_sale": true
        },
        {
            "id": 2,
            "title": "火腿肠20g",
            "category_id": 1,
            "barcode": "9787040396618",
            "price": 2.0,
            "old_price": 2.3,
            "sold_count": 12,
            "stock_count": 30,
            "rate": 4.2,
            "rate_count": 8,
            "add_dt": "2016-03-18 12:30:22",
            "pic": "",
            "for_sale": true
        }
    ]
}
```

- `POST /category/add`, 添加商品类别

输入:

```json
{
    "title": "饮料牛奶"
}
```

输出:

```json
{
    "ok": true,
    "id": 4
}
```

- `POST /category/<int:cat_id>/update`, 更新类别信息

输入:

```json
{
    "title": "饮料牛奶"
}
```

输出:

```json
{
    "ok": true
}
```

- `POST /category/<int:cat_id>/delete`, 删除商品类别(下架)

输出:

```json
{
    "ok": true
}
```

### 商品

- `GET /goods/all[?limit=]`, 获取所有商品信息

输出:

```json
[
    {
        "id": 1,
        "title": "方便面111g",
        "category_id": 1,
        "barcode": "",
        "price": 3.5,
        "old_price": 0.0,
        "sold_count": 23,
        "stock_count": 43,
        "rate": 3.9,
        "rate_count": 17,
        "add_dt": "2016-03-18 12:22:56",
        "pic": "http://img.r-c.im/12345.jpg",
        "for_sale": true
    },
    {
        "id": 2,
        "title": "火腿肠20g",
        "category_id": 3,
        "barcode": "9787040396618",
        "price": 2.0,
        "old_price": 2.3,
        "sold_count": 12,
        "stock_count": 30,
        "rate": 4.2,
        "rate_count": 8,
        "add_dt": "2016-03-18 12:30:22",
        "pic": "",
        "for_sale": true
    }
]
```

- `GET /goods/<int:goods_id>`, 获取特定 id 的商品信息

输出:

```json
{
    "id": 2,
    "title": "火腿肠20g",
    "category_id": 3,
    "barcode": "",
    "price": 2.0,
    "old_price": 2.3,
    "sold_count": 12,
    "stock_count": 30,
    "rate": 4.2,
    "rate_count": 8,
    "add_dt": "2016-03-18 12:30:22",
    "pic": "http://img.r-c.im/12347.jpg",
    "for_sale": true
}
```

- `POST /goods/add`, 添加商品

输入:

```json
{
    "title": "火腿肠20g",
    "category_id": 3,
    "barcode": "9787040396614",
    "price": 2.0,
    "stock_count": 30,
    "pic": "http://img.r-c.im/12347.jpg"
}
```

输出:

```json
{
    "ok": true,
    "id": 13
}
```

- `POST /goods/<int:goods_id>/update`, 更新商品

输入:

```json
{
    "title": "火腿肠20g",
    "category_id": 3,
    "barcode": "9787040396614",
    "price": 2.0,
    "stock_count": 30,
    "pic": "http://img.r-c.im/12347.jpg"
}
```

输出:

```json
{
    "ok": true
}
```

- `POST /goods/<int:goods_id>/delete`, 删除商品(下架)

输出:

```json
{
    "ok": true
}
```

### 订单

- `GET /order/all[?limit=]`, 获取所有订单信息

输出:

```json
[
    {
        "id": 1,
        "receiver_name": "钱宇超",
        "receiver_addr": "9-561",
        "phone": "17766232816",
        "sold_goods": [
            {
                "id": 1,
                "goods_id": 3,
                "order_id": 1,
                "deal_price": 2.0,
                "amount": 2,
                "rate": 5.0
            },
            {
                "id": 2,
                "goods_id": 10,
                "order_id": 1,
                "deal_price": 3.8,
                "amount": 1,
                "rate": 4.0
            }
        ],
        "total_price": 7.8,
        "rate": 4.0,
        "handled": true,
        "completed": true,
        "closed": false,
        "place_dt": "2016-03-18 12:22:56",
        "handle_dt": "2016-03-18 12:23:03",
        "complete_dt": "2016-03-18 12:34:13",
        "close_dt": ""
    },
    {
        "id": 2,
        "receiver_name": "宋夏子杰",
        "receiver_addr": "9-561",
        "phone": "17766232876",
        "sold_goods": [
            {
                "id": 3,
                "goods_id": 6,
                "order_id": 2,
                "deal_price": 1.5,
                "amount": 4,
                "rate": 0.0
            }
        ],
        "total_price": 6.0,
        "rate": 0.0,
        "handled": true,
        "completed": false,
        "closed": false,
        "place_dt": "2016-03-18 17:21:56",
        "handle_dt": "2016-03-18 17:23:03",
        "complete_dt": "",
        "close_dt": ""
    }
]
```

- `GET /order/unhandled[?limit=]`, 获取所有未处理订单信息

输出:

```json
[
    {
        "id": 1,
        "receiver_name": "钱宇超",
        "receiver_addr": "9-561",
        "phone": "17766232816",
        "sold_goods": [
            {
                "id": 1,
                "goods_id": 3,
                "order_id": 1,
                "deal_price": 2.0,
                "amount": 2,
                "rate": 5.0
            },
            {
                "id": 2,
                "goods_id": 10,
                "order_id": 1,
                "deal_price": 3.8,
                "amount": 1,
                "rate": 4.0
            }
        ],
        "total_price": 7.8,
        "rate": 0.0,
        "handled": false,
        "completed": false,
        "closed": false,
        "place_dt": "2016-03-18 12:22:56",
        "handle_dt": "",
        "complete_dt": "",
        "close_dt": ""
    }
]
```

- `GET /order/uncompleted[?limit=]`, 获取所有未完成(已处理)订单信息

输出:

```json
[
    {
        "id": 1,
        "receiver_name": "钱宇超",
        "receiver_addr": "9-561",
        "phone": "17766232816",
        "sold_goods": [
            {
                "id": 1,
                "goods_id": 3,
                "order_id": 1,
                "deal_price": 2.0,
                "amount": 2,
                "rate": 5.0
            },
            {
                "id": 2,
                "goods_id": 10,
                "order_id": 1,
                "deal_price": 3.8,
                "amount": 1,
                "rate": 4.0
            }
        ],
        "total_price": 7.8,
        "rate": 0.0,
        "handled": true,
        "completed": false,
        "closed": false,
        "place_dt": "2016-03-18 12:22:56",
        "handle_dt": "2016-03-18 17:23:03",
        "complete_dt": "",
        "close_dt": ""
    }
]
```

- `GET /order/completed[?limit=]`, 获取所有已完成订单信息

输出:

```json
[
    {
        "id": 1,
        "receiver_name": "钱宇超",
        "receiver_addr": "9-561",
        "phone": "17766232816",
        "sold_goods": [
            {
                "id": 1,
                "goods_id": 3,
                "order_id": 1,
                "deal_price": 2.0,
                "amount": 2,
                "rate": 5.0
            },
            {
                "id": 2,
                "goods_id": 10,
                "order_id": 1,
                "deal_price": 3.8,
                "amount": 1,
                "rate": 4.0
            }
        ],
        "total_price": 7.8,
        "rate": 0.0,
        "handled": true,
        "completed": true,
        "closed": false,
        "place_dt": "2016-03-18 12:22:56",
        "handle_dt": "2016-03-18 17:23:03",
        "complete_dt": "2016-03-18 12:34:13",
        "close_dt": ""
    }
]
```

- `GET /order/closed[?limit=]`, 获取所有已关闭订单信息

输出:

```json
[
    {
        "id": 1,
        "receiver_name": "钱宇超",
        "receiver_addr": "9-561",
        "phone": "17766232816",
        "sold_goods": [
            {
                "id": 1,
                "goods_id": 3,
                "order_id": 1,
                "deal_price": 2.0,
                "amount": 2,
                "rate": 5.0
            },
            {
                "id": 2,
                "goods_id": 10,
                "order_id": 1,
                "deal_price": 3.8,
                "amount": 1,
                "rate": 4.0
            }
        ],
        "total_price": 7.8,
        "rate": 0.0,
        "handled": true,
        "completed": false,
        "closed": true,
        "place_dt": "2016-03-18 12:22:56",
        "handle_dt": "2016-03-18 17:23:03",
        "complete_dt": "",
        "close_dt": "2016-03-18 17:23:56"
    }
]
```

- `GET /order/<int:order_id>`, 获取特定 id 的订单信息

输出:

```json
{
    "id": 2,
    "receiver_name": "宋夏子杰",
    "receiver_addr": "9-561",
    "phone": "17766232876",
    "sold_goods": [
        {
            "id": 3,
            "goods_id": 6,
            "order_id": 2,
            "deal_price": 1.5,
            "amount": 4,
            "rate": 0.0
        }
    ],
    "total_price": 6.0,
    "rate": 0.0,
    "handled": false,
    "completed": false,
    "closed": false,
    "place_dt": "2016-03-18 17:21:56",
    "handle_dt": "",
    "complete_dt": ""
}
```

- `POST /order/add`, 添加订单

输入:

```json
{
    "receiver_name": "钱宇超",
    "receiver_addr": "9-561",
    "phone": "17766232816",
    "sold_goods": [
        {
            "goods_id": 6,
            "amount": 4
        },
        {
            "goods_id": 11,
            "amount": 2
        }
    ]
}
```

输出:

```json
{
    "ok": true,
    "id": 21
}
```

- `POST /order/<int:order_id>/update`, 修改订单

输入:

```json
{
    "receiver_name": "钱宇超",
    "receiver_addr": "9-561",
    "phone": "17766232816"
}
```

输出:

```json
{
    "ok": true
}
```

- `POST /order/<int:order_id>/handle`, 处理订单

输出:

```json
{
    "ok": true
}
```

- `POST /order/<int:order_id>/complete`, 完成订单

输出:

```json
{
    "ok": true
}
```

- `POST /order/<int:order_id>/close`, 关闭订单

输出:

```json
{
    "ok": true
}
```

- (未实现) `POST /order/<int:order_id>/delete`, 删除订单

输出:

```json
{
    "ok": true
}
```

- (未实现) `POST /order/<int:order_id>/rate?score=`, 评价总订单

输出:

```json
{
    "ok": true
}
```

- (未实现) `POST /order/sold-goods/<int:sold_goods_id>/rate?score=`, 评价订单中单种商品

输出:

```json
{
    "ok": true
}
```
