import GameObject


class Scene:
    def __init__(self):
        self.game_object = list()

    def add(self, game_object):
        self.game_object.append(game_object)

    def delete(self):
        for i in self.game_object:
            i.delete()


def test_scene():
    s = Scene()

    p1_pos = (200, 200)
    p1_scale = (100, 100)
    p1 = GameObject.Player(p1_pos, p1_scale)
    s.add(p1)

    return s
