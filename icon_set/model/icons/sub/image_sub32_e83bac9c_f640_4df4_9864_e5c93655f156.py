"""Independent 32px profile of image.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e83bac9c-f640-4df4-9864-e5c93655f156'
SOURCE_PATH = 'pictographic-primitives/images/image_e83bac9c-f640-4df4-9864-e5c93655f156.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e83bac9c-f640-4df4-9864-e5c93655f156', 'pictographic-primitives/images/image_e83bac9c-f640-4df4-9864-e5c93655f156.svg'),)
PROFILE_SOURCE_KEYS = ('solo/image',)
SOLO_SOURCE_ICON_IDS = ('image',)
REFERENCE_EXPORT_SHA256 = '9b6a4891ba85510ed1568849d58d19378ac5db5bb65603b19fd60cf181ba786c'

class Drawing(Sub32):
    icon_id = 'image-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'images'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (20, 22), (13, 14))
        self.add_line('p1-r1-2', (13, 14), (2, 27))
        self.add_line('p1-r1-3', (2, 27), (30, 27))
        self.add_line('p1-r1-4', (30, 27), (22, 19))
        self.add_line('p1-r1-5', (22, 19), (20, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_arc('p2-r1-1', (22, 9), (30, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (30, 9), (22, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
