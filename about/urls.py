from django.contrib import admin
from django.urls import path
from about.views import showAboutMe, showAboutProject

urlpatterns = [
    path('/me', showAboutMe, name='about_me'),
    path('/project', showAboutProject, name='about_project'),
]