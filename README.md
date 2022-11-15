## Create postgres container

`docker run --name hw_28_pg -e POSTGRES_PASSWORD=hw_28_postgres -p 5432:5432 -d postgres`

## Migrate database

`python manage.py migrate`

## Create superuser and load data via admin console

`python manage.py createsuperuser`

### OR

`python manage.py loaddata loaddata/*`

