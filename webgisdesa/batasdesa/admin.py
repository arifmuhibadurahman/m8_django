from django.contrib.gis import admin
from .models import BangunanPogung
from leaflet.admin import LeafletGeoAdmin

class AdminPogung(LeafletGeoAdmin):
    settings_overrides = {
        'DEFAULT_CENTER': (-7.760030, 110.376214),  # atur zoom ke Pogung
        'DEFAULT_ZOOM': 14,
    }

# daftarkan model pada halaman admin
admin.site.register(BangunanPogung, AdminPogung)
