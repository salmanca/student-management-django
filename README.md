# student-management-django
This project is created for student management.
User can add the marks obtained by each student.

Project Setup:
        Clone the project in your computer.
        Change the database according to the database you are using.
              DATABASES = {
                      'default': {
                          'ENGINE': 'django.db.backends.postgresql',
                          'NAME': 'database name',
                          'USER': 'username',
                          'PASSWORD': 'database password',
                          'HOST': '127.0.0.1',
                          'PORT': 'port', this is optional
                      }
                  }
                  
        Migrate your models by entering command : python manage.py migrate
        Runserver : python manage.py runserver
        You can check the server in : localhost:8000 in your browser
        
        You can also create Super User for accessing the admin page where you can add, edit and delete students and subjects
        Command : python manage.py createsuperuser
