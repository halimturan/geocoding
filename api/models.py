from django.contrib.gis.db import models


class Ilce(models.Model):
    ilce_id = models.SmallIntegerField(verbose_name="İlçe ID")
    ad = models.CharField(max_length=50, verbose_name="İsim")
    geo = models.GeometryField(verbose_name="Geometri")


class Mahalle(models.Model):
    ilce_id = models.SmallIntegerField(verbose_name="İlçe ID")
    mahalle_id = models.IntegerField(verbose_name="Mahalle ID")
    ilce_ad = models.CharField(max_length=50, verbose_name="İsim")
    ad = models.CharField(max_length=50, verbose_name="İsim")
    geo = models.GeometryField(verbose_name="Geometri")


class Yol(models.Model):
    ilce_id = models.IntegerField(verbose_name="İlçe ID")
    mahalle_id = models.IntegerField(verbose_name="Mahalle ID")
    ilce_ad = models.CharField(max_length=50, verbose_name="İsim")
    mahalle_ad = models.CharField(max_length=50, verbose_name="Mahalle İsim")
    ad = models.CharField(max_length=250, verbose_name="İsim")
    geo = models.GeometryField(verbose_name="Geometri")


class Kapi(models.Model):
    ilce_id = models.IntegerField(verbose_name="İlçe ID")
    mahalle_id = models.IntegerField(verbose_name="Mahalle ID")
    ilce_ad = models.CharField(max_length=50, verbose_name="İsim")
    mahalle_ad = models.CharField(max_length=50, verbose_name="Mahalle İsim")
    kapi_no = models.CharField(max_length=50, verbose_name="Kapı No")
    bina_ad = models.CharField(max_length=250, verbose_name="Bina İsmi")
    yol_ad = models.CharField(max_length=250, verbose_name="Yol İsmi")
    geo = models.GeometryField(verbose_name="Geometri")


class POI(models.Model):
    poi_id = models.BigIntegerField(verbose_name="POI ID")
    ad = models.CharField(max_length=250, verbose_name="İsim")
    ilce_ad = models.CharField(max_length=50, verbose_name="İsim")
    mahalle_ad = models.CharField(max_length=50, verbose_name="Mahalle İsim")
    bina_ad = models.CharField(max_length=250, verbose_name="Mahalle İsim")
    geo = models.GeometryField(verbose_name="Geometri")
