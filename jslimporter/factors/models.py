from django.db import models
from django.utils import timezone


class Bunch(models.Model):
    categoryname = models.CharField(max_length=50, blank=False, null=False)
    chaptername = models.CharField(max_length=50, blank=False, null=False)
    sectionname = models.CharField(max_length=50, blank=False, null=False)
    termname = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.categoryname


class Bunchrelate(models.Model):
    relatepages = models.CharField(
        max_length=7, unique=True, blank=False, null=False)
    slideheader = models.CharField(max_length=50, blank=False, null=False)
    bunch = models.ForeignKey(Bunch, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.relatepages


class Details(models.Model):
    jslidepage = models.CharField(
        max_length=2, unique=True, blank=False, null=False)
    template = models.CharField(blank=False, null=False, max_length=50)
    leadtext = models.TextField
    image1 = models.CharField(blank=True, null=True, max_length=50)
    image3 = models.CharField(blank=True, null=True, max_length=50)
    image4 = models.CharField(blank=True, null=True, max_length=50)
    image5 = models.CharField(blank=True, null=True, max_length=50)
    image6 = models.CharField(blank=True, null=True, max_length=50)
    image7 = models.CharField(blank=True, null=True, max_length=50)
    image8 = models.CharField(blank=True, null=True, max_length=50)
    footertext1 = models.CharField(blank=True, null=True, max_length=50)
    footericon1 = models.CharField(blank=True, null=True, max_length=50)
    footertext2 = models.CharField(blank=True, null=True, max_length=50)
    footericon2 = models.CharField(blank=True, null=True, max_length=50)
    footertext3 = models.CharField(blank=True, null=True, max_length=50)
    footericon3 = models.CharField(blank=True, null=True, max_length=50)
    footertext4 = models.CharField(blank=True, null=True, max_length=50)
    footericon4 = models.CharField(blank=True, null=True, max_length=50)
    footertext5 = models.CharField(blank=True, null=True, max_length=50)
    footericon5 = models.CharField(blank=True, null=True, max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    bunchrelate = models.ForeignKey(Bunchrelate, on_delete=models.PROTECT)

    def __str__(self):
        return self.jslidepage


# Create your models here.
