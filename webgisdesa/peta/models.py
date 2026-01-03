from django.db import models

# Create your models here.

class Superhero(models.Model):
    nama = models.CharField(max_length=80)
    # lat = models.DecimalField(max_digits=15, decimal_places=5)
    # long = models.DecimalField(max_digits=15, decimal_places=5)
    # asosiasi = models.CharField(max_length=20)
    asosiasi = models.CharField(max_length=20)

    def __str__(self):
        return self.nama
    


    