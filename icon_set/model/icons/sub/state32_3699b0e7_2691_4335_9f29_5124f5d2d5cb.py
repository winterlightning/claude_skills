"""Independent 32px profile of state32-3699b0e7-2691-4335-9f29-5124f5d2d5cb.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3699b0e7-2691-4335-9f29-5124f5d2d5cb'
SOURCE_PATH = 'icon_set/assets/combination-state32/3699b0e7-2691-4335-9f29-5124f5d2d5cb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3699b0e7-2691-4335-9f29-5124f5d2d5cb', 'icon_set/assets/combination-state32/3699b0e7-2691-4335-9f29-5124f5d2d5cb.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '8e73f34ea811a1fbe05ec91b4d00113a4f4804fb1b08070bb22beaee48e13f0d'

class Drawing(Sub32):
    icon_id = 'state32-3699b0e7-2691-4335-9f29-5124f5d2d5cb'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (14, 12), (9, 16))
        self.add_line('p1-r1-2', (9, 16), (14, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p1-r2-1', (18, 12), (23, 16))
        self.add_line('p1-r2-2', (23, 16), (18, 20))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
