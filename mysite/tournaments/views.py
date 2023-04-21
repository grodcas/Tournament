from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import tournament, pool, comment, match
from .forms import SearchForm, RegistrationForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.utils import timezone

def sign_up(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('tournaments:index')
    else:
        form=RegistrationForm()
        print("hola")
    return render(request,'tournaments/register.html',{"form":form})

def index(request):
    if request.user.is_authenticated:
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
    else:
        context={'Tournaments':None,'form': SearchForm()}
    return render(request, 'tournaments/index.html',context)

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
    Comments=Match.comment_set.all
    context={'Match':Match, 'group_id':group_id, 'match_id': match_id, 'Comments':Comments}
    return render(request, 'tournaments/matches.html' ,context)
    
@login_required
def comments(request,tournament_id, group_id, match_id):    
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                content = comment_form.cleaned_data['content']
                Comment = comment(author=request.user.username, date=timezone.now(), content=content, match=get_object_or_404(match,pk=match_id))
                Comment.save()
                return redirect('tournaments:matches',tournament_id,group_id,match_id)
            else:
                Comment= comment(author=None, date=None, content=None)
        else:   
                Comment= comment(author=None, date=None, content=None)

        context={'Comment':Comment, 'form':comment_form, 'tour':tournament_id, 'group':group_id, 'match':match_id }
        return render(request, 'tournaments/comments.html',context)
