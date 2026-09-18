"""Independent 32px profile of upright-three-pointed-leaf-plant.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '64e98c12-a497-4ac3-ad90-841c585f54e3'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_64e98c12-a497-4ac3-ad90-841c585f54e3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('64e98c12-a497-4ac3-ad90-841c585f54e3', 'pictographic-primitives/decoration/batch-03/indoor plant_64e98c12-a497-4ac3-ad90-841c585f54e3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/upright-three-pointed-leaf-plant',)
SOLO_SOURCE_ICON_IDS = ('upright-three-pointed-leaf-plant',)
REFERENCE_EXPORT_SHA256 = '021c1106539d742f8906013ce84045fb696103114735549b1217d548397eff2f'

class Drawing(Sub32):
    icon_id = 'upright-three-pointed-leaf-plant-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'nature/plants'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (10, 22), ((7, 22), (5, 15), (5, 8)))
        self.add_bezier('p1-r1-2', (5, 8), ((5, 8), (5, 8), (5, 8)))
        self.add_bezier('p1-r1-3', (5, 8), ((9, 8), (12, 11), (12, 15)))
        self.add_bezier('p1-r1-4', (12, 15), ((12, 8), (14, 2), (16, 2)))
        self.add_bezier('p1-r1-5', (16, 2), ((18, 2), (20, 8), (20, 15)))
        self.add_bezier('p1-r1-6', (20, 15), ((20, 11), (23, 8), (27, 8)))
        self.add_bezier('p1-r1-7', (27, 8), ((27, 8), (27, 8), (27, 8)))
        self.add_bezier('p1-r1-8', (27, 8), ((27, 15), (25, 22), (22, 22)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (8, 22), (16, 22))
        self.add_line('p2-r1-2', (16, 22), (24, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (24, 22), (23, 29))
        self.add_bezier('p3-r1-2', (23, 29), ((23, 30), (22, 30), (20, 30)))
        self.add_line('p3-r1-3', (20, 30), (12, 30))
        self.add_bezier('p3-r1-4', (12, 30), ((10, 30), (9, 30), (9, 29)))
        self.add_line('p3-r1-5', (9, 29), (8, 22))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-5')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
