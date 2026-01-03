from django.db import models

# Create your models here.
from django.contrib.gis.db import models as gismodels


class BangunanPogung(models.Model):
    nama = gismodels.CharField(max_length=254, null=True, blank=True)
    jenis = gismodels.CharField(max_length=254, null=True, blank=True)
    pemilik = models.ForeignKey("peta.Superhero", on_delete=models.CASCADE, null=True, blank=True)
    geom = gismodels.MultiPolygonField(srid=4326, null=True, blank=True)



