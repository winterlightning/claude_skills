"""Independent 32px profile of icon.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6e799354-211d-4a17-873a-6f0ec808f6e8'
SOURCE_PATH = 'pictographic-primitives/state/@_6e799354-211d-4a17-873a-6f0ec808f6e8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6e799354-211d-4a17-873a-6f0ec808f6e8', 'pictographic-primitives/state/@_6e799354-211d-4a17-873a-6f0ec808f6e8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/icon',)
SOLO_SOURCE_ICON_IDS = ('icon',)
REFERENCE_EXPORT_SHA256 = '8865062af63d377d77ecb8d111323ea5fe148cabd78e85ab675b558823a91b9b'

class Drawing(Sub32):
    icon_id = 'icon-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (19, 29), (17, 30))
        self.add_bezier('p1-r1-2', (17, 30), ((16, 30), (15, 30), (15, 30)))
        self.add_bezier('p1-r1-3', (15, 30), ((14, 30), (13, 30), (12, 29)))
        self.add_bezier('p1-r1-4', (12, 29), ((6, 28), (2, 22), (2, 17)))
        self.add_bezier('p1-r1-5', (2, 17), ((2, 16), (2, 16), (2, 16)))
        self.add_bezier('p1-r1-6', (2, 16), ((2, 16), (2, 16), (2, 16)))
        self.add_bezier('p1-r1-7', (2, 16), ((2, 14), (2, 13), (3, 11)))
        self.add_bezier('p1-r1-8', (3, 11), ((5, 6), (10, 2), (16, 2)))
        self.add_bezier('p1-r1-9', (16, 2), ((16, 2), (16, 2), (16, 2)))
        self.add_bezier('p1-r1-10', (16, 2), ((16, 2), (17, 2), (17, 2)))
        self.add_bezier('p1-r1-11', (17, 2), ((24, 2), (30, 8), (30, 15)))
        self.add_bezier('p1-r1-12', (30, 15), ((30, 15), (30, 15), (30, 15)))
        self.add_bezier('p1-r1-13', (30, 15), ((30, 15), (30, 15), (30, 16)))
        self.add_bezier('p1-r1-14', (30, 16), ((30, 17), (30, 20), (28, 21)))
        self.add_bezier('p1-r1-15', (28, 21), ((28, 22), (26, 22), (25, 22)))
        self.add_bezier('p1-r1-16', (25, 22), ((25, 22), (24, 22), (24, 21)))
        self.add_line('p1-r1-17', (24, 21), (22, 19))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', closed=False)
        self.add_bezier('p2-r1-1', (22, 19), ((20, 21), (19, 22), (16, 22)))
        self.add_bezier('p2-r1-2', (16, 22), ((16, 22), (16, 22), (16, 22)))
        self.add_bezier('p2-r1-3', (16, 22), ((12, 22), (10, 19), (10, 16)))
        self.add_bezier('p2-r1-4', (10, 16), ((10, 15), (10, 14), (11, 13)))
        self.add_bezier('p2-r1-5', (11, 13), ((12, 11), (14, 10), (16, 10)))
        self.add_bezier('p2-r1-6', (16, 10), ((18, 10), (20, 10), (21, 12)))
        self.add_bezier('p2-r1-7', (21, 12), ((22, 13), (22, 15), (22, 16)))
        self.add_bezier('p2-r1-8', (22, 16), ((22, 17), (22, 18), (22, 19)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.relate("connect", 'p1-r1-17', 'p2-r1-1')
        self.relate("connect", 'p1-r1-17', 'p2-r1-8')
