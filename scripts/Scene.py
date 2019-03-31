import GameObject


STATIC = 0
DYNAMIC = 1
ATTACK = 2
CLOSE = 3


class Scene:
    def __init__(self):
        self.game_static_object = list()
        self.game_dynamic_object = list()
        self.attack_object = list()
        self.close_attack = list()

    def add(self, game_object, type):
        if type == STATIC:
            self.game_static_object.append(game_object)
        elif type == DYNAMIC:
            self.game_dynamic_object.append(game_object)
        elif type == ATTACK:
            self.attack_object.append(game_object)
        elif type == CLOSE:
            self.close_attack.append(game_object)

    def setPlayer(self, player):
        self.player = player

    def delete(self):
        for i in self.game_object:
            i.delete()


def test_scene():
    s = Scene()

    player_pos = (200, 200)
    player_scale = (100, 100)
    player = GameObject.Player(player_pos, player_scale)
    s.setPlayer(player)

    ground_pos = (0, 200)
    ground_scale = (1000, 100)
    ground = GameObject.Ground(ground_pos, ground_scale)
    s.add(ground, STATIC)

    monster1_pos = (300, 200)
    monster1_scale = (250, 100)
    monster1 = GameObject.Monster1(monster1_pos, monster1_scale)
    s.add(monster1, DYNAMIC)

    return s
