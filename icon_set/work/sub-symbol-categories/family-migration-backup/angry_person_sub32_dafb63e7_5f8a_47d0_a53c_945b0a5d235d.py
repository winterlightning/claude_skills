"""Independent 32px profile of angry-person.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'dafb63e7-5f8a-47d0-a53c-945b0a5d235d'
SOURCE_PATH = 'pictographic-primitives/symbol/angry person_dafb63e7-5f8a-47d0-a53c-945b0a5d235d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dafb63e7-5f8a-47d0-a53c-945b0a5d235d', 'pictographic-primitives/symbol/angry person_dafb63e7-5f8a-47d0-a53c-945b0a5d235d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/angry-person',)
SOLO_SOURCE_ICON_IDS = ('angry-person',)
REFERENCE_EXPORT_SHA256 = '4ecc72aa7bda85e6b1e97b0021380500b4843c8e405d213f478ecd2db959034f'

class Drawing(Sub32):
    icon_id = 'angry-person-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 13), (27, 13), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (27, 13), (5, 13), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (5, 30), ((8, 26), (12, 24), (16, 24)))
        self.add_bezier('p2-r1-2', (16, 24), ((20, 24), (24, 26), (27, 30)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (12, 10), (13, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (19, 11), (20, 10))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_arc('p5-r1-1', (14, 17), (18, 17), radius_x=2, radius_y=1, large_arc=False, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
