"""love heart keyhole: repaired SOLO48 composition.
Plan: Mirrored curved heart outline.
Keyshape: SQUARE provides a broad heart around the keyhole.
Reduction: Keyhole tapered stem reduced to a single stroke under a complete six-unit circular aperture.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd91aa870-d162-59ac-ae8f-ebb2fbe18fc5'
SOURCE_PATH = 'pictographic-primitives/romance/love heart keyhole_d91aa870-d162-59ac-ae8f-ebb2fbe18fc5.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCES = 'heart'

class Drawing(Solo48):
    icon_id = 'love-heart-keyhole'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('love', 'heart', 'keyhole')

    def heart(self):
        self.add_bezier('left-top', (24, 10), ((21, 7), (18, 6), (15, 6)), ((9, 6), (6, 12), (6, 20)))
        self.add_bezier('left-bottom', (6, 20), ((6, 30), (16, 38), (24, 42)))
        self.add_bezier('right-bottom', (24, 42), ((32, 38), (42, 30), (42, 20)))
        self.add_bezier('right-top', (42, 20), ((42, 12), (39, 6), (33, 6)), ((30, 6), (27, 7), (24, 10)))
        self.add_contour('heart', 'left-top', 'left-bottom', 'right-bottom', 'right-top', closed=True)

    def build(self):
        self.heart()
        self.add_arc('keyhole-right', (24, 19), (24, 25), radius_x=3)
        self.add_arc('keyhole-left', (24, 25), (24, 19), radius_x=3)
        self.add_contour('keyhole-round', 'keyhole-right', 'keyhole-left', closed=True)
        self.add_line('keyhole-stem', (24, 25), (24, 31))
        self.relate('connect', 'keyhole-round', 'keyhole-stem')
