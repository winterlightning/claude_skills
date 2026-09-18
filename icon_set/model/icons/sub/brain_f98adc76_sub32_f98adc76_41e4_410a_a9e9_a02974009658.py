"""Independent 32px profile of brain-f98adc76.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f98adc76-41e4-410a-a9e9-a02974009658'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/brain_f98adc76-41e4-410a-a9e9-a02974009658.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f98adc76-41e4-410a-a9e9-a02974009658', 'pictographic-primitives/artificial-intelligence/brain_f98adc76-41e4-410a-a9e9-a02974009658.svg'),)
PROFILE_SOURCE_KEYS = ('solo/brain-f98adc76',)
SOLO_SOURCE_ICON_IDS = ('brain-f98adc76',)
REFERENCE_EXPORT_SHA256 = 'eb8fc9b433cc5bffce85a66da6d9cf949ccbe6bff8e85c7a7de4f9174dae02cb'

class Drawing(Sub32):
    icon_id = 'brain-f98adc76-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'artificial-intelligence'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 19), ((2, 15), (3, 13), (6, 11)))
        self.add_bezier('p1-r1-2', (6, 11), ((6, 6), (8, 3), (13, 3)))
        self.add_bezier('p1-r1-3', (13, 3), ((14, 3), (16, 4), (17, 4)))
        self.add_bezier('p1-r1-4', (17, 4), ((18, 3), (20, 2), (21, 2)))
        self.add_bezier('p1-r1-5', (21, 2), ((25, 2), (26, 5), (26, 8)))
        self.add_bezier('p1-r1-6', (26, 8), ((29, 9), (30, 13), (30, 17)))
        self.add_bezier('p1-r1-7', (30, 17), ((30, 20), (28, 21), (28, 24)))
        self.add_bezier('p1-r1-8', (28, 24), ((28, 28), (26, 30), (23, 30)))
        self.add_bezier('p1-r1-9', (23, 30), ((21, 30), (19, 28), (18, 28)))
        self.add_bezier('p1-r1-10', (18, 28), ((17, 29), (16, 29), (14, 29)))
        self.add_bezier('p1-r1-11', (14, 29), ((12, 29), (11, 28), (10, 26)))
        self.add_bezier('p1-r1-12', (10, 26), ((8, 27), (7, 27), (7, 27)))
        self.add_bezier('p1-r1-13', (7, 27), ((4, 27), (2, 24), (2, 19)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
        self.add_bezier('p2-r1-1', (17, 4), ((14, 7), (14, 11), (14, 14)))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (18, 28), ((18, 26), (17, 24), (17, 23)))
        self.add_bezier('p3-r1-2', (17, 23), ((17, 20), (18, 18), (20, 16)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-9', 'p3-r1-1')
        self.relate("connect", 'p1-r1-10', 'p3-r1-1')
