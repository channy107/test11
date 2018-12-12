from django.db import models


class myPage(models.Model):
    apiprovider = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(primary_key=True, max_length=50, blank=True)
    name = models.DateTimeField(max_length=50, blank=True, null=True)
    userimage = models.CharField(max_length=200, blank=True, null=True)
    profile = models.CharField(max_length=200, blank=True, null=True)
    joiningdate = models.DateTimeField(null=True)
    votingcount = models.IntegerField(blank=True, null=True)
    authentication = models.IntegerField(blank=True, null=True)
    uniemail = models.CharField(max_length=50, blank=True, null=True)
# Create your models here.
