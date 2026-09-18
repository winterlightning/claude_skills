"""Independent 32px profile of vaccine-bottle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1610e3ba-84a5-4d21-aaf5-def7c21e3e28'
SOURCE_PATH = 'pictographic-primitives/health/vaccine bottle_1610e3ba-84a5-4d21-aaf5-def7c21e3e28.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1610e3ba-84a5-4d21-aaf5-def7c21e3e28', 'pictographic-primitives/health/vaccine bottle_1610e3ba-84a5-4d21-aaf5-def7c21e3e28.svg'),)
PROFILE_SOURCE_KEYS = ('solo/vaccine-bottle',)
SOLO_SOURCE_ICON_IDS = ('vaccine-bottle',)
REFERENCE_EXPORT_SHA256 = 'c6e4bdc903938d4765736868d41653f30a8474b79ef2b52f8f2160dbca68d697'

class Drawing(Sub32):
    icon_id = 'vaccine-bottle-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'health'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 2), (12, 8))
        self.add_bezier('p1-r1-2', (12, 8), ((8, 10), (5, 10), (5, 12)))
        self.add_line('p1-r1-3', (5, 12), (5, 20))
        self.add_line('p1-r1-4', (5, 20), (5, 27))
        self.add_arc('p1-r1-5', (5, 27), (8, 30), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-6', (8, 30), (24, 30))
        self.add_arc('p1-r1-7', (24, 30), (27, 27), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-8', (27, 27), (27, 20))
        self.add_line('p1-r1-9', (27, 20), (27, 12))
        self.add_bezier('p1-r1-10', (27, 12), ((27, 10), (24, 10), (20, 8)))
        self.add_line('p1-r1-11', (20, 8), (20, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_line('p2-r1-1', (9, 2), (12, 2))
        self.add_line('p2-r1-2', (12, 2), (20, 2))
        self.add_line('p2-r1-3', (20, 2), (23, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_bezier('p3-r1-1', (5, 20), ((7, 18), (9, 18), (10, 18)))
        self.add_bezier('p3-r1-2', (10, 18), ((12, 18), (14, 18), (16, 20)))
        self.add_bezier('p3-r1-3', (16, 20), ((18, 21), (20, 21), (22, 21)))
        self.add_bezier('p3-r1-4', (22, 21), ((23, 21), (25, 21), (27, 20)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-8', 'p3-r1-4')
        self.relate("connect", 'p1-r1-9', 'p3-r1-4')
        self.relate("connect", 'p1-r1-11', 'p2-r1-2')
        self.relate("connect", 'p1-r1-11', 'p2-r1-3')
