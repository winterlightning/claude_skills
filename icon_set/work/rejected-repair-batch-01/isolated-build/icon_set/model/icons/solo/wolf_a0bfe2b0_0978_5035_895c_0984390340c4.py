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
        self.add_arc('ruff', (8, 42), (20, 32), radius_x=22, radius_y=22, sweep=False)
        self.add_arc('lower-muzzle', (20, 32), (6, 31), radius_x=19, radius_y=19, sweep=True)
        self.add_arc('face', (6, 31), (21, 17), radius_x=65, radius_y=65, sweep=False)
        self.add_arc('brow', (21, 17), (30, 13), radius_x=12, radius_y=12, sweep=True)
        self.add_line('upper-muzzle', (30, 13), (40, 6))
        self.add_arc('nose', (40, 6), (41, 17), radius_x=14, radius_y=14, sweep=True)
        self.add_bezier('neck',(41,17),((42,20),(42,22),(42,24)),((42,27),(40,30),(38,33)))
        self.add_arc('chest', (38, 33), (33, 42), radius_x=20, radius_y=20, sweep=False)
        self.add_contour('outline', 'ruff', 'lower-muzzle', 'face', 'brow', 'upper-muzzle', 'nose', 'neck', 'chest', closed=False)
