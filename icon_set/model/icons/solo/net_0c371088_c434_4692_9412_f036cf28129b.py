"""Net (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c371088-c434-4692-9412-f036cf28129b'
SOURCE_PATH = 'pictographic-primitives/design/net_0c371088-c434-4692-9412-f036cf28129b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Net(Solo48):
    icon_id = 'net'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('net', 'design')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (42, 34), (24, 25))
        self.add_line('e1', (24, 25), (16, 42))
        self.add_line('e2', (42, 34), (42, 42))
        self.add_line('e3', (42, 42), (16, 42))
        self.add_line('e4', (42, 34), (42, 6))
        self.add_line('e5', (42, 6), (33, 6))
        self.add_line('e6', (16, 42), (6, 42))
        self.add_line('e7', (6, 42), (6, 16))
        self.add_line('e8', (6, 16), (6, 6))
        self.add_line('e9', (6, 6), (33, 6))
        self.add_line('e10', (6, 16), (24, 25))
        self.add_line('e11', (24, 25), (33, 6))
        self.add_contour('c0', 'e0', 'e1', closed=False)
        self.add_contour('c1', 'e2', 'e3', closed=False)
        self.add_contour('c2', 'e4', 'e5', closed=False)
        self.add_contour('c3', 'e6', 'e7', closed=False)
        self.add_contour('c4', 'e8', 'e9', closed=False)
        self.add_contour('c5', 'e10', 'e11', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
