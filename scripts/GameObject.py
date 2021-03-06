from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import Scene as sc


G_UP = 0
G_DOWN = 1
G_GOOD = 2
G_BAD = 3


class GameObject:
    def __init__(self, pos, scale):
        self.x, self.y = pos
        self.width, self.height = scale

    def draw(self, painter):
        # painter.drawRect(self.x, self.y, self.width, self.height)
        painter.drawPixmap(self.x, self.y, self.width, self.height, self.img)


class Ground(GameObject):
    def __init__(self, pos, scale):
        super().__init__(pos, scale)
        self.img = QPixmap('../src/ground.png')


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


class CloseAttack(GameObject):
    def __init__(self, pos, scale, camp):
        super().__init__(pos, scale)
        self.camp = camp


class DynamicGameObject(GameObject):
    def __init__(self, pos, scale):
        super().__init__(pos, scale)

        self.isMoving = False
        self.direction = Qt.Key_Right
        self.isJumping = False
        self.isNormalAttacking = False
        self.NormalAttackTrigger = False

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

    def normal_attack(self, scene, camp):
        if self.direction == Qt.Key_Right:
            self.img = self.img_attack
            self.temp_attack = CloseAttack((self.x + 100, self.y + 30), (30, 30), camp)
        elif self.direction == Qt.Key_Left:
            self.img = self.img_attack_r
            self.temp_attack = CloseAttack((self.x - 30, self.y + 30), (30, 30), camp)

        scene.add(self.temp_attack, sc.CLOSE)


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
        self.img_attack = QPixmap('../src/player_attack.png')
        self.img_attack_r = QPixmap('../src/player_attack_r.png')
        self.img = self.img_1

    def squat(self):
        self.height = 70
        self.y = 230
        if self.direction == Qt.Key_Right:
            self.img = self.img_squat
        elif self.direction == Qt.Key_Left:
            self.img = self.img_squat_r

    def init_img(self):
        if self.width == 130 and self.direction == Qt.Key_Left:
            self.x += 30
        self.width, self.height = 100, 100
        self.y = 200
        if self.direction == Qt.Key_Right:
            self.img = self.img_1
        elif self.direction == Qt.Key_Left:
            self.img = self.img_r1

    def normal_attack(self, s):
        if self.direction == Qt.Key_Right:
            self.width = 130
        elif self.direction == Qt.Key_Left:
            self.width = 130
            self.x -= 30
        super().normal_attack(s, G_GOOD)


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
        # if (self.x - s.player.x) < (50 + s.player.width) and self.x > s.player.x:
        #     self.direction = Qt.Key_Right
        #     self.move((self.x + interval * self.speed, self.y))
        # elif (s.player.x - self.x) < (50 + self.width) and s.player.x > self.x:
        #     self.direction = Qt.Key_Left
        #     self.move((self.x - interval * self.speed, self.y))
        pass
