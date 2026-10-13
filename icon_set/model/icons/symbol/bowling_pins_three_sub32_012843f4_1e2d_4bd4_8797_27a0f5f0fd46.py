"""Independent 32px profile of bowling-pins-three.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '012843f4-1e2d-4bd4-8797-27a0f5f0fd46'
SOURCE_PATH = 'pictographic-primitives/symbol/three bowlings_012843f4-1e2d-4bd4-8797-27a0f5f0fd46.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('012843f4-1e2d-4bd4-8797-27a0f5f0fd46', 'pictographic-primitives/symbol/three bowlings_012843f4-1e2d-4bd4-8797-27a0f5f0fd46.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bowling-pins-three',)
SOLO_SOURCE_ICON_IDS = ('bowling-pins-three',)
REFERENCE_EXPORT_SHA256 = 'f40013f945816a6507c09660de05131e7fc85a9a539d7ed162a74c5cc194d69b'

class Drawing(Sub32):
    icon_id = 'bowling-pins-three-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Row of three slim bowling pins: a dot head over a stick body, pins 8 units apart.
        for k, x in enumerate((4, 16, 28)):
            self.add_arc(f'head-{k}-1', (x - 2, 6), (x + 2, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
            self.add_arc(f'head-{k}-2', (x + 2, 6), (x - 2, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
            self.add_contour(f'head-{k}', f'head-{k}-1', f'head-{k}-2', closed=True)
            self.add_line(f'body-{k}', (x, 16), (x, 28))
