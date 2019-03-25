from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time
import GameObject as go
import Scene as sc


class ThreadAnimate(QThread):
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.time_recorder = time.time()
        self.update_v = 0.01

    def run(self):
        while True:
            interval = time.time()-self.time_recorder
            if interval > self.update_v:
                self.move(interval)
                self.time_recorder = time.time()
                # self.collide()

    def move(self, interval):
        for i in self.w.s.game_object:
            if i.isJumping:
                i.jump(interval * i.jump_speed)

            if i.isMoving:
                if i.direction == Qt.Key_Left:
                    i.move((i.x - interval * i.speed, i.y), 'l')
                if i.direction == Qt.Key_Right:
                    i.move((i.x + interval * i.speed, i.y), 'r')


class ThreadUpdate(QThread):
    def __init__(self, w):
        super().__init__()
        self.w = w

    def run(self):
        while True:
            self.w.update()
            time.sleep(0.01)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(400, 200, 1000, 500)
        self.setWindowTitle("我也不知道叫啥的小游戏")

        self.load_scene()
        self.show()

    def load_scene(self):
        self.s = sc.test_scene()

        for object in self.s.game_object:
            object.create(self)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Right or e.key() == Qt.Key_Left:
            if not self.s.game_object[0].isJumping:
                self.s.game_object[0].isMoving = True
                self.s.game_object[0].timerecorder = time.time()
                self.s.game_object[0].direction = e.key()

        if e.key() == Qt.Key_Space:
            self.s.game_object[0].isJumping = True

    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key_Right or e.key() == Qt.Key_Left:
            if self.s.game_object[0].direction == e.key():
                self.s.game_object[0].isMoving = False
                self.s.game_object[0].timerecorder = 0
                self.s.game_object[0].direction = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    t_update = ThreadUpdate(w)
    t_animate = ThreadAnimate(w)
    t_update.start()
    t_animate.start()
    sys.exit(app.exec_())
