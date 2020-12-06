from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models as gis_models
from django.db.models import Manager as GeoManager


class CommonOfficeInfo(models.Model):
    title = models.CharField(max_length=400)
    designation = models.CharField(max_length=400)
    area_of_coverage = models.IntegerField()
    physical_features = models.TextField(max_length=250, null=True)
    number_of_staff = models.IntegerField()
    issues_addressed = models.TextField(max_length=800, null=True)
    objects = GeoManager()
    location = gis_models.PointField(srid=4326)

    class Meta:
        abstract = True


class HeadOffice(CommonOfficeInfo):
    designation = models.CharField(max_length=400, default="Head Office")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Head Office"


class RegionalOffice(CommonOfficeInfo):
    designation = models.CharField(max_length=400, default="Regional Office")
    head_office = models.ForeignKey(HeadOffice, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Regional Offices"


class FieldOffice(CommonOfficeInfo):
    designation = models.CharField(max_length=400, default="Field Office")
    regional_office = models.ForeignKey(RegionalOffice,
                                        on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Field Offices"


class County(gis_models.Model):
    name = gis_models.CharField(max_length=25)
    code = gis_models.IntegerField()
    city_code = gis_models.CharField(max_length=24)
    geom = gis_models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = "Counties"
