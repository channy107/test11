from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'unid/index.html', {})

def contentMain(request):
    return render(request, 'unid/contentMain.html', {})