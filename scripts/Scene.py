import GameObject


class Scene:
    def __init__(self):
        self.game_object = list()

    def add(self, game_object):
        self.game_object.append(game_object)

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

    return s
