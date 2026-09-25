"""Independent 32px profile of eye-outline.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '3fb03548-09fc-4580-80ab-9c61e488e8e9'
SOURCE_PATH = 'pictographic-primitives/symbol/eyes_3fb03548-09fc-4580-80ab-9c61e488e8e9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3fb03548-09fc-4580-80ab-9c61e488e8e9', 'pictographic-primitives/symbol/eyes_3fb03548-09fc-4580-80ab-9c61e488e8e9.svg'), ('6627b62c-9a54-43be-8f20-fccd8ae111e8', 'pictographic-primitives/symbol/focus with eye_6627b62c-9a54-43be-8f20-fccd8ae111e8.svg'))
PROFILE_SOURCE_KEYS = ('solo/eye-outline', 'solo/eye-outline-focus')
SOLO_SOURCE_ICON_IDS = ('eye-outline', 'eye-outline-focus')
REFERENCE_EXPORT_SHA256 = '3f9f835209e60249bcce998450ba467637b401f4719e1f070dcef130ad74376c'

class DrawingVariant3(Sub32):
    icon_id = 'eye-outline-sub32-v3'
    related_origin_icon_id = 'eye-outline-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('ul', (2, 16), ((6, 9), (10, 6), (14, 6)))
        self.add_line('top', (14, 6), (18, 6))
        self.add_bezier('ur', (18, 6), ((22, 6), (26, 9), (30, 16)))
        self.add_bezier('lr', (30, 16), ((26, 23), (22, 26), (18, 26)))
        self.add_line('bottom', (18, 26), (14, 26))
        self.add_bezier('ll', (14, 26), ((10, 26), (6, 23), (2, 16)))
        self.add_contour('eye', 'ul', 'top', 'ur', 'lr', 'bottom', 'll', closed=True)
        self.add_arc('pupil-top', (13, 16), (19, 16), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('pupil-bottom', (19, 16), (13, 16), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('pupil', 'pupil-top', 'pupil-bottom', closed=True)
