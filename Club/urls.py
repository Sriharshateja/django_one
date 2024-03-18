from django import urls
from . import views
from django.urls import path


urlpatterns = [
    path("view/", views.ClubView.as_view() , name="view"),
]

