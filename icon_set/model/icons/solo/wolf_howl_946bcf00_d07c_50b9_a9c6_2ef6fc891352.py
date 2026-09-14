"""Howling wolf head with two radiating sound arcs. Separately composed to leave clear space around the signals."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '946bcf00-d07c-50b9-a9c6-2ef6fc891352'
SOURCE_PATH = 'pictographic-primitives/animals/wolf howl_946bcf00-d07c-50b9-a9c6-2ef6fc891352.svg'
AUTHOR = 'gpt-6'


class HowlingWolfWithSound(Solo48):
    icon_id = 'howling-wolf-with-sound'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('wolf', 'howl', 'sound', 'arcs', 'head', 'noise', 'canine', 'night')

    def build(self) -> None:
        self.add_line('ruff', (6, 42), (10, 31))
        self.add_arc('jaw', (10, 31), (6, 30), radius_x=10, radius_y=10, sweep=True)
        self.add_line('face', (6, 30), (16, 15))
        self.add_line('muzzle-1', (16, 15), (23, 11))
        self.add_line('muzzle-2', (23, 11), (25, 23))
        self.add_line('muzzle-3', (25, 23), (29, 20))
        self.add_arc('neck', (29, 20), (25, 32), radius_x=17, radius_y=17, sweep=True)
        self.add_arc('chest', (25, 32), (29, 42), radius_x=16, radius_y=16, sweep=False)
        self.add_contour('outline', 'ruff', 'jaw', 'face', 'muzzle-1', 'muzzle-2', 'muzzle-3', 'neck', 'chest', closed=False)
        self.add_bezier('sound-outer', (34, 6), *(((39.15470054, 9.21195379), (42, 14.92992149), (42, 21)),))
