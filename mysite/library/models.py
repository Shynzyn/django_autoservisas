from django.db import models
import uuid


# Create your models here.

class Automobilis(models.Model):
    valstybinis_nr = models.CharField(verbose_name="Valstybinis numeris", max_length=50)
    automobilio_modelis = models.ForeignKey(to="AutomobilioModelis", on_delete=models.SET_NULL, null=True)
    vin_kodas = models.CharField(verbose_name="Vin kodas", max_length=17, )
    klientas = models.CharField(verbose_name="Klientas", max_length=200, )

    def __str__(self):
        return f"{self.automobilio_modelis}, VIN: {self.vin_kodas}, VN: {self.valstybinis_nr}, Klientas: {self.klientas}"


class AutomobilioModelis(models.Model):
    marke = models.CharField(verbose_name="Automobilio marke", max_length=50, )
    modelis = models.CharField(verbose_name="Automobilio modelis", max_length=50, )

    def __str__(self):
        return f"{self.marke} {self.modelis}"


class Uzsakymas(models.Model):
    data = models.DateField(verbose_name="Uzsakymo data", null=True)
    automobilis = models.ForeignKey(to="Automobilis", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.data} {self.automobilis}"


class Paslauga(models.Model):
    pavadinimas = models.TextField(verbose_name="Paslaugos pavadinimas", max_length=500)
    kaina = models.CharField(verbose_name="Paslaugos kaina", max_length=50)

    def __str__(self):
        return f"{self.pavadinimas}"


class UzsakymoEilute(models.Model):
    paslauga = models.ForeignKey(to="Paslauga", on_delete=models.SET_NULL, null=True)
    uzsakymas = models.ForeignKey(to="Uzsakymas", on_delete=models.SET_NULL, null=True)
    kiekis = models.CharField(verbose_name="Kiekis", max_length=50)

    def __str__(self):
        return f"{self.kiekis} {self.paslauga} ------ [{self.uzsakymas}] "
