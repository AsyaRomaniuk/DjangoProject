from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("about", views.about),
    path("dev-projects", views.devProjects),
    path("traitors-list", views.traitorsList),
    path("sign-in", views.signIn),
    path("sign-up", views.signUp),
]
# 33