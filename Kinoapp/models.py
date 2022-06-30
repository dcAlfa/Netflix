from django.db import models

class Aktyor(models.Model):
    ism = models.CharField(max_length=30)
    mamlakat = models.CharField(max_length=60)
    erkakmi = models.BooleanField()

    def __str__(self):
        return self.ism

class Kino(models.Model):
    nom = models.CharField(max_length=100)
    yil = models.DateField()
    janr = models.CharField(max_length=50)
    aktyorlar = models.ManyToManyField(Aktyor)

    def __str__(self):
        return self.nom