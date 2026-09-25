"""Independent 32px profile of eye-outline.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3fb03548-09fc-4580-80ab-9c61e488e8e9'
SOURCE_PATH = 'pictographic-primitives/symbol/eyes_3fb03548-09fc-4580-80ab-9c61e488e8e9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3fb03548-09fc-4580-80ab-9c61e488e8e9', 'pictographic-primitives/symbol/eyes_3fb03548-09fc-4580-80ab-9c61e488e8e9.svg'), ('6627b62c-9a54-43be-8f20-fccd8ae111e8', 'pictographic-primitives/symbol/focus with eye_6627b62c-9a54-43be-8f20-fccd8ae111e8.svg'))
PROFILE_SOURCE_KEYS = ('solo/eye-outline', 'solo/eye-outline-focus')
SOLO_SOURCE_ICON_IDS = ('eye-outline', 'eye-outline-focus')
REFERENCE_EXPORT_SHA256 = '3f9f835209e60249bcce998450ba467637b401f4719e1f070dcef130ad74376c'

class Drawing(Sub32):
    icon_id = 'eye-outline-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 16), ((6, 9), (10, 5), (16, 5)))
        self.add_bezier('p1-r1-2', (16, 5), ((22, 5), (26, 9), (30, 16)))
        self.add_bezier('p1-r1-3', (30, 16), ((26, 23), (22, 27), (16, 27)))
        self.add_bezier('p1-r1-4', (16, 27), ((10, 27), (6, 23), (2, 16)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (12, 16), (20, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (20, 16), (12, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
