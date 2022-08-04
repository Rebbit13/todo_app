This is a test web service for todo list
---
In this app I was trying to follow rules of clean architecture and DDD.
This simple app can register user, generate JWT tokens, creates todos and set it done

Routes
---
* `/user`:
    * POST `/sign_up` - register user, gets username and password
    * POST `/sign_in` - generates token pair for user, gets username and password
    * POST `/refresh` - generates token pair for user, gets refresh token
    * PATCH `/change_password` - set new password, gets username and password
* `/todo`:
    * GET - get all todos for authorised user
    * POST - create new todo for authorised user
    * PATCH `/{todo_uuid}` - update todo by uuid
    * POST `/{todo_uuid}/set_done` - set todo done

Envs
---

| Name                      | Description                                      |
|---------------------------|--------------------------------------------------|
| `JWT_SECRET`              | Secret for JWT generate                          |
| `JWT_ALGORITHM`           | Algorithm for JWT generate                       |
| `JWT_PAYLOAD_TIME_FORMAT` | Time format to store expired_at in token payload |
| `LOG_LEVEL`               | Must be upper case string                        |
| `DEBUG`                   | Debug mode for fastapi app, must be bool         |
| `DB_USER`                 | User for database                                |
| `DB_PASSWORD`             | Password for database                            |
| `DB_HOST`                 | Database host                                    |
| `DB_PORT`                 | Database port                                    |
| `DB_NAME`                 | Database name                                    |


Migrate
---
To generate migration with aerich (you must install aerich):
> aerich migrate

For apply migrations:
> aerich upgrade


Run
---

> docker-compose build && docker-compose up


