from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list_view, name='games_list'),
    path('new/', views.game_new_view, name='game_new'),
    path('<int:game_id>/', views.game_detail_view, name='game_detail'),
    path('<int:game_id>/join/', views.game_join_view, name='game_join'),
    path('<int:game_id>/delete/', views.game_delete_view, name='game_delete'),
]
