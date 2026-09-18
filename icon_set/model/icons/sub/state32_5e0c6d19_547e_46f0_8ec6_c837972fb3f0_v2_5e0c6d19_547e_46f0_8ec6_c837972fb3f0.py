# Variant of state32-5e0c6d19-547e-46f0-8ec6-c837972fb3f0; parent file remains unchanged.
"""Independent 32px profile of state32-5e0c6d19-547e-46f0-8ec6-c837972fb3f0.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5e0c6d19-547e-46f0-8ec6-c837972fb3f0'
SOURCE_PATH = 'icon_set/assets/combination-state32/5e0c6d19-547e-46f0-8ec6-c837972fb3f0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5e0c6d19-547e-46f0-8ec6-c837972fb3f0', 'icon_set/assets/combination-state32/5e0c6d19-547e-46f0-8ec6-c837972fb3f0.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'fb0bab2042a8fa685ffbdff3c7ac8f7a14ca4825974dd852e94e53cd3728c7b9'

class DrawingVariant2(Sub32):
    icon_id = 'state32-5e0c6d19-547e-46f0-8ec6-c837972fb3f0-v2'
    variant_of = 'state32-5e0c6d19-547e-46f0-8ec6-c837972fb3f0'
    variant_label = 'Record the actual joined strokes; preserve reviewed artwork'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 9), (7, 30))
        self.add_line('p1-r1-2', (7, 30), (25, 30))
        self.add_line('p1-r1-3', (25, 30), (28, 9))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p1-r2-1', (2, 9), (30, 9))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
        self.add_bezier('p2-r1-1', (9, 9), ((9, 4), (13, 2), (16, 2)))
        self.add_bezier('p2-r1-2', (16, 2), ((19, 2), (23, 4), (23, 9)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'path-1-2', 'path-2-1')
