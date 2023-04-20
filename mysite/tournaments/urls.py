from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:tournament_id>/', views.details, name='details'),
    path('<int:tournament_id>/<int:group_id>/', views.groups, name='details')
]