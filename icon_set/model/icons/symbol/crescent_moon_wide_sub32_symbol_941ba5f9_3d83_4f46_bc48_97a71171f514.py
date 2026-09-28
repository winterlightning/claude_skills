"""Independent 32px profile of crescent-moon-wide.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '941ba5f9-3d83-4f46-bc48-97a71171f514'
SOURCE_PATH = 'pictographic-primitives/symbol/moon_941ba5f9-3d83-4f46-bc48-97a71171f514.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('941ba5f9-3d83-4f46-bc48-97a71171f514', 'pictographic-primitives/symbol/moon_941ba5f9-3d83-4f46-bc48-97a71171f514.svg'), ('5b9c3b71-2b29-4560-8949-289b5ff5bd10', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/night_5b9c3b71-2b29-4560-8949-289b5ff5bd10.svg'), ('e385a617-1ac0-43e4-88e6-64ee12800ad1', 'pictographic-primitives/symbol/moon_e385a617-1ac0-43e4-88e6-64ee12800ad1.svg'))
PROFILE_SOURCE_KEYS = ('solo/crescent-moon-wide', 'solo/crescent-moon-rounded')
SOLO_SOURCE_ICON_IDS = ('crescent-moon-wide', 'crescent-moon-rounded')
REFERENCE_EXPORT_SHA256 = 'ee3a701c22efb4aef96aabbbe9471f66316e9f55be513342b5beea540dc3fdf0'

class DrawingContainerSymbol(Sub32):
    icon_id = 'crescent-moon-wide-sub32-symbol'
    related_origin_icon_id = 'crescent-moon-wide-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/crescent-moon-wide-sub32'
    counterpart_icon_id = 'crescent-moon-wide-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 2), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p1-r1-2', (2, 16), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (16, 30), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p1-r1-4', (30, 16), (16, 2), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
