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
    ilce_ad = models.CharField(max_length=50, verbose_name="İlçe İsim")
    ilce_search_ad = models.CharField(max_length=50, verbose_name="İlçe İsim (Search)")
    mahalle_ad = models.CharField(max_length=50, verbose_name="Mahalle İsim")
    mahalle_search_ad = models.CharField(max_length=50, verbose_name="Mahalle İsim (Search)")
    kapi_no = models.CharField(max_length=50, verbose_name="Kapı No")
    kapi_search_no = models.CharField(max_length=50, verbose_name="Kapı No (Search)")
    bina_ad = models.CharField(max_length=250, verbose_name="Bina İsmi")
    yol_ad = models.CharField(max_length=250, verbose_name="Yol İsmi")
    yol_search_ad = models.CharField(max_length=250, verbose_name="Yol İsmi (Search)")
    geo = models.GeometryField(verbose_name="Geometri")


class POI(models.Model):
    poi_id = models.BigIntegerField(verbose_name="POI ID")
    kategori_id = models.SmallIntegerField(verbose_name="Kategori ID", null=True, blank=True)
    alt_kategori_id = models.SmallIntegerField(verbose_name="Alt Kategori ID", null=True, blank=True)
    ad = models.CharField(max_length=250, verbose_name="İsim")
    ilce_ad = models.CharField(max_length=50, verbose_name="İsim")
    mahalle_ad = models.CharField(max_length=50, verbose_name="Mahalle İsim")
    kategori = models.CharField(max_length=50, verbose_name="Kategori", null=True, blank=True)
    alt_kategori = models.CharField(max_length=50, verbose_name="Alt Kategori", null=True, blank=True)
    icon = models.CharField(max_length=50, verbose_name="İkon", null=True, blank=True)
    bina_ad = models.CharField(max_length=250, verbose_name="Mahalle İsim")
    geo = models.GeometryField(verbose_name="Geometri")
