from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import tournament, pool

def index(request):
    Tournament=tournament.objects.all
    context={'Tournaments':Tournament}
    return render(request, 'tournaments/index.html' ,context)

def details(request,tournament_id):
    Tournament=get_object_or_404(tournament,pk=tournament_id)
    Pools=Tournament.pool_set.all
    context={'Tournament':Pools}
    return render(request, 'tournaments/details.html' ,context)

def groups(request,tournament_id, group_id):
    Tournament=get_object_or_404(tournament,pk=tournament_id)
    Pools=Tournament.pool_set.get(pk=group_id)
    Matches=Pools.match_set.all
    context={'Matches':Matches, 'group_id':group_id}
    return render(request, 'tournaments/groups.html' ,context)

