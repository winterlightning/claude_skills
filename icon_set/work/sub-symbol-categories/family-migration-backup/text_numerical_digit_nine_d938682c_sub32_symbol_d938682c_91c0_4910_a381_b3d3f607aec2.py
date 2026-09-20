# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-numerical-digit-nine-d938682c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'd938682c-91c0-4910-a381-b3d3f607aec2'
SOURCE_PATH = 'icon_set/dist/text32/text-numerical-digit-nine-d938682c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d938682c-91c0-4910-a381-b3d3f607aec2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/9 (text)_d938682c-91c0-4910-a381-b3d3f607aec2.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-numerical-digit-nine-d938682c',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-9',)
REFERENCE_EXPORT_SHA256 = '25492b5c3641881d3f5dcbc1eed85ee2001f93dc73b8797954a4717c9d26f524'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-numerical-digit-nine-d938682c-sub32-symbol'
    variant_of = 'text-numerical-digit-nine-d938682c-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-numerical-digit-nine-d938682c-sub32'
    counterpart_icon_id = 'text-numerical-digit-nine-d938682c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 24
    text_ink_bounds = (0.0, 0.0, 24.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (2, 10), (22, 10), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_arc('p1-r1-2', (22, 10), (2, 10), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (22, 10), (22, 20))
        self.add_bezier('p2-r1-2', (22, 20), ((22, 26), (17, 30), (12, 30)))
        self.add_line('p2-r1-3', (12, 30), (5, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
