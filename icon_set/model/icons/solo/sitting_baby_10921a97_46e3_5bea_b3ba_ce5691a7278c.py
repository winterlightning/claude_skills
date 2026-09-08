"""A seated infant with a large head, rounded arms, diaper and wide oval feet. Symmetry and shared limb junctions keep the front-facing pose clear."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '10921a97-46e3-5bea-b3ba-ce5691a7278c'
SOURCE_PATH = 'pictographic-primitives/babies/baby care body_10921a97-46e3-5bea-b3ba-ce5691a7278c.svg'
AUTHOR = 'gpt-6'


class SittingBaby(Solo48):
    icon_id = 'sitting-baby'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/babies"
    aliases = ()
    keywords = ('sitting', 'baby', 'infant', 'nursery')

    def build(self) -> None:
        # Centerline extremes: (2,2)-(46,46).
        self.add_arc('head-top', (13, 13), (35, 13), radius_x=11, radius_y=11, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (35, 13), (13, 13), radius_x=11, radius_y=11, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('arm-left', (24, 24), (2, 34), radius_x=22, radius_y=10, sweep=False, large_arc=False)
        self.add_arc('hand-left', (2, 34), (4, 40), radius_x=2, radius_y=6, sweep=False, large_arc=False)
        self.add_contour('left-arm', 'arm-left', 'hand-left', closed=False)
        self.add_arc('hand-right', (44, 40), (46, 34), radius_x=2, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('arm-right', (46, 34), (24, 24), radius_x=22, radius_y=10, sweep=False, large_arc=False)
        self.add_contour('right-arm', 'hand-right', 'arm-right', closed=False)
        self.add_arc('foot-left-upper', (4, 40), (12, 34), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('foot-left-outer', (12, 34), (20, 40), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('foot-left-lower', (20, 40), (4, 40), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('foot-left', 'foot-left-upper', 'foot-left-outer', 'foot-left-lower', closed=True)
        self.add_arc('foot-right-upper', (28, 40), (36, 34), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('foot-right-outer', (36, 34), (44, 40), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('foot-right-lower', (44, 40), (28, 40), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('foot-right', 'foot-right-upper', 'foot-right-outer', 'foot-right-lower', closed=True)
        self.add_line('diaper-band', (12, 34), (36, 34))
        self.add_arc('diaper-bottom', (20, 40), (28, 40), radius_x=6, radius_y=4, sweep=False, large_arc=False)
        self.relate("connect", 'head', 'left-arm')
        self.relate("connect", 'head', 'right-arm')
        self.relate("connect", 'left-arm', 'right-arm')
        self.relate("connect", 'left-arm', 'foot-left')
        self.relate("connect", 'right-arm', 'foot-right')
        self.relate("connect", 'foot-left', 'diaper-bottom')
        self.relate("connect", 'foot-right', 'diaper-bottom')
        self.relate("connect", 'foot-left', 'diaper-band')
        self.relate("connect", 'foot-right', 'diaper-band')
