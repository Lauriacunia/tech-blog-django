from django.contrib import admin
from django.urls import path
from user.views import UpdateUser

urlpatterns = [
    path('/settings/<int:pk>', UpdateUser.as_view(), name='settings'),
]