"""Obstruction (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77ce8c19-d748-4677-9097-15486e0a1c5b'
SOURCE_PATH = 'pictographic-primitives/transportation/obstruction_77ce8c19-d748-4677-9097-15486e0a1c5b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Obstruction(Solo48):
    icon_id = 'obstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('obstruction', 'transportation')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (33, 27), (33, 42))
        self.add_line('e1', (33, 42), (15, 42))
        self.add_line('e2', (15, 42), (15, 27))
        self.add_line('e3', (33, 27), (26, 27))
        self.add_line('e4', (33, 27), (42, 27))
        self.add_line('e5', (42, 27), (42, 15))
        self.add_line('e6', (42, 15), (34, 15))
        self.add_line('e7', (33, 16), (29, 22))
        self.add_line('e8', (29, 22), (26, 27))
        self.add_line('e9', (15, 27), (26, 27))
        self.add_line('e10', (15, 27), (13, 27))
        self.add_line('e11', (13, 27), (21, 15))
        self.add_line('e12', (13, 27), (6, 27))
        self.add_line('e13', (6, 27), (6, 15))
        self.add_line('e14', (6, 15), (15, 15))
        self.add_line('e15', (21, 15), (33, 15))
        self.add_line('e16', (33, 15), (33, 6))
        self.add_line('e17', (33, 6), (15, 6))
        self.add_line('e18', (15, 6), (15, 15))
        self.add_line('e19', (21, 15), (15, 15))
        self.add_arc('e23', (34, 15), (33, 16), radius_x=15, radius_y=15, large_arc=False, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=False)
        self.add_contour('c1', 'e3', closed=False)
        self.add_contour('c2', 'e4', 'e5', 'e6', 'e23', 'e7', 'e8', closed=False)
        self.add_contour('c3', 'e9', closed=False)
        self.add_contour('c4', 'e10', closed=False)
        self.add_contour('c5', 'e11', closed=False)
        self.add_contour('c6', 'e12', 'e13', 'e14', closed=False)
        self.add_contour('c7', 'e15', 'e16', 'e17', 'e18', closed=False)
        self.add_contour('c8', 'e19', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
