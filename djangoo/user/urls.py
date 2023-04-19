from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.User_interface, name="userinterface"),
    path('userregister', views.User_register, name="userregister"),
    path('usersignin', views.User_signin, name='usersignin'),
    path('index', views.User_index, name='userindex'),
    # re_path(r'^admin_current_models$', views.admin_current_models, name='admin_current_models'),
    # # re_path(r'^delete/(?P<id>\d+)$', views.delete,name="delete"),


]

