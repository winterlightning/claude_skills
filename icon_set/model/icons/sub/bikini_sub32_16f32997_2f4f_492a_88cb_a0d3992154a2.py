"""Independent 32px profile of bikini.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '16f32997-2f4f-492a-88cb-a0d3992154a2'
SOURCE_PATH = 'pictographic-primitives/symbol/bikini_16f32997-2f4f-492a-88cb-a0d3992154a2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('16f32997-2f4f-492a-88cb-a0d3992154a2', 'pictographic-primitives/symbol/bikini_16f32997-2f4f-492a-88cb-a0d3992154a2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bikini',)
SOLO_SOURCE_ICON_IDS = ('bikini',)
REFERENCE_EXPORT_SHA256 = 'fafd8db80d82cfde8c73fcacdfc745649807ced94432f6efeda32c9726ba1b9f'

class Drawing(Sub32):
    icon_id = 'bikini-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (6, 13), ((10, 16), (13, 18), (13, 22)))
        self.add_bezier('p1-r1-2', (13, 22), ((13, 26), (11, 27), (8, 27)))
        self.add_bezier('p1-r1-3', (8, 27), ((4, 27), (2, 26), (2, 22)))
        self.add_bezier('p1-r1-4', (2, 22), ((2, 18), (4, 15), (6, 13)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (6, 13), (16, 5))
        self.add_line('p2-r1-2', (16, 5), (20, 5))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (26, 13), ((22, 16), (19, 18), (19, 22)))
        self.add_bezier('p3-r1-2', (19, 22), ((19, 26), (21, 27), (24, 27)))
        self.add_bezier('p3-r1-3', (24, 27), ((28, 27), (30, 26), (30, 22)))
        self.add_bezier('p3-r1-4', (30, 22), ((30, 18), (28, 15), (26, 13)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (26, 13), (16, 5))
        self.add_line('p4-r1-2', (16, 5), (12, 5))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (13, 22), (19, 22))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p5-r1-1')
        self.relate("connect", 'p1-r1-2', 'p5-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-2')
        self.relate("connect", 'p2-r1-2', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p4-r1-2')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p5-r1-1')
        self.relate("connect", 'p3-r1-2', 'p5-r1-1')
        self.relate("connect", 'p3-r1-4', 'p4-r1-1')
