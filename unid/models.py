from django.db import models
from django import forms
from datetime import datetime

class myPageInfomation(models.Model):
    # IDX = models.AutoField(default=1)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    apiprovider = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50, blank=True, null=True)
    userimage = models.CharField(max_length=200, blank=True, null=True)
    profile = models.CharField(max_length=200, blank=True, null=True)
    joiningdate = models.DateTimeField(blank=True, null=True)
    votingcount = models.IntegerField(blank=True, null=True)


class wallet(models.Model):
    # IDX = models.AutoField(default=1)
    email = models.ForeignKey(myPageInfomation, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    account = models.CharField(max_length=100, blank=True, null=True)
    privateKey = models.CharField(max_length=100, blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)
    transactions = models.CharField(max_length=100, blank=True, null=True)



class uploadContents(models.Model):
    contents_id = models.AutoField(primary_key=True, default=1)
    writeremail = models.CharField(max_length=50, blank=True, null=True)  # 기본키 설정??
    filename = models.CharField(max_length=100, blank=True, null=True)
    contentspath = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    publisheddate = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=50, blank=True, null=True)
    fileinfo = models.CharField(max_length=250, blank=True, null=True)
    totalpages = models.IntegerField(blank=True, null=True)
    previewpath = models.CharField(max_length=250, blank=True, null=True)
    authorinfo = models.CharField(max_length=1000, blank=True, null=True)
    intro = models.CharField(max_length=1000, blank=True, null=True)
    index = models.CharField(max_length=1000, blank=True, null=True)
    contents = models.CharField(max_length=1000, blank=True, null=True)  # 소개글 제한?
    reference = models.CharField(max_length=1000, default=True)
    hash = models.CharField(max_length=150, blank=True, null=True)


class replyForContents(models.Model):
    # IDX = models.AutoField(default=1)
    writeremail = models.ForeignKey(uploadContents, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    writer = models.CharField(max_length=50, blank=True, null=True)
    contents = models.CharField(max_length=1000, blank=True, null=True)



class forum(models.Model):
    contents_id = models.AutoField(primary_key=True, default=1)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    writer = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    tags = models.CharField(max_length=50, blank=True, null=True)
    contents = models.CharField(max_length=10000, blank=True, null=True)


class imagesForForum(models.Model):
    # IDX = models.AutoField(default=1)
    contents_id = models.ForeignKey(forum, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    filename = models.CharField(max_length=200, blank=True, null=True)


class replyForForum(models.Model):
    # IDX = models.AutoField(default=1)
    contents_id = models.ForeignKey(forum, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    writer = models.CharField(max_length=50, blank=True, null=True)
    contents = models.CharField(max_length=1000, blank=True, null=True)


class voters(models.Model):
    # IDX = models.AutoField(default=1)
    contents_id = models.ForeignKey(forum, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    list_of_voters = models.CharField(max_length=50, blank=True, null=True)
