from django.urls import path
from . import views
from django.urls import include
app_name = 'tournaments'
urlpatterns = [
    path('<int:tournament_id>/<int:group_id>/<int:match_id>/comment', views.comments, name='comments'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('', views.index, name='index'),
    path('<int:tournament_id>/', views.details, name='details1'),
    path('<int:tournament_id>/<int:group_id>/', views.groups, name='groups'),
    path('<int:tournament_id>/<int:group_id>/<int:match_id>', views.matches, name='matches')
]