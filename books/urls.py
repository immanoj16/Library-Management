from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'books'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.register, name='register'),
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^addbook/', views.addbook, name='addbook'),
    url(r'^removebook', views.removeBook, name='removebook'),
    url(r'^search/$', views.search, name='search'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^adduser/', views.adduser, name='adduser'),
]