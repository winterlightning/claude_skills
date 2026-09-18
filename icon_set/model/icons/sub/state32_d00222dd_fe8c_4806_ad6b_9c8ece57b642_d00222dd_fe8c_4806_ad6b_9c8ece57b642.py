"""Independent 32px profile of state32-d00222dd-fe8c-4806-ad6b-9c8ece57b642.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd00222dd-fe8c-4806-ad6b-9c8ece57b642'
SOURCE_PATH = 'pictographic-primitives/state/circle pound_d00222dd-fe8c-4806-ad6b-9c8ece57b642.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d00222dd-fe8c-4806-ad6b-9c8ece57b642', 'pictographic-primitives/state/circle pound_d00222dd-fe8c-4806-ad6b-9c8ece57b642.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circle-pound',)
SOLO_SOURCE_ICON_IDS = ('circle-pound',)
REFERENCE_EXPORT_SHA256 = '0605f5f65b1837381aa0073d1ccf9156ebfd5935bc7b2c9515b407124464a8f9'

class Drawing(Sub32):
    icon_id = 'state32-d00222dd-fe8c-4806-ad6b-9c8ece57b642'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (20, 11), ((20, 10), (19, 10), (17, 10)))
        self.add_bezier('p1-r1-2', (17, 10), ((15, 10), (14, 11), (13, 13)))
        self.add_line('p1-r1-3', (13, 13), (13, 20))
        self.add_bezier('p1-r1-4', (13, 20), ((13, 21.333333333333332), (12.333333333333334, 22), (11, 22)))
        self.add_line('p1-r1-5', (11, 22), (21, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p1-r2-1', (11, 16), (19, 16))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
