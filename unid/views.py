import os
from _sha256 import sha256
from datetime import datetime
from django.contrib.sessions.models import Session
import allauth.socialaccount.providers.google
from ftplib import FTP
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.datastructures import MultiValueDictKeyError
from web3 import Web3, HTTPProvider
from django.shortcuts import render
import requests
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
# from unid.models import myPage
from unid.models import myPageInfomation, contentsInfo
from web3.auto import w3
from unid.models import uploadContents
import random
from django.http import HttpResponseRedirect
from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
import hashlib

def mypage(request):
    # mypage = MypageInfomation.objects.get(email)
    contentsboard = uploadContents.objects.all()
    context = {'mypage':mypage,
               'contentsboard':contentsboard}
    return render(request, 'unid/mypage.html', context)

def contentsboard(request):
    contentsboard = uploadContents.objects.all()
    context = {'contentsboard':contentsboard}
    return render(request, 'unid/contentsboard.html', context)

def mywallet(request):
    return render(request, 'unid/mywallet.html', {})

def transaction(request):
    return render(request, 'unid/transaction.html', {})

def contentsdetail(request):
    return render(request, 'unid/contentsdetail.html', {})

def contentstran(request):
    return render(request, 'unid/contentstran.html', {})

def main(request):
    return render(request, 'unid/main.html', {})

def login(request):
    return render(request, 'unid/login.html', {})

def signup(request):
    return render(request, 'unid/signup.html', {})

def createaccount(request):
    if request.method == 'GET':
        return render(request, 'unid/createaccount.html', {})
    else:
        rpc_url = "http://localhost:8545"
        w3 = Web3(HTTPProvider(rpc_url))

        pwd = request.POST['pwd']
        account = w3.personal.newAccount(pwd)
        br = myPageInfomation(email=request.POST['email'],
                              name=request.POST['name'],
                              joiningdate=timezone.now(),
                              pwd=request.POST['pwd'],
                              account=account
                              )
        br.save()
        url = 'http://localhost:8000/unid'
        return HttpResponseRedirect(url)


def oauth(request):
    if request.method == 'GET':
        code = request.GET.get('code')
        url = "https://kauth.kakao.com/oauth/token"
        payload = "grant_type=authorization_code&client_id=122f531f95d70dabb69ff17f4f1b0be2&redirect_uri=http://localhost:8000/unid/oauth&code=" + str(
            code)
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        # response는 json형식이 아니니까 밑에 코드를 통해 json형식으로 바꾼다
        access_token = json.loads(((response.text).encode('utf-8')))['access_token']
        # return  HttpResponse(access_token)
        url = "https://kapi.kakao.com/v1/user/signup"
        headers.update({'Authorization': "Bearer " + str(access_token)})
        response = requests.request("POST", url, headers=headers)
        # return HttpResponse(response.text)
        url = "https://kapi.kakao.com/v1/user/me"
        response = requests.request("POST", url, headers=headers)
        # email = json.loads(((response.text).encode('utf-8')))['email']
        id = json.loads(((response.text).encode('utf-8')))['id']
        nickname = json.loads(((response.text).encode('utf-8')))['properties']['nickname']
        try:
             member = myPageInfomation.objects.get(email=id)
        except myPageInfomation.DoesNotExist:
            return render(
                request,
                'unid/createaccount.html',
                {'id': id, 'nickname': nickname}
            )
        else:
            request.session['user_email'] = member.email
            request.session['user_name'] = member.name
            request.session['user_account'] = '' + member.account

            url = 'http://localhost:8000/unid/mywallet'
            return HttpResponseRedirect(url)

    else:
        time = timezone.now()
        rpc_url = "http://localhost:8545"
        w3 = Web3(HTTPProvider(rpc_url))

        password = request.POST['pwd']  # ★★★★
        account = w3.personal.newAccount(password)
        lockpwd = sha256(password)
        br = myPageInfomation(email=request.POST['email'],
                              name=request.POST['name'],
                              joiningdate=timezone.now(),
                              pwd=lockpwd,  # ★★★★
                              account=account)
        br.save()
        url = 'http://localhost:8000/unid'
        return HttpResponseRedirect(url)


