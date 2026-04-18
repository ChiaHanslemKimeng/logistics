from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_shipment, name='create_shipment'),
    path('update/<int:pk>/', views.update_shipment, name='update_shipment'),
]
