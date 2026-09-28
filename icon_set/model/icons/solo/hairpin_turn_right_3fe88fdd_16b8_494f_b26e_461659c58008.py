"""Hairpin turn right (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3fe88fdd-16b8-494f-b26e-461659c58008'
SOURCE_PATH = 'pictographic-primitives/transportation/hairpin turn right_3fe88fdd-16b8-494f-b26e-461659c58008.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class HairpinTurnRight(Solo48):
    icon_id = 'hairpin-turn-right'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('hairpin', 'turn', 'right', 'transportation')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_line('e0', (27, 26), (34, 34))
        self.add_line('e1', (34, 34), (40, 29))
        self.add_line('e2', (34, 34), (34, 18))
        self.add_line('e3', (8, 19), (8, 44))
        self.add_bezier('e4', (34, 18), ((34, 17.009), (33.634, 14.9), (33.322, 13.945)), ((31.562, 8.591), (27.141, 4), (21.592, 4)), ((21.436, 4), (21.294, 4.009), (21.145, 4.009)), ((18.973, 4.009), (16.657, 4.664), (14.787, 5.882)), ((11.015, 8.345), (8.017, 13.236), (8.017, 18.1)), ((8.008, 18.245), (8.008, 18.855), (8, 19)))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', 'e4', 'e3', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
