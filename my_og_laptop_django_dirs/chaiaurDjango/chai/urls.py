
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_chai, name='all_chai_home'),
    path('order/', views.order, name='all_chai_order'), # localhost:8000/chai/order
    
]