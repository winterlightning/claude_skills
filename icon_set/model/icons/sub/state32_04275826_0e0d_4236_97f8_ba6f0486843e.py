"""Independent 32px profile of state32-04275826-0e0d-4236-97f8-ba6f0486843e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '04275826-0e0d-4236-97f8-ba6f0486843e'
SOURCE_PATH = 'icon_set/assets/combination-state32/04275826-0e0d-4236-97f8-ba6f0486843e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('04275826-0e0d-4236-97f8-ba6f0486843e', 'icon_set/assets/combination-state32/04275826-0e0d-4236-97f8-ba6f0486843e.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'b0a27165442e438d949783beed4b5af54c50578c54843869036eae2251a01d31'

class Drawing(Sub32):
    icon_id = 'state32-04275826-0e0d-4236-97f8-ba6f0486843e'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 29), (4, 3))
        self.add_line('p1-r1-2', (4, 3), (19, 3))
        self.add_line('p1-r1-3', (19, 3), (19, 29))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p1-r2-1', (19, 12), (27, 17))
        self.add_line('p1-r2-2', (27, 17), (27, 29))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', closed=False)
        self.add_line('p1-r3-1', (2, 29), (30, 29))
        self.add_contour('path-1-3', 'p1-r3-1', closed=False)
        self.add_line('p1-r4-1', (9, 10), (13, 10))
        self.add_contour('path-1-4', 'p1-r4-1', closed=False)
        self.add_line('p1-r5-1', (9, 19), (13, 19))
        self.add_contour('path-1-5', 'p1-r5-1', closed=False)
