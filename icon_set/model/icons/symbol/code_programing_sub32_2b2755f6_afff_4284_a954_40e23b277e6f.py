"""Independent 32px profile of code-programing.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2b2755f6-afff-4284-a954-40e23b277e6f'
SOURCE_PATH = 'pictographic-primitives/programing/code_2b2755f6-afff-4284-a954-40e23b277e6f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2b2755f6-afff-4284-a954-40e23b277e6f', 'pictographic-primitives/programing/code_2b2755f6-afff-4284-a954-40e23b277e6f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/code-programing',)
SOLO_SOURCE_ICON_IDS = ('code-programing',)
REFERENCE_EXPORT_SHA256 = '828c31eb173125a2423d3d6b310d12ffc1d1d349051de06a9f3f39424ac10e01'

class Drawing(Sub32):
    icon_id = 'code-programing-sub32'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'programing'
    categories = ('programing', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Code: angle brackets with a slash between them, 4 units clear.
        self.add_line('slash', (15, 24), (17, 8))
        self.add_polyline('left', (7, 8), (2, 16), (7, 24))
        self.add_polyline('right', (25, 8), (30, 16), (25, 24))
