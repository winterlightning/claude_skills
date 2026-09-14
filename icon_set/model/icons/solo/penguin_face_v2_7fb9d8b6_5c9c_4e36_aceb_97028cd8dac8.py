"""Square envelope; corrected the dome to exact quarter ellipses and moved the eyes inward symmetrically.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7fb9d8b6-5c9c-4e36-aceb-97028cd8dac8'
SOURCE_PATH = 'pictographic-primitives/animals/bird_7fb9d8b6-5c9c-4e36-aceb-97028cd8dac8.svg'
AUTHOR = 'gpt-6'

class PenguinFaceVariant2(Solo48):
    icon_id = 'penguin-face-v2'
    variant_of = 'penguin-face'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/animals'
    aliases = ()
    keywords = ('penguin', 'bird', 'face', 'head', 'beak', 'chick', 'animal', 'minimal')

    def build(self) -> None:
        self.add_line('shoulder-left', (6, 42), (8, 29))
        self.add_line('cheek-left', (8, 29), (8, 21))
        self.add_arc('dome-left', (8, 21), (24, 6), radius_x=16, radius_y=15, sweep=True)
        self.add_arc('dome-right', (24, 6), (40, 21), radius_x=16, radius_y=15, sweep=True)
        self.add_line('cheek-right', (40, 21), (40, 29))
        self.add_line('shoulder-right', (40, 29), (42, 42))
        self.add_contour('head', 'shoulder-left', 'cheek-left', 'dome-left', 'dome-right', 'cheek-right', 'shoulder-right', closed=False)
        self.add_line('eye-left', (17, 21), (17, 23))
        self.add_line('eye-right', (31, 21), (31, 23))
        self.add_line('beak-1', (19, 32), (24, 40))
        self.add_line('beak-2', (24, 40), (29, 32))
        self.add_contour('beak', 'beak-1', 'beak-2', closed=False)
