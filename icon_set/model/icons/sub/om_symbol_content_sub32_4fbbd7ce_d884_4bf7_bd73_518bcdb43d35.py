"""Independent 32px profile of om-symbol-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4fbbd7ce-d884-4bf7-bd73-518bcdb43d35'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/4fbbd7ce-d884-4bf7-bd73-518bcdb43d35.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4fbbd7ce-d884-4bf7-bd73-518bcdb43d35', 'icon_set/dist/gallery/combination-originals/4fbbd7ce-d884-4bf7-bd73-518bcdb43d35.svg'),)
PROFILE_SOURCE_KEYS = ('solo/om-symbol-content',)
SOLO_SOURCE_ICON_IDS = ('om-symbol-content',)
REFERENCE_EXPORT_SHA256 = '93af44473a066b32e680b67649ff5c8bbe5f82cf97564dbb8af86cae0ccb890e'

class Drawing(Sub32):
    icon_id = 'om-symbol-content-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 8), (18, 11), radius_x=8.246211251235321, radius_y=6.18465843842649, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (18, 11), (11, 17))
        self.add_arc('p1-r1-3', (11, 17), (18, 24), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (18, 24), (2, 24), radius_x=8, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (11, 17), ((14, 16), (17, 16), (20, 16)))
        self.add_bezier('p2-r1-2', (20, 16), ((26, 16), (30, 18), (30, 22)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (30, 22), (27, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (25, 10), (30, 7), radius_x=6, radius_y=5, large_arc=False, sweep=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (24, 2), (24, 2))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
