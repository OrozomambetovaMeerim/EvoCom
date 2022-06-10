import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-@gfqv(@mikkbf58utrnhf45kd;k90b/gghghfidw3#+l$3!!7r)(6e+tnbj1(h9wvvs_(v%64#'

DEBUG = False

ALLOWED_HOSTS = ['evocomservice.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'evocom_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]