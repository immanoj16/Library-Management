from django.conf.urls import url

from . import views

app_name = 'books'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^addbook', views.addbook, name='addbook'),
    url(r'^removebook', views.removeBook, name='removebook'),
    url(r'^search/$', views.search, name='search'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^edit/$', views.edit, name='edit'),
]