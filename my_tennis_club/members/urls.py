from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('', views.members, name='members'),
    path('members', views.members, name='members'),
    path('details/<int:id>', views.details, name='details')

]