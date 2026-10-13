"""Independent 32px profile of selection-square-handles.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '46c04fa9-89bb-45fb-bcaa-de2976c20dd6'
SOURCE_PATH = 'pictographic-primitives/symbol/square block_46c04fa9-89bb-45fb-bcaa-de2976c20dd6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('46c04fa9-89bb-45fb-bcaa-de2976c20dd6', 'pictographic-primitives/symbol/square block_46c04fa9-89bb-45fb-bcaa-de2976c20dd6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/selection-square-handles',)
SOLO_SOURCE_ICON_IDS = ('selection-square-handles',)
REFERENCE_EXPORT_SHA256 = '0c8ba87edf21c7b7111a9084ff327f0bf1ee4f36f110fedf9115467079fbc4c3'

class Drawing(Sub32):
    icon_id = 'selection-square-handles-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (10, 2))
        self.add_line('p1-r1-2', (10, 2), (10, 10))
        self.add_line('p1-r1-3', (10, 10), (2, 10))
        self.add_line('p1-r1-4', (2, 10), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (22, 2), (30, 2))
        self.add_line('p2-r1-2', (30, 2), (30, 10))
        self.add_line('p2-r1-3', (30, 10), (22, 10))
        self.add_line('p2-r1-4', (22, 10), (22, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (22, 22), (30, 22))
        self.add_line('p3-r1-2', (30, 22), (30, 30))
        self.add_line('p3-r1-3', (30, 30), (22, 30))
        self.add_line('p3-r1-4', (22, 30), (22, 22))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (2, 22), (10, 22))
        self.add_line('p4-r1-2', (10, 22), (10, 30))
        self.add_line('p4-r1-3', (10, 30), (2, 30))
        self.add_line('p4-r1-4', (2, 30), (2, 22))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (10, 6), (22, 6))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (26, 10), (26, 22))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (22, 26), (10, 26))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (6, 22), (6, 10))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
