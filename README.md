# Django API Boilerplate

Basic project boilerplate for django only as backend api

- django
- django-rest-framework
- django-cors-headers

### How to use
Create virtual environment, change project_name with your projects name :D
```sh
mkvirtualenv project_name
```

Install django
```sh
pip install django
```

Run django startproject with the --template option
```sh
django-admin.py startproject --template=https://github.com/netoxico/django-api-boilerplate/archive/master.zip project_name
```

Install requirements, for development
```sh
pip install -r requirements/development.txt
```

Set 'PROJECT_ENV' environment variable.
* 'development'
* 'production',
* 'staging'

If no 'PROJECT_ENV' especified takes 'development' settings as default

`NOTE: in development`
