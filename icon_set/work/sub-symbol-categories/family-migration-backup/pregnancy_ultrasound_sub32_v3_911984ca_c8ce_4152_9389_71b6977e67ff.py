# Variant of pregnancy-ultrasound-sub32-v2; parent file remains unchanged.
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

class DrawingVariant3(Sub32):
    icon_id = 'pregnancy-ultrasound-sub32-v3'
    variant_of = 'pregnancy-ultrasound-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Wide ultrasound sector with a shallow near arc and broad curved far edge.
        self.add_bezier('near',(11,8),((14,10),(18,10),(21,8)))
        self.add_line('right',(21,8),(30,18))
        self.add_bezier('far',(30,18),((24,26),(8,26),(2,18)))
        self.add_line('left',(2,18),(11,8))
        self.add_contour('sector','near','right','far','left',closed=True)
