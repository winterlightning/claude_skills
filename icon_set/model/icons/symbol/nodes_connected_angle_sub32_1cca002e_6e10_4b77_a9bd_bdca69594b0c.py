"""Independent 32px profile of nodes-connected-angle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1cca002e-6e10-4b77-a9bd-bdca69594b0c'
SOURCE_PATH = 'pictographic-primitives/symbol/design vector_1cca002e-6e10-4b77-a9bd-bdca69594b0c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1cca002e-6e10-4b77-a9bd-bdca69594b0c', 'pictographic-primitives/symbol/design vector_1cca002e-6e10-4b77-a9bd-bdca69594b0c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/nodes-connected-angle',)
SOLO_SOURCE_ICON_IDS = ('nodes-connected-angle',)
REFERENCE_EXPORT_SHA256 = 'bba367cd84ecddddc29bf8b1e1a37018d15ae135e7392c94f9ac13a899122211'

class Drawing(Sub32):
    icon_id = 'nodes-connected-angle-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (9, 12), (9, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (9, 20), (9, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (23, 2), (23, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (23, 10), (23, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (23, 22), (23, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (23, 30), (23, 22), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (9, 12), (19, 6))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (9, 20), (19, 26))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-1', 'p5-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p5-r1-1')
