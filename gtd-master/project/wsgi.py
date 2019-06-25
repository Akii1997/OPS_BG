import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()
import logging

from django.core.wsgi import get_wsgi_application

log = logging.getLogger(__name__)

application = get_wsgi_application()
