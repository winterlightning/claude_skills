"""Independent 32px profile of dog-head-profile.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '74ca938d-9d85-4544-b27a-8891d60149ba'
SOURCE_PATH = 'pictographic-primitives/symbol/dog head 1_74ca938d-9d85-4544-b27a-8891d60149ba.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('74ca938d-9d85-4544-b27a-8891d60149ba', 'pictographic-primitives/symbol/dog head 1_74ca938d-9d85-4544-b27a-8891d60149ba.svg'),)
PROFILE_SOURCE_KEYS = ('solo/dog-head-profile',)
SOLO_SOURCE_ICON_IDS = ('dog-head-profile',)
REFERENCE_EXPORT_SHA256 = 'd8be71276bb23fead3e298bbfd37cd35e69458a36064b7f70e77a2bcc91f52c1'

class Drawing(Sub32):
    icon_id = 'dog-head-profile-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 25), (19, 2))
        self.add_line('p1-r1-2', (19, 2), (16, 10))
        self.add_arc('p1-r1-3', (16, 10), (13, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (13, 11), (8, 11))
        self.add_bezier('p1-r1-5', (8, 11), ((5, 11), (2, 14), (2, 17)))
        self.add_bezier('p1-r1-6', (2, 17), ((2, 20), (5, 22), (8, 22)))
        self.add_line('p1-r1-7', (8, 22), (16, 24))
        self.add_line('p1-r1-8', (16, 24), (18, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
