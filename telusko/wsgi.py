

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telusko.settings')

application = get_wsgi_application()

# vercel_app/wsgi.py
app = get_wsgi_application()
