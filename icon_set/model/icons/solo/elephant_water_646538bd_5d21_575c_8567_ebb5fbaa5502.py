"""Raised continuous trunk, broad ear and two water strokes; shared endpoints attach the back to the ear."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '646538bd-5d21-575c-8567-ebb5fbaa5502'
SOURCE_PATH = 'pictographic-primitives/animals/elephant water_646538bd-5d21-575c-8567-ebb5fbaa5502.svg'
AUTHOR = 'gpt-6'


class ElephantSprayingWater(Solo48):
    icon_id = 'elephant-spraying-water'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('elephant', 'spraying', 'water')

    def build(self) -> None:
        # SQUARE visible bounds (0, 0, 48, 48); centerlines (2, 2, 46, 46).
        self.add_arc('trunk-outer', (14, 12), (2, 28), radius_x=12, radius_y=16, sweep=False)
        self.add_arc('cheek', (2, 28), (12, 40), radius_x=10, radius_y=12, sweep=False)
        self.add_arc('neck', (12, 40), (18, 46), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('outside', 'trunk-outer', 'cheek', 'neck')
        self.add_arc('trunk-tip', (14, 12), (16, 18), radius_x=3, radius_y=4, sweep=True)
        self.add_arc('trunk-inside', (16, 18), (10, 26), radius_x=9, radius_y=10, sweep=False)
        self.add_arc('trunk-fold', (10, 26), (15, 29), radius_x=3, radius_y=3, sweep=False)
        self.add_arc('brow', (15, 29), (25, 27), radius_x=8, radius_y=6, sweep=True)
        self.add_arc('ear-top', (25, 27), (38, 33), radius_x=9, radius_y=9, sweep=True)
        self.add_contour('raised', 'trunk-tip', 'trunk-inside', 'trunk-fold', 'brow', 'ear-top')
        self.relate("connect", 'outside', 'raised')
        self.add_arc('ear-bottom', (38, 33), (27, 43), radius_x=11, radius_y=10, sweep=True)
        self.relate("connect", 'raised', 'ear-bottom')
        self.add_arc('back', (38, 33), (46, 41), radius_x=8, radius_y=8, sweep=True)
        self.add_line('rump', (46, 41), (46, 46))
        self.add_contour('body', 'back', 'rump')
        self.relate("connect", 'raised', 'body')
        self.relate("connect", 'ear-bottom', 'body')
        self.add_line('water-left', (23, 2), (20, 5))
        self.add_line('water-right', (34, 7), (38, 10))
