from django.urls import path
from .views import cat_fact_view

urlpatterns = [
    path("cat-fact/", cat_fact_view, name="cat_fact"),
]
