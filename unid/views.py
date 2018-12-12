from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'unid/index.html', {})

def contentmain(request):
    return render(request, 'unid/contentmain.html', {})

def mywallet(request):
    return render(request, 'unid/mywallet.html', {})