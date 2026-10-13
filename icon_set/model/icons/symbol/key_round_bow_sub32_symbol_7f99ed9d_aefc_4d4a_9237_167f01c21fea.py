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
        # Key on the diagonal: round bow, straight shaft and two teeth.
        self.add_arc('bow-1', (2, 23), (16, 23), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('bow-2', (16, 23), (2, 23), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('bow', 'bow-1', 'bow-2', closed=True)
        self.add_line('shaft', (14, 18), (30, 2))
        self.add_line('tooth-1', (26, 6), (29, 9))
        self.add_line('tooth-2', (20, 12), (23, 15))
        self.relate('connect', 'bow', 'shaft')
        self.relate('connect', 'shaft', 'tooth-1')
        self.relate('connect', 'shaft', 'tooth-2')
