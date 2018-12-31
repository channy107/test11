from django.db import models
from django import forms
from models import *
from datetime import datetime

class myPageInfomation(models.Model):
    IDX = models.AutoField(default=1)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    apiprovider = models.CharField(max_length=50)
    email = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    userimage = models.CharField(max_length=200, blank=True, null=True)
    profile = models.CharField(max_length=200, blank=True, null=True)
    joiningdate = models.DateTimeField()
    votingcount = models.IntegerField()


class wallet(models.Model):
    IDX = models.AutoField(default=1)
    id = models.ForeignKey(myPageInfomation, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    account = models.CharField(max_length=100)
    privateKey = models.CharField(max_length=100)
    balance = models.IntegerField()
    transactions = models.CharField()



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


class replyForContents(models.Model):
    IDX = models.AutoField(default=1)
    id = models.ForeignKey(uploadContents, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    writer = models.CharField(max_length=50)
    contents = models.CharField(max_length=1000)



class forum(models.Model):
    contents_id = models.AutoField(primary_key=True, default=1)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    writer = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)
    contents = models.CharField(max_length=10000)


class imagesForForum(models.Model):
    IDX = models.AutoField(default=1)
    id = models.ForeignKey(forum, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    path = models.CharField(max_length=200)
    filename = models.CharField(max_length=200)


class replyForForum(models.Model):
    IDX = models.AutoField(default=1)
    contents_id = models.ForeignKey(forum, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    writer = models.CharField(max_length=50)
    contents = models.CharField(max_length=1000)


class voters(models.Model):
    IDX = models.AutoField(default=1)
    id = models.ForeignKey(forum, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    list_of_voters = models.CharField(max_length=50)
