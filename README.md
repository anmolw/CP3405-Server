# API Reference

## Announcements

`GET /api/announcements`

Response:

```json
[
    {
        "title": "Canteen closure",
        "description": "The canteen will be closed on 30/8/18.",
        "created_at": "2018-08-14T08:28:28.276605Z"
    }
]
```

## Restaurant listing

`GET /api/restaurants`

Response:

```json
[
    {
        "id": 1,
        "name": "Japanese Food",
        "thumbnail": "http://example.com/media/default.png",
        "items": [
            {
                "id": 10,
                "name": "Bento Set",
                "price": 4.5
            }
        ]
    },
    {
        "id": 2,
        "name": "Indian Food",
        "items": [
            {
                "id": 23,
                "name": "Samosa",
                "price": 2.5
            }
        ]
    }
]
```

## Placing an order

`CREATE /api/orders`

Request:

```json
{
    "restaurant": 1,
    "items": [
        {
            "item": 1,
            "quantity": 1
        },
        {
            "item": 2,
            "quantity": 2
        }
    ]
}
```