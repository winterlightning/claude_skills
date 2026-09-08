"""Minimal wolf head with one pointed ear, blunt muzzle and dot eye. Open throat and upright nape retain the source posture."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5980d529-a023-5a54-8f17-b3538741399a'
SOURCE_PATH = 'pictographic-primitives/animals/wolf_5980d529-a023-5a54-8f17-b3538741399a.svg'
AUTHOR = 'gpt-6'


class WolfHead(Solo48):
    icon_id = 'wolf-head'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('wolf', 'head', 'profile', 'minimal', 'snout', 'ear', 'canine', 'dog')

    def build(self) -> None:
        self.add_line('nape', (5, 40), (5, 25))
        self.add_arc('skull', (5, 25), (17, 7), radius_x=20, radius_y=20, sweep=True)
        self.add_line('ear-1', (17, 7), (24, 2))
        self.add_line('ear-2', (24, 2), (24, 12))
        self.add_arc('brow', (24, 12), (34, 20), radius_x=11, radius_y=11, sweep=True)
        self.add_line('muzzle', (34, 20), (43, 20))
        self.add_line('nose-front', (43, 20), (43, 24))
        self.add_arc('nose', (43, 24), (35, 32), radius_x=8, radius_y=8, sweep=True)
        self.add_line('jaw', (35, 32), (29, 32))
        self.add_arc('throat', (29, 32), (21, 40), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('chest', (21, 40), (24, 46), radius_x=10, radius_y=10, sweep=False)
        self.add_contour('outline', 'nape', 'skull', 'ear-1', 'ear-2', 'brow', 'muzzle', 'nose-front', 'nose', 'jaw', 'throat', 'chest', closed=False)
        self.add_dot('eye', (23, 23))
