"""Independent 32px profile of pregnancy-ultrasound.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '911984ca-c8ce-4152-9389-71b6977e67ff'
SOURCE_PATH = 'pictographic-primitives/health/pregnancy ultrasound_911984ca-c8ce-4152-9389-71b6977e67ff.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('911984ca-c8ce-4152-9389-71b6977e67ff', 'pictographic-primitives/health/pregnancy ultrasound_911984ca-c8ce-4152-9389-71b6977e67ff.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pregnancy-ultrasound',)
SOLO_SOURCE_ICON_IDS = ('pregnancy-ultrasound',)
REFERENCE_EXPORT_SHA256 = 'd6156e992473077548755c74eada16ea9eab436be28a1209a66331cb3901341a'

class Drawing(Sub32):
    icon_id = 'pregnancy-ultrasound-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'health'
    categories = ('health', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (11, 5), ((12, 6), (14, 6), (16, 6)))
        self.add_bezier('p1-r1-2', (16, 6), ((18, 6), (20, 6), (21, 5)))
        self.add_line('p1-r1-3', (21, 5), (30, 20))
        self.add_bezier('p1-r1-4', (30, 20), ((26, 24), (20, 27), (16, 27)))
        self.add_bezier('p1-r1-5', (16, 27), ((12, 27), (6, 24), (2, 20)))
        self.add_line('p1-r1-6', (2, 20), (11, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
