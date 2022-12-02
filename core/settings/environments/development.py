# Standard imports
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure-*gaqx96fy!uwj#oi$k4jcg4q5(a&!qm1&%5$rv)q=68fx7w=q('

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(locals()['BASE_DIR'], "db.sqlite3"),
        'TEST': {
            'NAME': os.path.join(locals()['BASE_DIR'], "test.sqlite3"),
        },
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,
            "SOCKET_TIMEOUT": 5,
        },
    }
}

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'

STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR / 'media/'
MEDIA_URL = '/media/'
