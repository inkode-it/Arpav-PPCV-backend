"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import dotenv
import django
from channels.routing import get_default_application
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.environ.get("DJANGO_SETTINGS_MODULE", "djangoapp.settings"))
django.setup()
from djangoapp.routing  import application as app

#application = routing.application
application = app