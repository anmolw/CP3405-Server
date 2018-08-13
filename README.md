# API Reference

## Restaurant listing

`GET /api/restaurants`

Response:
```json
[
    {
        "id": 1,
        "name": "Japanese Food",
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