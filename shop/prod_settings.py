
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'lm@6f4crv9h9io2365a-0deh*pe%*1u6#__tqpzp2g1qo2kw2iyzhn'

DEBUG = False


ALLOWED_HOSTS = ['45.147.178.9', 'diamstore.site', '127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postresql_psycopg2',
        'NAME' : 'shop',
        'USER' : 'userdb',
        'PASSWORD' : 'mirgul1234',
        'HOST' : '45.147.178.9',
        'PORT' : '5432',

    }

}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'mainapp/static')

try:
    from .local_settings import *
except ImportError:
    from .prod_settings import *