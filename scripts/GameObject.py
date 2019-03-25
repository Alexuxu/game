from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class GameObject:
    def __init__(self, pos, scale):
        self.isMoving = False
        self.direction = 0
        self.speed = 0
        self.x, self.y = pos
        self.width, self.height = scale

    def create(self, w):
        pass


class Player(GameObject):
    def __init__(self, pos, scale):
        super().__init__(pos, scale)
        self.speed = 100

    def create(self, w):
        img_player1 = QPixmap('../src/player1.png')
        img_player2 = QPixmap('../src/player2.png')

        self.label = QLabel(w)
        self.label.setGeometry(self.x, self.y, self.width, self.height)
        self.label.setPixmap(img_player1)

    def move(self, pos):
        self.x, self.y = pos
        self.label.move(pos[0], pos[1])

    def delete(self):
        self.label.deleteLater()
