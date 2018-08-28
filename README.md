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

## Listing reservations

`GET /api/seating`

Response:

```json
[
    {
        "id": 1,
        "seats_available": 4,
        "AC": false
    },
    {
        "id": 2,
        "seats_available": 3,
        "AC": false
    },
    {
        "id": 3,
        "seats_available": 4,
        "AC": false
    },
    {
        "id": 4,
        "seats_available": 0,
        "AC": false
    },
    {
        "id": 5,
        "seats_available": 4,
        "AC": false
    },
    {
        "id": 6,
        "seats_available": 3,
        "AC": false
    },
    {
        "id": 7,
        "seats_available": 4,
        "AC": false
    },
    {
        "id": 8,
        "seats_available": 0,
        "AC": false
    },
    {
        "id": 9,
        "seats_available": 4,
        "AC": true
    },
    {
        "id": 10,
        "seats_available": 3,
        "AC": true
    },
    {
        "id": 11,
        "seats_available": 4,
        "AC": true
    },
    {
        "id": 12,
        "seats_available": 0,
        "AC": true
    },
    {
        "id": 13,
        "seats_available": 4,
        "AC": true
    },
    {
        "id": 14,
        "seats_available": 3,
        "AC": true
    },
    {
        "id": 15,
        "seats_available": 4,
        "AC": true
    },
    {
        "id": 16,
        "seats_available": 0,
        "AC": true
    }
]
```

## Creating a reservation

`CREATE /api/reservations`

Request:

```json
{
    "table": 1
}
```

<!-- Response:

```json
{
    "id": 1,
    "placed_at": 
}
``` -->