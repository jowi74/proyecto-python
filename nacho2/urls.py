from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list_view, name='products_list'),
    path('', views.apppage, name='apppage'),
    path('<slug:slug>', views.person_detail, name='person_detail'),
]
