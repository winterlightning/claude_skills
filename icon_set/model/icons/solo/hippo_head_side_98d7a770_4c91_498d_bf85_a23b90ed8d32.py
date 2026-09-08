"""Hippo with widely open rising upper jaw and deep rounded lower jaw; reinterprets the ambiguous source through its diagonal jaw opening, without teeth."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '98d7a770-4c91-498d-bf85-a23b90ed8d32'
SOURCE_PATH = 'pictographic-primitives/animals/hippo head side_98d7a770-4c91-498d-bf85-a23b90ed8d32.svg'
AUTHOR = 'gpt-6'


class HippoHeadOpenMouth(Solo48):
    icon_id = 'hippo-head-open-mouth'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('hippo', 'hippopotamus', 'head', 'mouth', 'open', 'jaw', 'profile', 'animal')

    def build(self) -> None:
        # Keyshape ink extremes: (0, 3, 48, 45); centerlines inset by stroke radius 2.
        self.add_line('head-1', (2, 33), (11, 22))
        self.add_line('head-2', (11, 22), (10, 22))
        self.add_arc('head-3', (10, 22), (7, 19), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-4', (7, 19), (10, 16), radius_x=3, radius_y=3, sweep=True)
        self.add_line('head-5', (10, 16), (14, 17))
        self.add_line('head-6', (14, 17), (26, 5))
        self.add_line('head-7', (26, 5), (32, 5))
        self.add_line('head-8', (32, 5), (39, 11))
        self.add_line('head-9', (39, 11), (29, 21))
        self.add_arc('head-10', (29, 21), (27, 27), radius_x=10, radius_y=10, sweep=False)
        self.add_arc('head-11', (27, 27), (30, 35), radius_x=12, radius_y=12, sweep=False)
        self.add_arc('head-12', (30, 35), (37, 38), radius_x=10, radius_y=10, sweep=False)
        self.add_line('head-13', (37, 38), (46, 38))
        self.add_line('head-14', (46, 38), (46, 32))
        self.add_contour('head', 'head-1', 'head-2', 'head-3', 'head-4', 'head-5', 'head-6', 'head-7', 'head-8', 'head-9', 'head-10', 'head-11', 'head-12', 'head-13', 'head-14', closed=False)
        self.add_arc('lower-jaw-1', (46, 38), (41, 43), radius_x=5, radius_y=5, sweep=True)
        self.add_line('lower-jaw-2', (41, 43), (25, 41))
        self.add_line('lower-jaw-3', (25, 41), (22, 43))
        self.add_contour('lower-jaw', 'lower-jaw-1', 'lower-jaw-2', 'lower-jaw-3', closed=False)
        self.relate("connect", 'head', 'lower-jaw')
