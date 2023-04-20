from django.urls import path
from . import views
app_name = 'tournaments'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:tournament_id>/', views.details, name='details'),
    path('<int:tournament_id>/<int:group_id>/', views.groups, name='details'),
    path('<int:tournament_id>/<int:group_id>/<int:match_id>', views.matches, name='details')
]