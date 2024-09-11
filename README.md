# Blog Application Backend

This blog API, developed with Django REST Framework and PostgreSQL, enables users to manage blog posts through create, read, update, and delete operations. It also offers functionalities such as user authentication, commenting, post favoriting, and liking or disliking posts.

## Technologies Used

- Django Rest Framework
- PostgreSQL
- JWT (JSON Web Tokens)
- Swagger and Redoc

## Features Include

- **User Authentication:** Registration and token management (JWT).
- **Posts:** Create, update, delete, and list blog posts. Only the author can modify their posts.
- **Comments:** Users can comment on a post or another comment. Comments can be managed by the author or an admin.
- **Favorites:** Users can mark posts as favorites. Each user's favorites are private to them.
- **Likes & Dislikes:** Users can like or dislike posts.


## API ENDPOINTS

More detailed description available at /swagger and /redoc

### Auth

| Allowed Methods | Url                     | Description       |
| --------------- | ----------------------- | ----------------- |
| POST            | /api/auth/register      | Create an Account |
| POST            | /api/auth/token         | Generating a JWT  |
| POST            | /api/auth/token/refresh | Refreshes the JWT |


### User

| Allowed Methods | Url                            | Description             |
| --------------- | ------------------------------ | ----------------------- |
| GET             | /api/user/{username}           | User Information        |
| GET             | /api/user/{username}/posts     | List User Posts         |
| GET             | /api/user/{username}/likes     | List User Likes         |
| GET             | /api/user/{username}/dislikes  | List User Dislikes      |
| GET             | /api/user/{username}/favorites | List User Favorites     |
| GET             | /api/user/{username}/comments  | List User Comments      |
| PATCH           | /api/user/{username}/edit      | Update User Information |

### Posts

| Allowed Methods         | Url                           | Description                               |
| ----------------------- | ----------------------------- | ----------------------------------------- |
| GET, POST               | /api/posts                    | List or Create Posts                      |
| GET, PUT, PATCH, DELETE | /api/posts/{id}               | Operations Related to an Existing Post    |
| GET, POST               | /api/posts/{post_id}/comments | List or Create Comments                   |
| GET, PUT, PATCH, DELETE | /api/posts/comments/{id}      | Operations Related to an Existing Comment |

### Interactions

| Allowed Methods | Url                                       | Description                                |
| --------------- | ----------------------------------------- | ------------------------------------------ |
| GET, POST       | /api/interactions/like/post/{post_id}     | List or Create Likes                       |
| GET, DELETE     | /api/interactions/like/{id}               | Operations Related to an Existing Like     |
| GET, POST       | /api/interactions/dislike/post/{post_id}  | List or Create a Dislike                   |
| GET, DELETE     | /api/interactions/dislike/{id}            | Operations Related to an Existing Dislike  |
| POST            | /api/interactions/favorite/post/{post_id} | Create a Favorite                          |
| GET, DELETE     | /api/interactions/favorite/{id}           | Operations Related to an Existing Favorite |

