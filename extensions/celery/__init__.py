from __future__ import absolute_import

# Standard imports
import os

# Third-party imports.
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
