import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


#  TODO - create filter for PointField(address)
#  TODO - permissions
#  TODO - fix_activate_link
#  TODO - deploy
#  TODO - docker
#  TODO - chat
#  TODO - parsing
