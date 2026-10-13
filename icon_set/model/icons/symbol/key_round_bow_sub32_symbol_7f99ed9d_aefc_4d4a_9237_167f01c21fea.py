"""Independent 32px profile of key-round-bow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7f99ed9d-aefc-4d4a-9237-167f01c21fea'
SOURCE_PATH = 'pictographic-primitives/symbol/state key_7f99ed9d-aefc-4d4a-9237-167f01c21fea.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7f99ed9d-aefc-4d4a-9237-167f01c21fea', 'pictographic-primitives/symbol/state key_7f99ed9d-aefc-4d4a-9237-167f01c21fea.svg'), ('8d4e51db-4d2a-4285-a400-fd2f7b20a987', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-05/key_8d4e51db-4d2a-4285-a400-fd2f7b20a987.svg'))
PROFILE_SOURCE_KEYS = ('solo/key-round-bow',)
SOLO_SOURCE_ICON_IDS = ('key-round-bow',)
REFERENCE_EXPORT_SHA256 = '03bdc2b2de3f7f32bee53969b6cae062f640ce2cb12b8bc6469c35fbf2622cdb'

class DrawingContainerSymbol(Sub32):
    icon_id = 'key-round-bow-sub32-symbol'
    related_origin_icon_id = 'key-round-bow-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/key-round-bow-sub32'
    counterpart_icon_id = 'key-round-bow-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (21, 21), ((21, 26), (16, 30), (11, 30)))
        self.add_bezier('p1-r1-2', (11, 30), ((9, 30), (7, 29), (5, 27)))
        self.add_bezier('p1-r1-3', (5, 27), ((3, 25), (2, 23), (2, 21)))
        self.add_bezier('p1-r1-4', (2, 21), ((2, 16), (6, 11), (11, 11)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (11, 11), (21, 2))
        self.add_line('p2-r1-2', (21, 2), (30, 2))
        self.add_line('p2-r1-3', (30, 2), (30, 11))
        self.add_line('p2-r1-4', (30, 11), (21, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (9, 21), ((9, 19), (10, 18), (11, 18)))
        self.add_bezier('p3-r1-2', (11, 18), ((13, 18), (14, 19), (14, 21)))
        self.add_bezier('p3-r1-3', (14, 21), ((14, 22), (13, 23), (11, 23)))
        self.add_bezier('p3-r1-4', (11, 23), ((10, 23), (9, 22), (9, 21)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
