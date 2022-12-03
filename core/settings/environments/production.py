# Standard imports
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure-*gaqx96fy!uwj#oi$k4jcg4q5(a&!qm1&%5$rv)q=68fx7w=q('

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DEFAULT_DB_NAME"),
        'USER': os.environ.get("DEFAULT_DB_USER"),
        'PASSWORD': os.environ.get("DEFAULT_DB_PASSWD"),
        'HOST': "postgresdb",
        'PORT': 5432,
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
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
