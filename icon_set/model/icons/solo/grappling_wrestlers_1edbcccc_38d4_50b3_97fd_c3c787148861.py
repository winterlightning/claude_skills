'Two crouching wrestlers grapple face to face.\nConstruction: Square centerlines (6,6)-(42,42). Mirror crouching bodies and joined arms; omit doubled overlapping arm outlines.\nLucide: accessibility: circular heads and bent limb construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1edbcccc-38d4-50b3-97fd-c3c787148861'
SOURCE_PATH = 'pictographic-primitives/sports/wrestling fight_1edbcccc-38d4-50b3-97fd-c3c787148861.svg'
AUTHOR = 'gpt-6'

class GrapplingWrestlers(Solo48):
    icon_id = 'grappling-wrestlers'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('grappling', 'wrestlers', 'sport')

    def build(self):
        self.add_arc('left-head-top', (12, 9), (18, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('left-head-bottom', (18, 9), (12, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('left-head', 'left-head-top', 'left-head-bottom', closed=True)
        self.add_arc('right-head-top', (30, 9), (36, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('right-head-bottom', (36, 9), (30, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('right-head', 'right-head-top', 'right-head-bottom', closed=True)
        self.add_polyline('left-body', (6, 42), (12, 32), (15, 21), closed=False)
        self.add_polyline('left-leg', (12, 32), (21, 36), (21, 42), closed=False)
        self.relate("connect", 'left-body', 'left-leg')
        self.add_polyline('right-body', (42, 42), (36, 32), (33, 21), closed=False)
        self.add_polyline('right-leg', (36, 32), (27, 36), (27, 42), closed=False)
        self.relate("connect", 'right-body', 'right-leg')
        self.add_polyline('arms', (15, 21), (24, 27), (33, 21), closed=False)
        self.relate("connect", 'arms', 'left-body')
        self.relate("connect", 'arms', 'right-body')
