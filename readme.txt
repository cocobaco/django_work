0. install django and check version
pip install django
python -m django --version

1. create project
django-admin startproject proj1

files and folders created:
    manage.py: command-line utility to interact with project
    inner proj1 dir:
        __init__.py: tells python to consider dir as package
        settings.py: config file for the project
        urls.py: URL declarations for the project (like a table of contents)
        wsgi.py: web server gateway interface

2. run server. in django project folder, type
python manage.py runserver

3. visit website. go to browser, type
localhost:8000 or 127.0.0.1:800

4. admin page
localhost:8000/admin

5. create app (inside project folder)
python manage.py startapp app1

6. edit views.py files inside apps' directories

7. edit corresponding urls.py files (both the apps and the project)
path function: path(route, view, kwargs=None, name=None)
example: path('weblog/', include('blogs.urls'), name='Blog')

8. change models and do migrations
change models (in models.py)
python manage.py makemigrations (tell django that changes are made to the models)
python manage.py migrate (create model tables in the database)

9. create (admin) user
python manage.py createsuperuser

10. check for any problems
python manage.py check

https://docs.djangoproject.com/en/2.1/intro/tutorial02/
