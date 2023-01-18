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
* GET POST /perks [x]
* GET PUT DELETE /perks/1 [x]

## Medias
* POST /medias
* DELETE /medias/1

## Users
* GET PUT /me (공개되지 않을 개인적인 정보)
* POST /users
* GET /users/username  (공개될 정보)
* PUT /users/change-password
* POST /users/log-in
* POST /users/log-out
* POST /users/github


{
    "username": "wonju2",
    "email": "wonju2@wonju.com",
    "name": "이원주2",
    "gender": "female",
    "language": "kr",
    "currency": "won",
    "password": "123456",
}