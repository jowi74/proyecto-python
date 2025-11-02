from django.urls import path
from . import views
urlpatterns = [
    path('', views.apppage, name='apppage'),
    path('<slug:slug>/', views.person_detail, name='person_detail'),
]