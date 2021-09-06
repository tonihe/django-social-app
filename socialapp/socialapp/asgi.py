"""
ASGI config for socialapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialapp.settings')

django_asgi_app = get_asgi_application()
django_wsgi_app = get_wsgi_application()

application = ProtocolTypeRouter({
    "http": django_wsgi_app,
    # Just HTTP for now. (We can add other protocols later.)
})