"""Independent 32px profile of state32-e3714f65-499d-4ba7-9ecb-87ecc26acfff.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e3714f65-499d-4ba7-9ecb-87ecc26acfff'
SOURCE_PATH = 'icon_set/assets/combination-state32/e3714f65-499d-4ba7-9ecb-87ecc26acfff.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e3714f65-499d-4ba7-9ecb-87ecc26acfff', 'icon_set/assets/combination-state32/e3714f65-499d-4ba7-9ecb-87ecc26acfff.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '81fcb06fcde08128fc14f3acd547793165ee8757dc57fae9795af42598054674'

class Drawing(Sub32):
    icon_id = 'state32-e3714f65-499d-4ba7-9ecb-87ecc26acfff'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (11, 13), (21, 13), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (21, 13), (21, 19))
        self.add_arc('p1-r1-3', (21, 19), (11, 19), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (11, 19), (11, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
