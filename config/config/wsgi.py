"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os, sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/config/config')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.config.settings')
application = get_wsgi_application()
