
from django.conf.urls import url
from django.contrib.auth.views import login

from ui import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.getMap, name='getMap'),
    
    # User's URL
    url(r'^login/$', login, {'template_name': 'account/login.html' }, name='user_login'),
    url(r'user_logout/$', views.user_logout, name='user_logout'),
    url(r'^register/$', views.register, name='register'),
    
    
    url(r'^map/get-term/', views.getTerm, name='getTerm'),
    url(r'^save_location/$', views.saveLocation, name='saveLocation' ),
    
    # Chat URL
    url(r'^chat-page/$', views.chat, name='chat'),
    url(r'^post-message/$', views.postMessage, name='postMessage'),
    url(r'^view-message/$', views.getMessage, name='getMessage'),

    
]
