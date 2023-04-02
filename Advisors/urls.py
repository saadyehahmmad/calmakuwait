from django.urls import path, include
from . import viewssss

urlpatterns = [
    path('Advisors/', viewssss.all_advisor),
    path('Advisors/<str:slug>/', viewssss.advisor),
]