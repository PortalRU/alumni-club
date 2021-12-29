import os
from django.core.wsgi import get_wsgi_application

if os.getenv("ENV") == "Heroku":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.production_settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()