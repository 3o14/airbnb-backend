## Categories
* GET POST /categories
* GET(Rooms) PUT DELETE /categories/1

## Rooms
* GET POST /rooms
* GET PUT DELETE /rooms/1
* GET /rooms/1/amenities
* GET /rooms/1/reviews
* GET POST /rooms/1/bookings
* GET PUT DELETE /rooms/1/bookings/2
* GET POST /amenities
* GET PUT DELETE /amenities/1

## Experiences
* GET POST /experiences
* GET PUT DELETE /experiences/1
* GET /experiences/1/perks
* GET POST /experiences/1/bookings
* GET PUT DELETE /experiences/1/bookings
* GET POST /perks
* GET PUT DELETE /perks/1

## Medias
* POST /medias
* DELETE /medias/1

## Users
* GET PUT /me (공개되지 않을 개인적인 정보)
* POST /users
* GET /users/username  (공개될 정보)
* POST /users/log-in
* POST /users/change-password
* POST /users/github


{
    "last_login": "2023-01-11T19:07:49.327300+09:00",
    "username": "wonju",
    "email": "",
    "date_joined": "2022-12-28T18:18:27.200285+09:00",
    "avatar": "",
    "name": "원주",
    "is_host": null,
    "gender": "",
    "language": "",
    "currency": ""
}