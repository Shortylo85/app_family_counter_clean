
from django.conf.urls import url
from django.contrib.auth.views import login

from ui import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.getMap, name='getMap'),
    url(r'^map1/$', views.getMap1, name='getMap1'),
    
    # User's URL
    url(r'^login/$', login, {'template_name': 'account/login.html' }, name='user_login'),
    url(r'user_logout/$', views.user_logout, name='user_logout'),
    url(r'^register/$', views.register, name='register'),
    
    
    url(r'^map/get-term/', views.getTerm, name='getTerm'),
    url(r'^tree/$', views.showTree, name='showTree'),
    url(r'^save_location/$', views.saveLocation, name='saveLocation' ),
    url(r'^save_location_1/$', views.saveLocation1, name='saveLocation1' ),
    url(r'^family-form/$', views.getFamilyForm, name='getfamilyForm'),
    url(r'^post-family-form/$', views.postFamilyForm, name='postFamilyForm'),

    

    
    # Chat URL
    url(r'^chat-page/$', views.chat, name='chat'),
    url(r'^post-message/$', views.postMessage, name='postMessage'),
    url(r'^view-message/$', views.getMessage, name='getMessage'),

    
]
