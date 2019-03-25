from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time


J_UP = 0
J_DOWN = 1


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

        self.isJumping = False
        self.jump_status = J_UP
        self.y_origin = 200
        self.jump_height = 150
        self.jump_speed = 200

        self.speed = 100
        self.img_interval = 0.2
        self.img_timerecorder = 0

    def create(self, w):
        self.img_player1 = QPixmap('../src/player1.png')
        self.img_player2 = QPixmap('../src/player2.png')
        self.img_player_r1 = QPixmap('../src/player_r1.png')
        self.img_player_r2 = QPixmap('../src/player_r2.png')

        self.label = QLabel(w)
        self.label.setGeometry(self.x, self.y, self.width, self.height)
        self.label.setPixmap(self.img_player1)
        self.img_index = 1

    def move(self, pos, direction):
        self.x, self.y = pos
        self.label.move(pos[0], pos[1])

        if time.time() - self.img_timerecorder > self.img_interval:
            if direction == 'r':
                if self.img_index != 2:
                    self.label.setPixmap(self.img_player2)
                    self.img_index = 2
                elif self.img_index != 1:
                    self.label.setPixmap(self.img_player1)
                    self.img_index = 1

            elif direction == 'l':
                if self.img_index != 4:
                    self.label.setPixmap(self.img_player_r2)
                    self.img_index = 4
                elif self.img_index != 3:
                    self.label.setPixmap(self.img_player_r1)
                    self.img_index = 3
            self.img_timerecorder = time.time()

    def jump(self, num):
        if self.y > self.y_origin and self.jump_status == J_DOWN:
            self.isJumping = False
            self.y = self.y_origin
            self.jump_status = J_UP

        if self.y < self.jump_height:
            self.jump_status = J_DOWN

        if self.jump_status == J_UP:
            self.y -= num
            self.label.move(self.x, self.y)
        elif self.jump_status == J_DOWN:
            self.y += num
            self.label.move(self.x, self.y)

    def delete(self):
        self.label.deleteLater()
