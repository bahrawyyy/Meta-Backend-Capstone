# Meta-Backend-Capstone Endpoints

| Method | URL Path                         | Description                          |
|--------|---------------------------------|--------------------------------------|
| GET    | /restaurant/                     | Index page                            |
| GET    | /restaurant/home/                | Home page                             |
| GET    | /restaurant/menu/                | List all menu items                   |
| POST   | /restaurant/menu/                | Create a new menu item                |
| GET    | /restaurant/menu/<int:pk>        | Retrieve a single menu item by ID    |
| PUT    | /restaurant/menu/<int:pk>        | Update a menu item by ID              |
| DELETE | /restaurant/menu/<int:pk>        | Delete a menu item by ID              |
| GET    | /restaurant/booking/tables/      | List all bookings                     |
| POST   | /restaurant/booking/tables/      | Create a new booking                  |
| GET    | /restaurant/booking/tables/<int:pk>/ | Retrieve a booking by ID          |
| PUT    | /restaurant/booking/tables/<int:pk>/ | Update a booking by ID            |
| DELETE | /restaurant/booking/tables/<int:pk>/ | Delete a booking by ID            |
| POST   | /auth/users/                      | Register a new user                   |
| POST   | /auth/token/login/                | Login and obtain auth token           |
| POST   | /auth/token/logout/               | Logout                                |
| POST   | /api-token-auth/                  | Obtain token (DRF built-in endpoint) |
