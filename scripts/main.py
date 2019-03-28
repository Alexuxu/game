from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time
import threading
import GameObject as go
import Scene as sc


WIDTH = 1000
HEIGHT = 500


class GameMain(threading.Thread):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.time_recorder = time.time()
        self.interval_threshold = 0.016

    def run(self):
        while True:
            time.sleep(0.01)
            interval = time.time() - self.time_recorder
            if interval > self.interval_threshold:
                self.change_status(interval)
                self.AI(interval)
                self.init_attack()

                self.window.update()
                self.time_recorder = time.time()

    def change_status(self, interval):
        p = self.window.scene.player
        if p.isSquatting:
            p.squat()
            return

        if p.isMoving:
            if p.direction == Qt.Key_Right:
                p.move((p.x + p.speed * interval, p.y))
            elif p.direction == Qt.Key_Left:
                p.move((p.x - p.speed * interval, p.y))

        if p.isJumping:
            p.jump(interval * p.jump_speed)

        if p.isAttack:
            p.attack(self.window.scene)

    def AI(self, interval):
        s = self.window.scene
        for object in s.game_dynamic_object:
            object.logic(s, interval)
        for object in s.attack_object:
            object.logic(interval)

    def collide(self):
        pass

    def init_attack(self):
        pass


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 200, WIDTH, HEIGHT)
        self.init_scene()
        self.show()

    def init_scene(self):
        self.scene = sc.test_scene()

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)

        # draw the main player
        self.scene.player.draw(painter)
        # draw the rest of game object
        for object in self.scene.game_static_object:
            object.draw(painter)
        for object in self.scene.game_dynamic_object:
            object.draw(painter)
        for object in self.scene.attack_object:
            object.draw(painter)

        painter.end()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Left or e.key() == Qt.Key_Right:
            self.scene.player.isMoving = True
            self.scene.player.direction = e.key()

        if e.key() == Qt.Key_Up:
            self.scene.player.isJumping = True

        if e.key() == Qt.Key_Down:
            if not self.scene.player.isJumping:
                self.scene.player.isSquatting = True

    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key_Left or e.key() == Qt.Key_Right:
            self.scene.player.isMoving = False

        if e.key() == Qt.Key_Down:
            self.scene.player.isSquatting = False
            self.scene.player.init_img()


if __name__ == "__main__":
    # create app
    app = QApplication(sys.argv)

    # create main window and main game thread
    main_window = MainWindow()
    game_thread = GameMain(main_window)
    game_thread.start()

    # main thread loop
    sys.exit(app.exec_())
