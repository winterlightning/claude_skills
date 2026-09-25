"""Independent 32px profile of blind.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '5dce7e9a-2184-434a-9e94-71138d2b612d'
SOURCE_PATH = 'pictographic-primitives/interface-essential/blind_5dce7e9a-2184-434a-9e94-71138d2b612d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5dce7e9a-2184-434a-9e94-71138d2b612d', 'pictographic-primitives/interface-essential/blind_5dce7e9a-2184-434a-9e94-71138d2b612d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/blind',)
SOLO_SOURCE_ICON_IDS = ('blind',)
REFERENCE_EXPORT_SHA256 = 'de5bd426cf9070e4f9280e10ff9493847089e546ec1fd1352c5e39b2a582fe4b'

class DrawingContainerSymbol(Sub32):
    icon_id = 'blind-sub32-symbol'
    related_origin_icon_id = 'blind-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/blind-sub32'
    counterpart_icon_id = 'blind-sub32'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (6, 11), radius_x=18, radius_y=24, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (6, 11), (30, 16), radius_x=18, radius_y=24, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (30, 16), (26, 21), radius_x=18, radius_y=24, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (26, 21), (2, 16), radius_x=18, radius_y=24, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (6, 11), (27, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
