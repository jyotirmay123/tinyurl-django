# tinyurl-django

### Run

- Create a virtual environment `python -m venv venv`
- Activate the virtual environment `source venv/bin/activate`
- Set up Postgress database in local machine
- Update db credentials in __DTATABSE__ section of settings.py like below:
    ```JSON
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': '<DATABSE NAME>',
                'USER': '<USER_NAME>',
                'PASSWORD': '<PASSWORD>',
                'HOST': '127.0.0.1',
                'PORT': '5432',
            }
        }
    ```
- Install requirements `pip install -r requirements.txt`
- Migrate tables `./manage.py migrate`
- Run test-cases `./manage.py test`
- Run server `./manage.py runserver`
- Open `localhost:8000/tinyurl` in a browser window.