
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'lm@6f4crv9h9ioa-0deh*pe%*1u6#__tqpzp2g1qo2kw2iyzhn'


DEBUG = True

ALLOWED_HOSTS = [ ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'mainapp/static')




