from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock_selection, name='stock_selection')
]
