from django.db import models
from django.contrib.auth.models import User

#definimos los estados del juego

GAME_STATES = (
    ('ACTIVE', 'Active'), #el juego esta activo
    ('WIN_P1', 'Player 1 won'), #gana el primer jugador
    ('WIN_P2', 'Player 2 won'), #gana el segundo jugador
    ('TIE', 'Tie'), #empate
)

class Game(models.Model):
    room_name = models.CharField(max_length=50, unique=True) #nombre unico
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player1_games') #jugador 1, obligatorio
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player2_games', null=True, blank=True) #jugador 2, opcinal, 
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #el owner de la partida
    board = models.CharField(max_length=9, default="_________") #tablero de juego
    active_player = models.IntegerField(default=1)  # jugador activo, por defecto jugador 1, 2 para jugador 2
    state = models.CharField(max_length=10, choices=GAME_STATES, default='ACTIVE') #estado de la partida, activa, tiene un ganador, hay empate

    def __str__(self):
        return f"{self.room_name} (Owner: {self.owner})"
