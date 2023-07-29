"""
ASGI config for TASK_MANAGER_USING_ANGULAR_AND_DJANGO project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TASK_MANAGER_USING_ANGULAR_AND_DJANGO.settings')

application = get_asgi_application()
