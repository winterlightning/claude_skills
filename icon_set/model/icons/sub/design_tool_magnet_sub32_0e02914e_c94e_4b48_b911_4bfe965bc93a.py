"""Independent 32px profile of design-tool-magnet.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0e02914e-c94e-4b48-b911-4bfe965bc93a'
SOURCE_PATH = 'pictographic-primitives/design/design tool magnet_0e02914e-c94e-4b48-b911-4bfe965bc93a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0e02914e-c94e-4b48-b911-4bfe965bc93a', 'pictographic-primitives/design/design tool magnet_0e02914e-c94e-4b48-b911-4bfe965bc93a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/design-tool-magnet',)
SOLO_SOURCE_ICON_IDS = ('design-tool-magnet',)
REFERENCE_EXPORT_SHA256 = '92424af0b43f72b154045ed283e3e59c4b483f67261733c2a671fd0163ae6aab'

class Drawing(Sub32):
    icon_id = 'design-tool-magnet-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (10, 2))
        self.add_line('p1-r1-2', (10, 2), (10, 16))
        self.add_arc('p1-r1-3', (10, 16), (22, 16), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (22, 16), (22, 2))
        self.add_line('p1-r1-5', (22, 2), (30, 2))
        self.add_line('p1-r1-6', (30, 2), (30, 16))
        self.add_arc('p1-r1-7', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (2, 16), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (2, 10), (10, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (22, 10), (30, 10))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
