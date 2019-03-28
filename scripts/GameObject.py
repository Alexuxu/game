from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time


G_UP = 0
G_DOWN = 1


class GameObject:
    def __init__(self, pos, scale):
        self.x, self.y = pos
        self.width, self.height = scale

    def draw(self, painter):
        painter.drawPixmap(self.x, self.y, self.width, self.height, self.img)


class Ground(GameObject):
    def __init__(self, pos, scale):
        super().__init__(pos, scale)
        self.img = QPixmap('../src/ground.png')


class DynamicGameObject(GameObject):
    def __init__(self, pos, scale):
        super().__init__(pos, scale)

        self.isMoving = False
        self.direction = Qt.Key_Right
        self.isJumping = False
        self.isAttack = False

        self.jump_status = G_UP
        self.y_origin = 200
        self.jump_height = 150
        self.jump_speed = 200
        self.speed = 200

        self.img_interval = 0.2
        self.img_timerecorder = 0
        self.img_index = 0

    def move(self, pos):
        if pos[0] > (1000 - self.width) or pos[0] < 0:
            return
        self.x, self.y = pos
        t = time.time() - self.img_timerecorder

        if t > self.img_interval:
            if self.direction == Qt.Key_Right:
                if self.img_index != 2:
                    self.img = self.img_2
                    self.img_index = 2
                elif self.img_index != 1:
                    self.img = self.img_1
                    self.img_index = 1

            elif self.direction == Qt.Key_Left:
                if self.img_index != 4:
                    self.img = self.img_r2
                    self.img_index = 4
                elif self.img_index != 3:
                    self.img = self.img_r1
                    self.img_index = 3
            self.img_timerecorder = time.time()

    def jump(self, delta):
        if self.y > self.y_origin and self.jump_status == G_DOWN:
            self.isJumping = False
            self.y = self.y_origin
            self.jump_status = G_UP

        if self.y < self.jump_height:
            self.jump_status = G_DOWN

        if self.jump_status == G_UP:
            self.y -= delta
        elif self.jump_status == G_DOWN:
            self.y += delta


class Player(DynamicGameObject):
    def __init__(self, pos, scale):
        super().__init__(pos, scale)

        self.isSquatting = False

        self.img_1 = QPixmap('../src/player1.png')
        self.img_2 = QPixmap('../src/player2.png')
        self.img_r1 = QPixmap('../src/player_r1.png')
        self.img_r2 = QPixmap('../src/player_r2.png')
        self.img_squat = QPixmap('../src/player_squat.png')
        self.img_squat_r = QPixmap('../src/player_squat_r.png')
        self.img = self.img_1

    def squat(self):
        self.height = 70
        self.y = 230
        if self.direction == Qt.Key_Right:
            self.img = self.img_squat
        elif self.direction == Qt.Key_Left:
            self.img = self.img_squat_r

    def init_img(self):
        self.height = 100
        self.y = 200
        if self.direction == Qt.Key_Right:
            self.img = self.img_1
        elif self.direction == Qt.Key_Left:
            self.img = self.img_r1


class Monster1(DynamicGameObject):
    def __init__(self, pos, scale):
        super().__init__(pos, scale)

        self.speed = 50

        self.img_1 = QPixmap('../src/dragon_1')
        self.img_2 = QPixmap('../src/dragon_2')
        self.img_r1 = QPixmap('../src/dragon_r1')
        self.img_r2 = QPixmap('../src/dragon_r2')
        self.img = self.img_1

    def logic(self, s, interval):
            if (self.x - s.player.x) < (50 + s.player.width) and self.x > s.player.x:
                self.direction = Qt.Key_Right
                self.move((self.x + interval * self.speed, self.y))
            elif (s.player.x - self.x) < (50 + self.width) and s.player.x > self.x:
                self.direction = Qt.Key_Left
                self.move((self.x - interval * self.speed, self.y))


class AttackObject(GameObject):
    def __init__(self, pos, scale):
        super().__init__(pos, scale)
        self.speed = 0

    def move(self, pos):
        if pos[0] > 1000 or pos[0] < 0 or pos[1] > 500 or pos[1] < 0:
            return
        self.x, self.y = pos

    def logic(self, interval):
        pass
