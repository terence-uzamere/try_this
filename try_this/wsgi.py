"""
WSGI config for try_this project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
<<<<<<< HEAD

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "try_this.settings")

application = get_wsgi_application()
=======
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "try_this.settings")

application = Cling(get_wsgi_application())
>>>>>>> b36305de2d14cb77f2669caefd3f1b6f6d8f9afe
