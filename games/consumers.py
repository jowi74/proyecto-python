import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import Game
from asgiref.sync import sync_to_async

class GameConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"] #obtiene el room_id desde la url del websocket
        self.group_name = f"game_{self.room_id}" #creamos un nombre del grupo unico para la partida

        await self.channel_layer.group_add( #se unen al grupo del canal para que los jugadores recivan los mensajes
            self.group_name,
            self.channel_name
        )

        await self.accept() #se acepta la conexion al websocket

    async def disconnect(self, close_code): #cuando el usuario cierra la conexion se sale del grupo
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data) #convertimos el json a python
        position = data.get("position") # es la casilla que el jugador quiere marcar
        username = data.get("username") #el nombre del jugador

        game = await sync_to_async(Game.objects.select_related("player1", "player2").get)(id=self.room_id) #obtenemos el juego y al usuario
        user = await sync_to_async(User.objects.get)(username=username)

        player1 = game.player1
        player2 = game.player2

    #se verifica el turno del jugador
        if (game.active_player == 1 and user != game.player1) or \
           (game.active_player == 2 and user != game.player2):
            return

        board = list(game.board) #se convierte el tablero de juego en una lista

        if board[position] == "_": #verifica si la casilla esta vacia
            if game.active_player == 1:
                board[position] = "X"
                game.active_player = 2 #si jugador 1 X se cambia a jugador 2
            else:
                board[position] = "O"
                game.active_player = 1 #si jugador 2 marca O se cambia a jugador 1

        board_str = "".join(board) #se guarda el tablero en un string
        game.board = board_str

        result = self.check_winner(board) #se verifica si hay un ganador y hay un empate

        if result == "X":
            game.state = "WIN_P1"
        elif result == "O":
            game.state = "WIN_P2"
        elif result == "TIE":
            game.state = "TIE"

        await sync_to_async(game.save)() #se guardan los cambios en la base de datos

        await self.channel_layer.group_send( #se actualiza la informacion a todos los jugadores de la partida
            self.group_name,
            {
                "type": "send_update",
                "data": {
                    "board": board_str,
                    "state": game.state,
                    "active_player": game.active_player,
                }
            }
        )

    async def send_update(self, event):
        await self.send(text_data=json.dumps({
            "game_data": event["data"]
        }))

    def check_winner(self, board): #revisa las combinaciones ganadoras
        win_positions = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]

        for a, b, c in win_positions: #revisa si alguna de estas combinaciones tienen el mismo simbolo X , O
            if board[a] == board[b] == board[c] and board[a] != "_":
                return board[a]


        if "_" not in board: #si no hay, sale empate
            return "TIE"
        
    
        return None
