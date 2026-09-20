"""Independent 32px profile of sledding-person.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd6bf82b5-b45d-4650-80db-680bfbec97fe'
SOURCE_PATH = 'pictographic-primitives/symbol/snow slide_d6bf82b5-b45d-4650-80db-680bfbec97fe.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d6bf82b5-b45d-4650-80db-680bfbec97fe', 'pictographic-primitives/symbol/snow slide_d6bf82b5-b45d-4650-80db-680bfbec97fe.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sledding-person',)
SOLO_SOURCE_ICON_IDS = ('sledding-person',)
REFERENCE_EXPORT_SHA256 = 'db1e356bee0953ac51aa88cfbad72e59043dacadc82812cc260bbcd3adde6505'

class Drawing(Sub32):
    icon_id = 'sledding-person-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (22, 11), (30, 11), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 11), (22, 11), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (4, 2), (7, 10))
        self.add_bezier('p2-r1-2', (7, 10), ((8, 11), (13, 15), (16, 15)))
        self.add_bezier('p2-r1-3', (16, 15), ((16, 15), (17, 15), (17, 15)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (11, 3), (17, 15))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 18), (19, 28))
        self.add_bezier('p4-r1-2', (19, 28), ((19, 29), (22, 30), (25, 30)))
        self.add_bezier('p4-r1-3', (25, 30), ((28, 30), (30, 29), (30, 28)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
