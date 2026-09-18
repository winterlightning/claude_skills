"""Independent 32px profile of state32-063ab342-3eb9-4c77-b5e5-59de1a294e59.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '063ab342-3eb9-4c77-b5e5-59de1a294e59'
SOURCE_PATH = 'icon_set/assets/combination-state32/063ab342-3eb9-4c77-b5e5-59de1a294e59.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('063ab342-3eb9-4c77-b5e5-59de1a294e59', 'icon_set/assets/combination-state32/063ab342-3eb9-4c77-b5e5-59de1a294e59.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '33ab7b0e6c44f0f7e36a7ad00d3490162d8213cc758c88090eaf9eab58f3fe7c'

class Drawing(Sub32):
    icon_id = 'state32-063ab342-3eb9-4c77-b5e5-59de1a294e59'
    keyshape = Keyshape.HRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 7), (19, 7))
        self.add_bezier('p1-r1-2', (19, 7), ((21, 7), (22, 8), (22, 10)))
        self.add_line('p1-r1-3', (22, 10), (22, 22))
        self.add_bezier('p1-r1-4', (22, 22), ((22, 24), (21, 25), (19, 25)))
        self.add_line('p1-r1-5', (19, 25), (5, 25))
        self.add_bezier('p1-r1-6', (5, 25), ((3, 25), (2, 24), (2, 22)))
        self.add_line('p1-r1-7', (2, 22), (2, 10))
        self.add_bezier('p1-r1-8', (2, 10), ((2, 8), (3, 7), (5, 7)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (22, 12), (30, 8))
        self.add_line('p2-r1-2', (30, 8), (30, 24))
        self.add_line('p2-r1-3', (30, 24), (22, 20))
        self.add_line('p2-r1-4', (22, 20), (22, 12))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
