from django.shortcuts import render
import requests
import json
from django.http import HttpResponse
from unid.models import myPage


def mywallet(request):
    return render(request, 'unid/mywallet.html', {})

def oauth(request):
    code = request.GET.get('code')
    url = "https://kauth.kakao.com/oauth/token"
    payload = "grant_type=authorization_code&client_id=122f531f95d70dabb69ff17f4f1b0be2&redirect_uri=http://localhost:8000/unid/oauth&code=" + str(code)
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
    id = json.loads(((response.text).encode('utf-8')))['id']
    br = myPage(email=str(id))
    br.save()
    return HttpResponse(id)

def contentsdetail(request):
    return render(request, 'unid/contentsdetail.html', {})

def contentstran(request):
    return render(request, 'unid/contentstran.html', {})

def main(request):
    return render(request, 'unid/main.html', {})

def login(request):
    return render(request, 'unid/login.html', {})
