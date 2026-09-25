"""Independent 32px profile of state32-14b2c83a-b6f9-4186-8a3b-4d7a1895c6ec.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '14b2c83a-b6f9-4186-8a3b-4d7a1895c6ec'
SOURCE_PATH = 'icon_set/assets/combination-state32/14b2c83a-b6f9-4186-8a3b-4d7a1895c6ec.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('14b2c83a-b6f9-4186-8a3b-4d7a1895c6ec', 'icon_set/assets/combination-state32/14b2c83a-b6f9-4186-8a3b-4d7a1895c6ec.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '29a85d8e3f1398e1b1d841a6e69de335c9335ddb61f0d50980675e985e985d4d'

class Drawing(Sub32):
    icon_id = 'state32-14b2c83a-b6f9-4186-8a3b-4d7a1895c6ec'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (4, 24), ((6, 22), (7, 19.333333333333332), (7, 16)))
        self.add_line('p1-r1-2', (7, 16), (7, 12))
        self.add_bezier('p1-r1-3', (7, 12), ((7, 8.666666666666668), (9, 6.666666666666667), (13, 6)))
        self.add_bezier('p1-r1-4', (13, 6), ((13, 3.3333333333333335), (14, 2), (16, 2)))
        self.add_bezier('p1-r1-5', (16, 2), ((18, 2), (19, 3.3333333333333335), (19, 6)))
        self.add_bezier('p1-r1-6', (19, 6), ((23, 6.666666666666667), (25, 8.666666666666668), (25, 12)))
        self.add_line('p1-r1-7', (25, 12), (25, 16))
        self.add_bezier('p1-r1-8', (25, 16), ((25, 19.333333333333332), (26, 22), (28, 24)))
        self.add_line('p1-r1-9', (28, 24), (4, 24))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_line('p2-r1-1', (15, 30), (17, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
