from django.db import models
from django import forms

class myPageInFomation(models.Model):
    apiprovider = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(primary_key=True, max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    userimage = models.CharField(max_length=200, blank=True, null=True)
    profile = models.CharField(max_length=200, blank=True, null=True)
    joiningdate = models.DateTimeField(null=True)
    votingcount = models.IntegerField(blank=True, null=True)
    #authentication = models.CharField(max_length=20, blank=True, null=True)
    #uniemail = models.CharField(max_length=50, blank=True, null=True)
    # pwd = models.CharField(max_length=20, blank=True, null=True)
    account = models.CharField(max_length=100, blank=True, null=True)



class uploadContents(models.Model):
    contents_id = models.AutoField(primary_key=True, default=1)
    writeremail = models.CharField(max_length=50)  # 기본키 설정??
    filename = models.CharField(max_length=100)
    contentspath = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    publisheddate = models.DateTimeField()
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    tags = models.CharField(max_length=50)
    fileinfo = models.CharField(max_length=250)
    totalpages = models.IntegerField()
    previewpath = models.CharField(max_length=250)
    authorinfo = models.CharField(max_length=1000)
    intro = models.CharField(max_length=1000)
    index = models.CharField(max_length=1000)
    contents = models.CharField(max_length=1000)  # 소개글 제한?
    reference = models.CharField(max_length=1000, default=True)
    hash = models.CharField(max_length=150)
