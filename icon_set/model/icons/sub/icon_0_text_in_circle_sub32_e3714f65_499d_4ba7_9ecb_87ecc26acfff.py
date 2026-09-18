"""Independent 32px profile of icon-0-text-in-circle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e3714f65-499d-4ba7-9ecb-87ecc26acfff'
SOURCE_PATH = 'pictographic-primitives/state/0 text in circle_e3714f65-499d-4ba7-9ecb-87ecc26acfff.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e3714f65-499d-4ba7-9ecb-87ecc26acfff', 'pictographic-primitives/state/0 text in circle_e3714f65-499d-4ba7-9ecb-87ecc26acfff.svg'),)
PROFILE_SOURCE_KEYS = ('solo/icon-0-text-in-circle',)
SOLO_SOURCE_ICON_IDS = ('icon-0-text-in-circle',)
REFERENCE_EXPORT_SHA256 = '9a2a96442fa40bccaacddc40c716e980385c1b298dc4244b115d220e57fde623'

class Drawing(Sub32):
    icon_id = 'icon-0-text-in-circle-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (16, 8), (21, 16), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (21, 16), (16, 24), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (16, 24), (11, 16), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p2-r1-4', (11, 16), (16, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
