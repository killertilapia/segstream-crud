# Requirements
1. Python 3.11
2. Node 18.12.1

Optional
- poetry - https://python-poetry.org/

# Get Started

## Backend API Server
- Made using Django4.1 with Rest
- Dependencies managed by poetry but `requirements.txt` available

1. `$ cd segstream`
2. `$ poetry install` - should run for a few minutes
3. `$ poetry shell` - activate virtualenv
4. `$ python manage.py migrate`
5. `$ python manage.py createsuperuser`
6. `$ python manage.py runserver`

## Endpoints
I'm assuming that the base url is: `http://localhost:8000`

1. `api/v1/docs/` - Swagger or OpenAPI docs; Only accessible if DEBUG is True
2. `api/v1/users/` - full CRUD for Users
3. `api/v1/apilogs/` - Read-only for API Logs

The `admin` route is also available.

## Frontend
- Made with Vue3

1. `$ cd frontend`
2. `$ npm install` - should run for a few minutes
3. `$ npm run dev`
4. Open a browser and navigate to http://localhost:5173

## Running API Unit test
1. `$ cd segstream`
2. `$ poetry shell`
3. `$ python manage.py test apps -v 2 --settings=segstream.test_settings`

The `test_settings.py` file inherits from the `settings.py`. The only difference
is that the `test_settings.py` uses a memory-only DB.


