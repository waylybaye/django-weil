# DJANGO-WEIL

django weil is a weil client for django


### INSTALL

    $ pip install django-weil
    $ vi settings.py

    # Add dj_weil to Installed Apps
    INSTALLED_APPS = [
        ...
        'dj_weil',
    ]

    # Set the email backend
    EMAIL_BACKEND = "dj_weil.backend.EmailBackend""
    WEIL_END_POINT = "http://internal.com/api/send"
    WEIL_ACCESS_TOKEN = "your-secret-token"

    $ ./manage.py syncdb

Start send your mail !
