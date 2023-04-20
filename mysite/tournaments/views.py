from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import tournament, pool
from .forms import SearchForm

def index(request):
    Tournament=tournament.objects.all
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            Tournament = tournament.objects.filter(name__contains=query)
        else:
            Tournament=tournament.objects.all
    else:
        search_form = SearchForm()
        Tournament=tournament.objects.all
    context={'Tournaments':Tournament,'form': search_form}
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

def matches(request,tournament_id, group_id, match_id):
    Tournament=get_object_or_404(tournament,pk=tournament_id)
    Pools=Tournament.pool_set.get(pk=group_id)
    Match=Pools.match_set.get(pk=match_id)
    context={'Match':Match, 'group_id':group_id, 'match_id': match_id}
    return render(request, 'tournaments/matches.html' ,context)
