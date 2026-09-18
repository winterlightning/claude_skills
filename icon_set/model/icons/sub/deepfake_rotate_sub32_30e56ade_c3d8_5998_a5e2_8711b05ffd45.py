"""Independent 32px profile of deepfake-rotate.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '30e56ade-c3d8-5998-a5e2-8711b05ffd45'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/deepfake rotate_30e56ade-c3d8-5998-a5e2-8711b05ffd45.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('30e56ade-c3d8-5998-a5e2-8711b05ffd45', 'pictographic-primitives/artificial-intelligence/deepfake rotate_30e56ade-c3d8-5998-a5e2-8711b05ffd45.svg'),)
PROFILE_SOURCE_KEYS = ('solo/deepfake-rotate',)
SOLO_SOURCE_ICON_IDS = ('deepfake-rotate',)
REFERENCE_EXPORT_SHA256 = '744a2a18a095297bca04c268ad53b850a868e36427cc4ccf87e4f939c79a79f6'

class Drawing(Sub32):
    icon_id = 'deepfake-rotate-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'artificial-intelligence'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (18, 5), (14, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (18, 5), (14, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (23, 8), ((25, 10), (26, 12), (27, 15)))
        self.add_bezier('p3-r1-2', (27, 15), ((27, 15), (27, 16), (27, 17)))
        self.add_bezier('p3-r1-3', (27, 17), ((27, 17), (27, 17), (27, 17)))
        self.add_bezier('p3-r1-4', (27, 17), ((27, 17), (27, 18), (27, 18)))
        self.add_bezier('p3-r1-5', (27, 18), ((27, 19), (27, 21), (26, 23)))
        self.add_bezier('p3-r1-6', (26, 23), ((25, 26), (22, 29), (18, 30)))
        self.add_bezier('p3-r1-7', (18, 30), ((18, 30), (17, 30), (17, 30)))
        self.add_bezier('p3-r1-8', (17, 30), ((16, 30), (16, 30), (16, 30)))
        self.add_bezier('p3-r1-9', (16, 30), ((10, 30), (5, 24), (5, 18)))
        self.add_bezier('p3-r1-10', (5, 18), ((5, 18), (5, 17), (5, 17)))
        self.add_bezier('p3-r1-11', (5, 17), ((5, 17), (5, 17), (5, 17)))
        self.add_bezier('p3-r1-12', (5, 17), ((5, 14), (6, 11), (8, 8)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', 'p3-r1-10', 'p3-r1-11', 'p3-r1-12', closed=False)
        self.add_bezier('p4-r1-1', (26, 23), ((20, 22), (14, 19), (11, 14)))
        self.add_bezier('p4-r1-2', (11, 14), ((10, 12), (9, 11), (9, 10)))
        self.add_bezier('p4-r1-3', (9, 10), ((9, 10), (8, 8), (8, 8)))
        self.add_bezier('p4-r1-4', (8, 8), ((8, 8), (8, 8), (8, 8)))
        self.add_bezier('p4-r1-5', (8, 8), ((8, 8), (10, 7), (10, 7)))
        self.add_bezier('p4-r1-6', (10, 7), ((12, 5), (15, 6), (18, 5)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p4-r1-6')
        self.relate("connect", 'p2-r1-1', 'p4-r1-6')
        self.relate("connect", 'p3-r1-5', 'p4-r1-1')
        self.relate("connect", 'p3-r1-6', 'p4-r1-1')
        self.relate("connect", 'p3-r1-12', 'p4-r1-3')
        self.relate("connect", 'p3-r1-12', 'p4-r1-4')
        self.relate("connect", 'p3-r1-12', 'p4-r1-5')
