"""Independent 32px profile of tall-crescent-moon.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'ab11dce4-bd70-5a18-b77d-6f0e04cf719c'
SOURCE_PATH = 'pictographic-primitives/weather/night moon gibbous_ab11dce4-bd70-5a18-b77d-6f0e04cf719c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ab11dce4-bd70-5a18-b77d-6f0e04cf719c', 'pictographic-primitives/weather/night moon gibbous_ab11dce4-bd70-5a18-b77d-6f0e04cf719c.svg'), ('65e05ed7-b793-4969-b4cd-b8618a5b69d3', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/night_65e05ed7-b793-4969-b4cd-b8618a5b69d3.svg'))
PROFILE_SOURCE_KEYS = ('solo/tall-crescent-moon',)
SOLO_SOURCE_ICON_IDS = ('tall-crescent-moon',)
REFERENCE_EXPORT_SHA256 = 'd4bdd3bcaea9bac5ad527af69259d952a5d74b50ce11f4c85d865d3168e9ce51'

class DrawingContainerSymbol(Sub32):
    icon_id = 'tall-crescent-moon-sub32-symbol'
    related_origin_icon_id = 'tall-crescent-moon-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/tall-crescent-moon-sub32'
    counterpart_icon_id = 'tall-crescent-moon-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'weather'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (27, 2), ((15, 2), (5, 8), (5, 16)))
        self.add_bezier('p1-r1-2', (5, 16), ((5, 24), (15, 30), (27, 30)))
        self.add_bezier('p1-r1-3', (27, 30), ((23, 27), (20, 22), (20, 16)))
        self.add_bezier('p1-r1-4', (20, 16), ((20, 10), (23, 5), (27, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
