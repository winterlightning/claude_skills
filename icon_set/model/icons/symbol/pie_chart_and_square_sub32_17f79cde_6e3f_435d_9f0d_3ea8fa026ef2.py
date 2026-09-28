"""Independent 32px profile of pie-chart-and-square.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '17f79cde-6e3f-435d-9f0d-3ea8fa026ef2'
SOURCE_PATH = 'pictographic-primitives/symbol/pie chart and square_17f79cde-6e3f-435d-9f0d-3ea8fa026ef2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('17f79cde-6e3f-435d-9f0d-3ea8fa026ef2', 'pictographic-primitives/symbol/pie chart and square_17f79cde-6e3f-435d-9f0d-3ea8fa026ef2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pie-chart-and-square',)
SOLO_SOURCE_ICON_IDS = ('pie-chart-and-square',)
REFERENCE_EXPORT_SHA256 = '4e9a6a2bce4d0c8bd0757ec02f82a55f4de1fc40c4ed6564d48268ed0557f626'

class Drawing(Sub32):
    icon_id = 'pie-chart-and-square-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (21, 13), (30, 13))
        self.add_line('p1-r1-2', (30, 13), (30, 30))
        self.add_line('p1-r1-3', (30, 30), (13, 30))
        self.add_bezier('p1-r1-4', (13, 30), ((13, 30), (13, 30), (13, 30)))
        self.add_bezier('p1-r1-5', (13, 30), ((13, 29), (13, 29), (13, 29)))
        self.add_line('p1-r1-6', (13, 29), (13, 21))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (21, 13), (13, 13))
        self.add_line('p2-r1-2', (13, 13), (13, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (21, 12), ((21, 6), (17, 2), (12, 2)))
        self.add_bezier('p3-r1-2', (12, 2), ((6, 2), (2, 6), (2, 12)))
        self.add_bezier('p3-r1-3', (2, 12), ((2, 17), (6, 21), (12, 21)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-2')
