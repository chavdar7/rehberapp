from django.db import models

# Create your models here.

class Contact(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    telno = models.CharField(max_length=50)
    fav = models.BooleanField(default=False)
    block = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.ad