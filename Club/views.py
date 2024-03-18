from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Club, Player








class ClubView(ListView):

    model = Club
    template_name = "club/listview.html"
    context_object_name = "view"




# Create your views here.
