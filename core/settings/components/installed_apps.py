INSTALLED_APPS = [
    # core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third-party apps
    'drf_yasg',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_celery_beat',
    # local apps
    'apps.common.apps.CommonConfig',
    'apps.accounts.apps.AccountsConfig',
    'apps.notifications.apps.NotificationsConfig',
]
