"""Independent 32px profile of canoe-and-paddle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7b8e9bf7-9bed-5b92-918e-e02031e1e3e3'
SOURCE_PATH = 'pictographic-primitives/outdoors/canoe single_7b8e9bf7-9bed-5b92-918e-e02031e1e3e3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7b8e9bf7-9bed-5b92-918e-e02031e1e3e3', 'pictographic-primitives/outdoors/canoe single_7b8e9bf7-9bed-5b92-918e-e02031e1e3e3.svg'), ('18ef3c0c-f96b-4a36-b74d-e15aada31f40', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/canoe paddle_18ef3c0c-f96b-4a36-b74d-e15aada31f40.svg'))
PROFILE_SOURCE_KEYS = ('solo/canoe-and-paddle',)
SOLO_SOURCE_ICON_IDS = ('canoe-and-paddle',)
REFERENCE_EXPORT_SHA256 = 'c2006b5886003bd202267871505c8f18afff49910a68eb6479e0650f5ad3b651'

class Drawing(Sub32):
    icon_id = 'canoe-and-paddle-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Canoe (top view, pointed both ends, one thwart) beside a double-bladed paddle.
        self.add_bezier('hull-r', (24, 2), ((32, 8), (32, 24), (24, 30)))
        self.add_bezier('hull-l', (24, 30), ((16, 24), (16, 8), (24, 2)))
        self.add_contour('hull', 'hull-r', 'hull-l', closed=True)
        self.add_line('thwart', (18, 16), (30, 16))
        self.add_polyline('blade-top', (2, 2), (10, 2), (10, 8), (6, 12), (2, 8), closed=True)
        self.add_polyline('blade-bottom', (2, 30), (10, 30), (10, 24), (6, 20), (2, 24), closed=True)
        self.add_line('shaft', (6, 12), (6, 20))
        self.relate('connect', 'hull', 'thwart')
        self.relate('connect', 'blade-top', 'shaft')
        self.relate('connect', 'blade-bottom', 'shaft')
