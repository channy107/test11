from _sha256 import sha256

from allauth.socialaccount.templatetags import socialaccount
from web3 import Web3, HTTPProvider
from django.shortcuts import render
import requests
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
# from unid.models import myPage
from unid.models import myPageInFomation
from web3.auto import w3


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
    return render(request, 'unid/createaccount.html', {})
#     if request.method == 'GET':
#         # email = json.loads(((response.text).encode('utf-8')))['email']
#         email = socialaccount.extra_data.email
#
#         try:
#              member = myPageInFomation.extra_data.objects.get(email=id)
#              request.session['user_id'] = member.email
#              request.session['user_name'] = member.name
#              request.session['user_account'] = member.account
#         except myPageInFomation.DoesNotExist:
#             return render(
#                 request,
#                 'unid/createaccount.html',
#                 {'id': id, 'nickname': nickname}
#             )
#         else:
#             # return HttpResponse(member)
#             url = 'http://localhost:8000/unid/mywallet'
#             return HttpResponseRedirect(url)
#
#     else:
#         time = timezone.now()
#         rpc_url = "http://localhost:8545"
#         w3 = Web3(HTTPProvider(rpc_url))
#         account = w3.personal.newAccount('pwd')
#         pwd = request.POST['pwd'].encode('utf-8')  # ★★★★
#         lockpwd = sha256(pwd)
#         br = myPageInFomation(email=request.POST['email'],
#                               name=request.POST['name'],
#                               joiningdate=timezone.now(),
#                               pwd=lockpwd,  # ★★★★
#                               account=account)
#         br.save()
#         url = 'http://localhost:8000/unid'
#         return HttpResponseRedirect(url)
#     return render(request, 'unid/createaccount.html', {})

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
             member = myPageInFomation.objects.get(email=id)
             request.session['user_id'] = member.email
             request.session['user_name'] = member.name
             request.session['user_account'] = member.account
        except myPageInFomation.DoesNotExist:
            return render(
                request,
                'unid/createaccount.html',
                {'id': id, 'nickname': nickname}
            )
        else:
            # return HttpResponse(member)
            url = 'http://localhost:8000/unid/mywallet'
            return HttpResponseRedirect(url)

    else:
        time = timezone.now()
        rpc_url = "http://localhost:8545"
        w3 = Web3(HTTPProvider(rpc_url))
        account = w3.personal.newAccount('pwd')
        pwd = request.POST['pwd'].encode('utf-8')  # ★★★★
        lockpwd = sha256(pwd)
        br = myPageInFomation(email=request.POST['email'],
                              name=request.POST['name'],
                              joiningdate=timezone.now(),
                              pwd=lockpwd,  # ★★★★
                              account=account)
        br.save()
        url = 'http://localhost:8000/unid'
        return HttpResponseRedirect(url)

def contentsupload(request):
    return render(request, 'unid/contentsupload.html', {})

def mypage(request):
    return render(request, 'unid/mypage.html', {})