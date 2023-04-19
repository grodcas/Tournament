from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import tournament

def index(request):
    Tournament=tournament.objects.all
    context={'Tournaments':Tournament}
    return render(request, 'tournaments/index.html' ,context)