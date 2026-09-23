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

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-numerical-digit-nine-d938682c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 20
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 18.0005, 20.00000000000001)

    def build(self):
        """Source-native uppercase composition for '9'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (16.0005, 6.72498), (16.0005, 13.1172))
        self.add_bezier('p1-r1-2', (16.0005, 13.1172), ((16.0005, 15.8139), (13.8144, 18), (11.1177, 18)))
        self.add_line('p1-r1-3', (11.1177, 18), (5.62988, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_arc('p2-r1-1', (4, 6.80433), (16, 6.80433), radius_x=6, radius_y=4.80433, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (16, 6.80433), (4, 6.80433), radius_x=6, radius_y=4.80433, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
