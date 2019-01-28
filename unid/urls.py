from django.conf.urls import url
from django.contrib import admin
from django.urls import path


from .views import *





urlpatterns = [
    path('mywallet/', mywallet,),
    path('', main, name='main'),
    path('info_popular/', info_popular, name='info_popular'),
    path('main_upload/', main_upload, name='main_upload'),
    path('main_detail/<int:id>', main_detail, name='main_detail'),
    path('contentsdetail/<int:id>', contentsdetail, name='contentsdetail'),
    path('contentstran/', contentstran, name='contentstran'),
    path('oauth', oauth, name='oauth'),
    path('login/', login, name='login'),
    path('transaction/', transaction),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('createaccount/', createaccount, name='createaccount'),
    path('contentsupload/', contentsupload, name='contentsupload'),
    path('mypage/', mypage, name='mypage'),
    path('contentsboard/', contentsboard,   name='contentsboard'),
    path('searchcontents/<str:category>', searchcontents, name='searchcontents'),
    path('moneytrade/', moneytrade, name='moneytrade'),
    path('download/', download, name='download'),
    path('writereply/', writereply, name='writereply'),
    path('mainreply/', mainreply, name='maineply'),
    path('voting/', voting, name='voting'),
    path('vote/', vote, name='vote'),
]
