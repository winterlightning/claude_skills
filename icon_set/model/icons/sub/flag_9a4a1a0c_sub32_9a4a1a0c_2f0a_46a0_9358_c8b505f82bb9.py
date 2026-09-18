"""Independent 32px profile of flag-9a4a1a0c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9a4a1a0c-2f0a-46a0-9358-c8b505f82bb9'
SOURCE_PATH = 'pictographic-primitives/social/flag_9a4a1a0c-2f0a-46a0-9358-c8b505f82bb9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9a4a1a0c-2f0a-46a0-9358-c8b505f82bb9', 'pictographic-primitives/social/flag_9a4a1a0c-2f0a-46a0-9358-c8b505f82bb9.svg'), ('c753cf19-a137-4abc-ac45-e83ec45cd778', 'pictographic-primitives/social/flag_c753cf19-a137-4abc-ac45-e83ec45cd778.svg'))
PROFILE_SOURCE_KEYS = ('solo/flag-9a4a1a0c', 'solo/flag-c753cf19')
SOLO_SOURCE_ICON_IDS = ('flag-9a4a1a0c', 'flag-c753cf19')
REFERENCE_EXPORT_SHA256 = '5da2e7c789077887a0fef2ba82c352c176f536c8ee962674f0364698bf0569cf'

class Drawing(Sub32):
    icon_id = 'flag-9a4a1a0c-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'social'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 2), (5, 5))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (5, 30), (5, 19))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (5, 5), (13, 6), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_line('p3-r1-2', (13, 6), (18, 4))
        self.add_arc('p3-r1-3', (18, 4), (27, 6), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('p3-r1-4', (27, 6), (25, 10))
        self.add_arc('p3-r1-5', (25, 10), (24, 12), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('p3-r1-6', (24, 12), (27, 19))
        self.add_arc('p3-r1-7', (27, 19), (19, 17), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('p3-r1-8', (19, 17), (14, 20))
        self.add_arc('p3-r1-9', (14, 20), (5, 19), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', closed=False)
        self.add_line('p4-r1-1', (5, 5), (5, 19))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-9')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-9', 'p4-r1-1')
