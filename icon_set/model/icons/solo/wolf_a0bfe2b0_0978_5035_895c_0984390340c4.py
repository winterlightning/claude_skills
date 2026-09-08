"""Howling wolf head and shoulders; long lifted muzzle, swept ear and open ruff. Sparse coherent curves preserve the asymmetric source silhouette."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0bfe2b0-0978-5035-895c-0984390340c4'
SOURCE_PATH = 'pictographic-primitives/animals/wolf_a0bfe2b0-0978-5035-895c-0984390340c4.svg'
AUTHOR = 'gpt-6'


class HowlingWolfProfile(Solo48):
    icon_id = 'howling-wolf-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('wolf', 'howl', 'profile', 'head', 'muzzle', 'night', 'canine', 'wild')

    def build(self) -> None:
        self.add_arc('ruff', (8, 46), (20, 32), radius_x=22, radius_y=22, sweep=False)
        self.add_arc('lower-muzzle', (20, 32), (2, 31), radius_x=19, radius_y=19, sweep=True)
        self.add_arc('face', (2, 31), (21, 17), radius_x=65, radius_y=65, sweep=False)
        self.add_arc('brow', (21, 17), (30, 13), radius_x=12, radius_y=12, sweep=True)
        self.add_line('upper-muzzle', (30, 13), (40, 2))
        self.add_arc('nose', (40, 2), (41, 17), radius_x=14, radius_y=14, sweep=True)
        self.add_line('ear-1', (41, 17), (39, 23))
        self.add_line('ear-2', (39, 23), (46, 20))
        self.add_arc('neck', (46, 20), (38, 33), radius_x=18, radius_y=18, sweep=True)
        self.add_arc('chest', (38, 33), (33, 46), radius_x=20, radius_y=20, sweep=False)
        self.add_contour('outline', 'ruff', 'lower-muzzle', 'face', 'brow', 'upper-muzzle', 'nose', 'ear-1', 'ear-2', 'neck', 'chest', closed=False)
