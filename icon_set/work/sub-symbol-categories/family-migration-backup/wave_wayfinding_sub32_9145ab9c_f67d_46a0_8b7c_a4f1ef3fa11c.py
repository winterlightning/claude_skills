"""Independent 32px profile of wave-wayfinding.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9145ab9c-f67d-46a0-8b7c-a4f1ef3fa11c'
SOURCE_PATH = 'pictographic-primitives/wayfinding/wave_9145ab9c-f67d-46a0-8b7c-a4f1ef3fa11c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9145ab9c-f67d-46a0-8b7c-a4f1ef3fa11c', 'pictographic-primitives/wayfinding/wave_9145ab9c-f67d-46a0-8b7c-a4f1ef3fa11c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wave-wayfinding',)
SOLO_SOURCE_ICON_IDS = ('wave-wayfinding',)
REFERENCE_EXPORT_SHA256 = '7cfb79a60e7173c0aeebbd5d67b0c483051f1001f8a4a34a9f1a11224ebcc932'

class Drawing(Sub32):
    icon_id = 'wave-wayfinding-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'wayfinding'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 17), (8, 17))
        self.add_line('p1-r1-2', (8, 17), (13, 5))
        self.add_line('p1-r1-3', (13, 5), (18, 27))
        self.add_line('p1-r1-4', (18, 27), (22, 15))
        self.add_line('p1-r1-5', (22, 15), (30, 15))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
