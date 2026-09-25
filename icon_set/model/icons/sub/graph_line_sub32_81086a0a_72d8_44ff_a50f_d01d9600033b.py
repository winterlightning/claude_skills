"""Independent 32px profile of graph-line.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '81086a0a-72d8-44ff-a50f-d01d9600033b'
SOURCE_PATH = 'pictographic-primitives/business/graph line_81086a0a-72d8-44ff-a50f-d01d9600033b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('81086a0a-72d8-44ff-a50f-d01d9600033b', 'pictographic-primitives/business/graph line_81086a0a-72d8-44ff-a50f-d01d9600033b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/graph-line',)
SOLO_SOURCE_ICON_IDS = ('graph-line',)
REFERENCE_EXPORT_SHA256 = '224db364082c4fe9a1b19b728ed89e363fa7dc576af54c3761611420eb3d7c08'

class Drawing(Sub32):
    icon_id = 'graph-line-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'business'
    categories = ('primitives', 'business')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (23, 5), (30, 5))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (30, 5), (20, 20))
        self.add_arc('p2-r1-2', (20, 20), (19, 20), radius_x=20, radius_y=20, large_arc=False, sweep=False)
        self.add_line('p2-r1-3', (19, 20), (13, 12))
        self.add_line('p2-r1-4', (13, 12), (2, 27))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (30, 5), (30, 15))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
