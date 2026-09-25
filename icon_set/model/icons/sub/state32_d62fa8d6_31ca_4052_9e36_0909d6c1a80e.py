"""Independent 32px profile of state32-d62fa8d6-31ca-4052-9e36-0909d6c1a80e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd62fa8d6-31ca-4052-9e36-0909d6c1a80e'
SOURCE_PATH = 'icon_set/assets/combination-state32/d62fa8d6-31ca-4052-9e36-0909d6c1a80e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d62fa8d6-31ca-4052-9e36-0909d6c1a80e', 'icon_set/assets/combination-state32/d62fa8d6-31ca-4052-9e36-0909d6c1a80e.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '237b404290df7c6bd1e500d872d549d2ec26344aafa8c861b1dd5f083c9da4df'

class Drawing(Sub32):
    icon_id = 'state32-d62fa8d6-31ca-4052-9e36-0909d6c1a80e'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 8), (22, 8))
        self.add_bezier('p1-r1-2', (22, 8), ((23.333333333333332, 8), (24, 8.666666666666666), (24, 10)))
        self.add_line('p1-r1-3', (24, 10), (24, 22))
        self.add_bezier('p1-r1-4', (24, 22), ((24, 23.333333333333332), (23.333333333333332, 24), (22, 24)))
        self.add_line('p1-r1-5', (22, 24), (10, 24))
        self.add_bezier('p1-r1-6', (10, 24), ((8.666666666666666, 24), (8, 23.333333333333332), (8, 22)))
        self.add_line('p1-r1-7', (8, 22), (8, 10))
        self.add_bezier('p1-r1-8', (8, 10), ((8, 8.666666666666666), (8.666666666666666, 8), (10, 8)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (12, 2), (12, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (12, 24), (12, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 12), (8, 12))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (24, 12), (30, 12))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (20, 2), (20, 8))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (20, 24), (20, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (2, 20), (8, 20))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (24, 20), (30, 20))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
