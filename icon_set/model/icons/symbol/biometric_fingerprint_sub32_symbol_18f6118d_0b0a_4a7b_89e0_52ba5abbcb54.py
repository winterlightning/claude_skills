"""Independent 32px profile of biometric-fingerprint.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '18f6118d-0b0a-4a7b-89e0-52ba5abbcb54'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/fingerprint_18f6118d-0b0a-4a7b-89e0-52ba5abbcb54.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('18f6118d-0b0a-4a7b-89e0-52ba5abbcb54', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/fingerprint_18f6118d-0b0a-4a7b-89e0-52ba5abbcb54.svg'),)
PROFILE_SOURCE_KEYS = ('solo/biometric-fingerprint',)
SOLO_SOURCE_ICON_IDS = ('biometric-fingerprint',)
REFERENCE_EXPORT_SHA256 = 'fd061383d4724e84344b7d1a07e4103e71c657c50ff4965ed041db3987e1c4aa'

class DrawingContainerSymbol(Sub32):
    icon_id = 'biometric-fingerprint-sub32-symbol'
    related_origin_icon_id = 'biometric-fingerprint-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/biometric-fingerprint-sub32'
    counterpart_icon_id = 'biometric-fingerprint-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Fingerprint: two concentric ridges 8 units apart (three cannot keep 4 units at this size).
        self.add_line('p1-r1-1', (2, 24), (2, 16))
        self.add_arc('p1-r1-2', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 16), (30, 24))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (10, 30), (10, 16))
        self.add_arc('p2-r1-2', (10, 16), (22, 16), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (22, 16), (22, 28))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
