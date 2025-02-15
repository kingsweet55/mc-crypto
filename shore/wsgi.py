"""
WSGI config for shore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

# These lines have to be before any Django imports or they will fail
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shore.settings")
os.environ.setdefault('ALLOWED_HOSTS', '*')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
