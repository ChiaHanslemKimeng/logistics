from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from django.shortcuts import redirect

urlpatterns = [
    # Login is handled via /admin/
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', lambda r: redirect('/admin/'), name='dashboard'),
]
