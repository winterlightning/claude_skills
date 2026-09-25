"""Independent 32px profile of horizontal-double-ended-wrench.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd63b4e68-3e3c-4320-ad5b-85484116fc79'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/wrench_d63b4e68-3e3c-4320-ad5b-85484116fc79.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d63b4e68-3e3c-4320-ad5b-85484116fc79', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/wrench_d63b4e68-3e3c-4320-ad5b-85484116fc79.svg'),)
PROFILE_SOURCE_KEYS = ('solo/horizontal-double-ended-wrench',)
SOLO_SOURCE_ICON_IDS = ('horizontal-double-ended-wrench',)
REFERENCE_EXPORT_SHA256 = 'bbd34472ac562d2c2a686189e147f907232a7a2d8c656dccb4cbcebc4cc495a8'

class Drawing(Sub32):
    icon_id = 'horizontal-double-ended-wrench-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 12), ((2, 9), (3, 6), (6, 6)))
        self.add_bezier('p1-r1-2', (6, 6), ((10, 6), (10, 12), (13, 12)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (13, 20), ((10, 20), (10, 26), (6, 26)))
        self.add_bezier('p2-r1-2', (6, 26), ((3, 26), (2, 23), (2, 20)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 20), (8, 20))
        self.add_line('p3-r1-2', (8, 20), (8, 12))
        self.add_line('p3-r1-3', (8, 12), (2, 12))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_bezier('p4-r1-1', (30, 12), ((30, 9), (29, 6), (26, 6)))
        self.add_bezier('p4-r1-2', (26, 6), ((22, 6), (22, 12), (19, 12)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_bezier('p5-r1-1', (19, 20), ((22, 20), (22, 26), (26, 26)))
        self.add_bezier('p5-r1-2', (26, 26), ((29, 26), (30, 23), (30, 20)))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (30, 20), (24, 20))
        self.add_line('p6-r1-2', (24, 20), (24, 12))
        self.add_line('p6-r1-3', (24, 12), (30, 12))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', closed=False)
        self.add_line('p7-r1-1', (13, 12), (19, 12))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (13, 20), (19, 20))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-3')
        self.relate("connect", 'p1-r1-2', 'p7-r1-1')
        self.relate("connect", 'p2-r1-1', 'p8-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p4-r1-1', 'p6-r1-3')
        self.relate("connect", 'p4-r1-2', 'p7-r1-1')
        self.relate("connect", 'p5-r1-1', 'p8-r1-1')
        self.relate("connect", 'p5-r1-2', 'p6-r1-1')
