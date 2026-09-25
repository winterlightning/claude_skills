"""Independent 32px profile of state32-e6789468-9cc2-4444-a388-10e9ec1fdcb5.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e6789468-9cc2-4444-a388-10e9ec1fdcb5'
SOURCE_PATH = 'icon_set/assets/combination-state32/e6789468-9cc2-4444-a388-10e9ec1fdcb5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e6789468-9cc2-4444-a388-10e9ec1fdcb5', 'icon_set/assets/combination-state32/e6789468-9cc2-4444-a388-10e9ec1fdcb5.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'fd3365f3e6d800c4310aa10107d0980cddc2bba1e9d025e7569ee6201ab27637'

class Drawing(Sub32):
    icon_id = 'state32-e6789468-9cc2-4444-a388-10e9ec1fdcb5'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 9), ((6.666666666666666, 5.666666666666667), (11.333333333333334, 4), (16, 4)))
        self.add_bezier('p1-r1-2', (16, 4), ((20.666666666666664, 4), (25.333333333333336, 5.666666666666667), (30, 9)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p1-r2-1', (8, 17), ((10.666666666666666, 15), (13.333333333333334, 14), (16, 14)))
        self.add_bezier('p1-r2-2', (16, 14), ((18.666666666666668, 14), (21.333333333333332, 15), (24, 17)))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', closed=False)
        self.add_line('p2-r1-1', (16, 28), (16, 28))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
