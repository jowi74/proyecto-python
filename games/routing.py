from django.urls import re_path
from .consumers import GameConsumer

websocket_urlpatterns = [ #se define la ruta para websocket que incluye un room_id dinamico
    re_path(r"ws/tictactoe/(?P<room_id>\w+)/$", GameConsumer.as_asgi()),
]
