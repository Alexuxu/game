from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time


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
        self.img_interval = 0.2
        self.img_timerecorder = 0

    def create(self, w):
        self.img_player1 = QPixmap('../src/player1.png')
        self.img_player2 = QPixmap('../src/player2.png')

        self.label = QLabel(w)
        self.label.setGeometry(self.x, self.y, self.width, self.height)
        self.label.setPixmap(self.img_player1)
        self.img_index = 1

    def move(self, pos):
        self.x, self.y = pos
        self.label.move(pos[0], pos[1])

        if time.time() - self.img_timerecorder > self.img_interval:
            if self.img_index == 1:
                self.label.setPixmap(self.img_player2)
                self.img_index = 2
            elif self.img_index == 2:
                self.label.setPixmap(self.img_player1)
                self.img_index = 1
            self.img_timerecorder = time.time()


    def delete(self):
        self.label.deleteLater()
