from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time


G_UP = 0
G_DOWN = 1


class GameObject:
    def __init__(self, pos, scale):
        self.isMoving = False
        self.direction = 0
        self.isJumping = False
        self.isSquatting = False
        self.speed = 0
        self.x, self.y = pos
        self.width, self.height = scale

    def create(self, w):
        pass


class Player(GameObject):
    def __init__(self, pos, scale):
        super().__init__(pos, scale)

        self.jump_status = G_UP
        self.y_origin = 200
        self.jump_height = 150
        self.jump_speed = 200
        self.speed = 200
        self.img_interval = 0.2
        self.img_timerecorder = 0

        self.img_player1 = QPixmap('../src/player1.png')
        self.img_player2 = QPixmap('../src/player2.png')
        self.img_player_r1 = QPixmap('../src/player_r1.png')
        self.img_player_r2 = QPixmap('../src/player_r2.png')
        self.img_player_squat = QPixmap('../src/player_squat.png')
        self.img_player_squat_r = QPixmap('../src/player_squat_r.png')
        self.img = self.img_player1
        self.img_index = 0

    def draw(self, painter):
        painter.drawPixmap(self.x, self.y, self.width, self.height, self.img)

    def walk(self, pos):
        self.x, self.y = pos
        t = time.time() - self.img_timerecorder

        if t > self.img_interval:
            if self.direction == Qt.Key_Right:
                if self.img_index != 2:
                    self.img = self.img_player2
                    self.img_index = 2
                elif self.img_index != 1:
                    self.img = self.img_player1
                    self.img_index = 1

            elif self.direction == Qt.Key_Left:
                if self.img_index != 4:
                    self.img = self.img_player_r2
                    self.img_index = 4
                elif self.img_index != 3:
                    self.img = self.img_player_r1
                    self.img_index = 3
            self.img_timerecorder = time.time()

    def jump(self, num):
        if self.y > self.y_origin and self.jump_status == G_DOWN:
            self.isJumping = False
            self.y = self.y_origin
            self.jump_status = G_UP

        if self.y < self.jump_height:
            self.jump_status = G_DOWN

        if self.jump_status == G_UP:
            self.y -= num
        elif self.jump_status == G_DOWN:
            self.y += num

    def squat(self):
        if self.direction == Qt.Key_Right:
            self.img = self.img_player_squat
        elif self.direction == Qt.Key_Left:
            self.img = self.img_player_squat_r

    def init_img(self):
        if self.direction == Qt.Key_Right:
            self.img = self.img_player1
        elif self.direction == Qt.Key_Left:
            self.img = self.img_player_r1
