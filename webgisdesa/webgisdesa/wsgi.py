import os
import sys
from django.core.wsgi import get_wsgi_application

# Menghitung path ke folder yang berisi 'manage.py'
# Agar Django bisa menemukan folder 'webgisdesa.settings'
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webgisdesa.settings")

application = get_wsgi_application()

# Baris ini sangat krusial untuk Vercel (Serverless Function)
app = application
