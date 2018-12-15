from django.db import models

class myPageInFomation(models.Model):
    apiprovider = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(primary_key=True, max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    userimage = models.CharField(max_length=200, blank=True, null=True)
    profile = models.CharField(max_length=200, blank=True, null=True)
    joiningdate = models.DateTimeField(null=True)
    votingcount = models.IntegerField(blank=True, null=True)
    authentication = models.CharField(max_length=20, blank=True, null=True)
    uniemail = models.CharField(max_length=50, blank=True, null=True)
    pwd = models.CharField(max_length=20, blank=True, null=True)
    account = models.CharField(max_length=100, blank=True, null=True)
