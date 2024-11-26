# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1241024/data/www/api.designartproject.ru/django_project')
sys.path.insert(1, '/var/www/u1241024/data/www/api.designartproject.ru/venv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()