def contentsupload(request):
    if request.method == 'GET':
        return render(request, 'unid/contentsupload.html', {})
    else:  # submit으로 제출
        try:
            upload_files = request.FILES.getlist('user_files')  # submit에 첨부됨 파일
        except MultiValueDictKeyError:
            pass
        try:
            now = datetime.now()
            today = now.strftime('%Y-%m-%d')
            os.makedirs("uploadfiles/" + today) #그 날짜에 맞는 디렉토리 생성
            # root_dir = "우리 서버"   # ★★★★★★★★★★★
            # contents_dir = root_dir + "/" + today + "/"
            # contents_dir = today + "/"
        except FileExistsError as e:
            pass
        ftpfilelist = []
        uifilelist = []
        for upload_file in upload_files:  # 다중 파일 업로드
            # file_name = upload_file.name
            file_name = str(random.random())
            userfilename = upload_file.name
            ftpfilelist.append(file_name)
            uifilelist.append(userfilename)
            now = datetime.now()
            today = now.strftime('%Y-%m-%d')
            contents_dir = "uploadfiles/" + today + "/"
                      #해당 날짜의 디렉토리
            with open(contents_dir + file_name, 'wb') as file:  # 저장경로
                for chunk in upload_file.chunks():
                    file.write(chunk)

        # 검수시스템 추후 개발예정

        ftp = FTP()
        ftp.connect("210.107.78.157")    #Ftp 주소 Connect(주소 , 포트)
        ftp.login("unid", "dkagh")
        ftp.cwd("/home/unid/contents")
        ftp_contents_dir = "/home/unid/contents/" + today + "/"
        try:
            ftp.mkd(today)
        except:
            ftp.cwd("/home/unid/contents/" + today)
        ftp.cwd("/home/unid/contents/" + today)
        os.chdir("uploadfiles/" + today)
        # contents_dir = today + "/"
        # # with open(contents_dir + file_name, "wb") as file:
        # #     ftp.storlines('STOR %s' % file_name, file)
        filehashdatas = []
        for file in ftpfilelist:
            file_name = file
            uploadfile = open(file_name, "rb")
            filedata = uploadfile.read()
            hashdata = hashlib.sha256(filedata).hexdigest()
            filehashdatas.append(hashdata)
            # uploadfile = open("uploadfiles/" + today + "/" + file_name, "rb")
            ftp.storbinary('STOR ' + file_name, uploadfile)
            uploadfile.close()

        br = uploadContents(
                        contentspath=contents_dir,
                        writeremail=request.session['user_email'],
                        filename=file_name,
                        title=request.POST['title'],
                        publisheddate=request.POST['publisheddate'],
                        category=request.POST['category'],
                        price=request.POST['price'],
                        tags=request.POST['tags'],
                        fileinfo=request.POST['fileinfo'],
                        totalpages=request.POST['totalpages'],
                        # previewpath=request.POST['previewpath'],
                        authorinfo=request.POST['authorinfo'],
                        intro=request.POST['intro'],
                        index=request.POST['index'],
                        contents=request.POST['contents'],  # 소개글 제한?
                        reference=request.POST['reference'],
        )
        br.save()

        idx = uploadContents.objects.all().order_by('-pk')[0].contents_id     # ★



        listlength = len(ftpfilelist)

        for i in range(listlength):
            br = contentsInfo(
                               contents_id=idx,
                               uploadfilename=uifilelist[i],
                               ftpsavefilename=ftpfilelist[i],
                               contentspath=ftp_contents_dir,
                               hash=filehashdatas[i],
                               )
            br.save()

        url = '/unid/contentstran/'
        return HttpResponseRedirect(url)