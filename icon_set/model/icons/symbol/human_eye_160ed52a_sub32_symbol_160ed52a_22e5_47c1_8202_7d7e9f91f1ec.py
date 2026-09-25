"""Independent 32px profile of human-eye-160ed52a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '160ed52a-22e5-47c1-8202-7d7e9f91f1ec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/eye_160ed52a-22e5-47c1-8202-7d7e9f91f1ec.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('160ed52a-22e5-47c1-8202-7d7e9f91f1ec', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/eye_160ed52a-22e5-47c1-8202-7d7e9f91f1ec.svg'),)
PROFILE_SOURCE_KEYS = ('solo/human-eye-160ed52a',)
SOLO_SOURCE_ICON_IDS = ('human-eye-160ed52a',)
REFERENCE_EXPORT_SHA256 = '044e2ea9d57ea076a782adc06fc5517ca825163141babecee730f0f30d8070c2'

class DrawingContainerSymbol(Sub32):
    icon_id = 'human-eye-160ed52a-sub32-symbol'
    related_origin_icon_id = 'human-eye-160ed52a-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/human-eye-160ed52a-sub32'
    counterpart_icon_id = 'human-eye-160ed52a-sub32'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    categories = ('health', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=18, radius_y=24, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=18, radius_y=24, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (13, 16), (20, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (20, 16), (13, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
