from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^photo/list/$', views.photo, name='photo'),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'admin/login.html'}, name='login'),

    url(r'^accounts/logout/$', auth_views.logout,{'next_page': '/'}, name='logout'),
   
]

