"""Corrected keyshape selection to match the existing square proportions.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
Lucide cat: integrated pointed ears and tapered cheek outline.
"""
# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4d54d729-428a-4c82-8087-0f1d42f93c74'
SOURCE_PATH = 'pictographic-primitives/animals/fox_4d54d729-428a-4c82-8087-0f1d42f93c74.svg'
AUTHOR = 'gpt-6'

class FoxHead(Solo48):
    icon_id = 'fox-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('fox', 'head', 'face', 'ears', 'snout', 'animal', 'wildlife', 'canine')

    def build(self) -> None:
        self.add_arc('head-1', (24, 42), (17, 38), radius_x=10, radius_y=10, sweep=True)
        self.add_line('head-2', (17, 38), (6, 24))
        self.add_line('head-3', (6, 24), (7, 21))
        self.add_line('head-4', (7, 21), (6, 6))
        self.add_line('head-5', (6, 6), (17, 15))
        self.add_line('head-6', (17, 15), (31, 15))
        self.add_line('head-7', (31, 15), (42, 6))
        self.add_line('head-8', (42, 6), (41, 21))
        self.add_line('head-9', (41, 21), (42, 24))
        self.add_line('head-10', (42, 24), (31, 38))
        self.add_arc('head-11', (31, 38), (24, 42), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', 'head-3', 'head-4', 'head-5', 'head-6', 'head-7', 'head-8', 'head-9', 'head-10', 'head-11', closed=True)
        self.add_dot('nose', (24, 32))
