"""Independent 32px profile of carrot-with-two-pointed-leaves.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6175b21e-96a2-4503-a4cc-6b0bc36376c0'
SOURCE_PATH = 'pictographic-primitives/food/carrot_6175b21e-96a2-4503-a4cc-6b0bc36376c0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6175b21e-96a2-4503-a4cc-6b0bc36376c0', 'pictographic-primitives/food/carrot_6175b21e-96a2-4503-a4cc-6b0bc36376c0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/carrot-with-two-pointed-leaves',)
SOLO_SOURCE_ICON_IDS = ('carrot-with-two-pointed-leaves',)
REFERENCE_EXPORT_SHA256 = 'b7c0515f7de3002b2ccc1c0c1222bbb9273c75f4f852db578b954aba04270a0d'

class Drawing(Sub32):
    icon_id = 'carrot-with-two-pointed-leaves-profile32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/food'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 12), ((15, 12), (15, 11), (14, 11)))
        self.add_bezier('p1-r1-2', (14, 11), ((11, 11), (9, 14), (9, 16)))
        self.add_bezier('p1-r1-3', (9, 16), ((9, 21), (15, 30), (16, 30)))
        self.add_bezier('p1-r1-4', (16, 30), ((17, 30), (23, 21), (23, 16)))
        self.add_bezier('p1-r1-5', (23, 16), ((23, 14), (21, 11), (18, 11)))
        self.add_bezier('p1-r1-6', (18, 11), ((17, 11), (17, 12), (16, 12)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_bezier('p2-r1-1', (16, 12), ((12, 12), (5, 9), (5, 2)))
        self.add_bezier('p2-r1-2', (5, 2), ((10, 3), (16, 6), (16, 12)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (16, 12), ((20, 12), (27, 9), (27, 2)))
        self.add_bezier('p3-r1-2', (27, 2), ((22, 3), (16, 6), (16, 12)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-2')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-2')
        self.relate("connect", 'p1-r1-6', 'p3-r1-1')
        self.relate("connect", 'p1-r1-6', 'p3-r1-2')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-2')
