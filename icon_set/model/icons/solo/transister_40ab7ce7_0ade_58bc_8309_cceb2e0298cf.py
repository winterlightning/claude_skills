"""Transister (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40ab7ce7-0ade-58bc-8309-cceb2e0298cf'
SOURCE_PATH = 'pictographic-primitives/electronics/transister_40ab7ce7-0ade-58bc-8309-cceb2e0298cf.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Transister(Solo48):
    icon_id = 'transister'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    categories = ('electronics', 'primitives')
    aliases = ()
    keywords = ('transister', 'electronics')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (38, 23), (38, 4))
        self.add_line('e1', (38, 4), (10, 4))
        self.add_line('e2', (10, 4), (10, 23))
        self.add_line('e3', (40, 23), (8, 23))
        self.add_line('e4', (15, 23), (15, 44))
        self.add_line('e5', (24, 23), (24, 44))
        self.add_line('e6', (33, 23), (33, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=False)
        self.add_contour('c1', 'e3', closed=False)
        self.add_contour('c2', 'e4', closed=False)
        self.add_contour('c3', 'e5', closed=False)
        self.add_contour('c4', 'e6', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c1')
        self.relate('connect', 'c4', 'c1')
