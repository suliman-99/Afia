from django.db import models 


class Country(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Cities"
        unique_together = ('name', 'country')


class Specialization(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    def __str__(self) -> str:
        return self.name

