"""Independent 32px profile of state32-6d29f24a-3e64-4196-858e-9eff669a98f5.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '063ab342-3eb9-4c77-b5e5-59de1a294e59'
SOURCE_PATH = 'pictographic-primitives/state/video_063ab342-3eb9-4c77-b5e5-59de1a294e59.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('063ab342-3eb9-4c77-b5e5-59de1a294e59', 'pictographic-primitives/state/video_063ab342-3eb9-4c77-b5e5-59de1a294e59.svg'), ('86847067-8fdd-411e-9dcf-21637870d1dc', 'pictographic-primitives/symbol/video_86847067-8fdd-411e-9dcf-21637870d1dc.svg'), ('6d29f24a-3e64-4196-858e-9eff669a98f5', 'pictographic-primitives/state/video_6d29f24a-3e64-4196-858e-9eff669a98f5.svg'), ('77cac2c6-9ef1-4a3f-85bf-963aeda09df3', 'pictographic-primitives/symbol/video_77cac2c6-9ef1-4a3f-85bf-963aeda09df3.svg'))
PROFILE_SOURCE_KEYS = ('solo/video', 'solo/video-86847067', 'solo/video-state', 'solo/video-symbol')
SOLO_SOURCE_ICON_IDS = ('video', 'video-86847067', 'video-state', 'video-symbol')
REFERENCE_EXPORT_SHA256 = '617cf2fd29ac4d21b9702b2e53964a47f2f624d1d990805018ef0f3895015bcf'

class Drawing(Sub32):
    icon_id = 'state32-6d29f24a-3e64-4196-858e-9eff669a98f5'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (22, 5))
        self.add_line('p1-r1-2', (22, 5), (22, 12))
        self.add_line('p1-r1-3', (22, 12), (30, 8))
        self.add_line('p1-r1-4', (30, 8), (30, 24))
        self.add_line('p1-r1-5', (30, 24), (22, 20))
        self.add_line('p1-r1-6', (22, 20), (22, 27))
        self.add_line('p1-r1-7', (22, 27), (2, 27))
        self.add_line('p1-r1-8', (2, 27), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
