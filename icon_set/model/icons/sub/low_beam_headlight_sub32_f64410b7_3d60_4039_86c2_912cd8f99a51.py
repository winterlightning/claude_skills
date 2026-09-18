"""Independent 32px profile of low-beam-headlight.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f64410b7-3d60-4039-86c2-912cd8f99a51'
SOURCE_PATH = 'pictographic-primitives/transportation/car dashboard lights_f64410b7-3d60-4039-86c2-912cd8f99a51.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f64410b7-3d60-4039-86c2-912cd8f99a51', 'pictographic-primitives/transportation/car dashboard lights_f64410b7-3d60-4039-86c2-912cd8f99a51.svg'),)
PROFILE_SOURCE_KEYS = ('solo/low-beam-headlight',)
SOLO_SOURCE_ICON_IDS = ('low-beam-headlight',)
REFERENCE_EXPORT_SHA256 = '39ecd49ae871e521f8f15b3bc81faaf23de818bf0fcdeedd659de6f836da5e08'

class Drawing(Sub32):
    icon_id = 'low-beam-headlight-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (19, 5), (19, 27))
        self.add_arc('p1-r1-2', (19, 27), (19, 5), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 10), (12, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 22), (12, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
