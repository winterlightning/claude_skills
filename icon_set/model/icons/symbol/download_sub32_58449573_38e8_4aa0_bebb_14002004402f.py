"""Independent 32px profile of download.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '58449573-38e8-4aa0-bebb-14002004402f'
SOURCE_PATH = 'pictographic-primitives/arrows/download_58449573-38e8-4aa0-bebb-14002004402f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('58449573-38e8-4aa0-bebb-14002004402f', 'pictographic-primitives/arrows/download_58449573-38e8-4aa0-bebb-14002004402f.svg'), ('b452f6dc-091e-4314-a34a-bc3ee182e314', 'pictographic-primitives/emails/download_b452f6dc-091e-4314-a34a-bc3ee182e314.svg'))
PROFILE_SOURCE_KEYS = ('solo/download', 'solo/download-b452f6dc')
SOLO_SOURCE_ICON_IDS = ('download', 'download-b452f6dc')
REFERENCE_EXPORT_SHA256 = '95f8369db92fb21983cb9e0ed3b8aeba4d59d84cc1802adc59db905e84066db5'

class Drawing(Sub32):
    icon_id = 'download-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 22), (2, 25))
        self.add_arc('p1-r1-2', (2, 25), (4, 27), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (4, 27), (28, 27))
        self.add_arc('p1-r1-4', (28, 27), (30, 25), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (30, 25), (30, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (16, 5), (16, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (9, 15), (16, 21))
        self.add_line('p3-r1-2', (16, 21), (23, 15))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
