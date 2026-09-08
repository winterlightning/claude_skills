"""Mirrored fox face with tall pointed ears and tapered muzzle; no eyes in source. Lucide cat informs integrated ear contour."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d54d729-428a-4c82-8087-0f1d42f93c74'
SOURCE_PATH = 'pictographic-primitives/animals/fox_4d54d729-428a-4c82-8087-0f1d42f93c74.svg'
AUTHOR = 'gpt-6'


class FoxHead(Solo48):
    icon_id = 'fox-head'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('fox', 'head', 'face', 'ears', 'snout', 'animal', 'wildlife', 'canine')

    def build(self) -> None:
        # Keyshape ink extremes: (0, 3, 48, 45); centerlines inset by stroke radius 2.
        self.add_arc('head-1', (24, 43), (17, 38), radius_x=10, radius_y=10, sweep=True)
        self.add_line('head-2', (17, 38), (2, 24))
        self.add_line('head-3', (2, 24), (7, 21))
        self.add_line('head-4', (7, 21), (6, 5))
        self.add_line('head-5', (6, 5), (17, 15))
        self.add_line('head-6', (17, 15), (31, 15))
        self.add_line('head-7', (31, 15), (42, 5))
        self.add_line('head-8', (42, 5), (41, 21))
        self.add_line('head-9', (41, 21), (46, 24))
        self.add_line('head-10', (46, 24), (31, 38))
        self.add_arc('head-11', (31, 38), (24, 43), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', 'head-3', 'head-4', 'head-5', 'head-6', 'head-7', 'head-8', 'head-9', 'head-10', 'head-11', closed=True)
        self.add_dot('nose', (24, 32))
