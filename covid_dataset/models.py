from django.db import models


class CountryWiseLatest(models.Model):
    country = models.CharField(max_length=80, blank=True, null=True)
    confirmed = models.FloatField(blank=True, null=True)
    deaths = models.FloatField(blank=True, null=True)
    recovered = models.FloatField(blank=True, null=True)
    who_region = models.CharField(max_length=80, blank=True, null=True)
    country_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'country_wise_latest'

    def __str__(self):
        return self.country
