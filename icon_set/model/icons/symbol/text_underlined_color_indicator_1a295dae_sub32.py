"""Independent 32px profile of text-underlined-color-indicator-1a295dae.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '1a295dae-51a7-4b2e-b79e-e90d2d2be701'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-color-indicator-1a295dae.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1a295dae-51a7-4b2e-b79e-e90d2d2be701', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/co (text u)_1a295dae-51a7-4b2e-b79e-e90d2d2be701.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-color-indicator-1a295dae',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-o')
REFERENCE_EXPORT_SHA256 = '128ce011f30b9f53c9a51bb78c83ab8415d3f16af9440f2b0bbb47a9732f95fc'

class Drawing(TextSub32):
    icon_id = 'text-underlined-color-indicator-1a295dae-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 36
    text_ink_bounds = (0.0, 0.0, 36.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (34, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (27, 21), ((31, 21), (34, 18), (34, 15)))
        self.add_bezier('p2-r1-2', (34, 15), ((34, 11), (31, 8), (27, 8)))
        self.add_bezier('p2-r1-3', (27, 8), ((23, 8), (20, 11), (20, 15)))
        self.add_bezier('p2-r1-4', (20, 15), ((20, 18), (23, 21), (27, 21)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (14, 5), ((12, 3), (11, 2), (9, 2)))
        self.add_bezier('p3-r1-2', (9, 2), ((6, 2), (2, 6), (2, 12)))
        self.add_bezier('p3-r1-3', (2, 12), ((2, 17), (6, 21), (9, 21)))
        self.add_bezier('p3-r1-4', (9, 21), ((11, 21), (12, 20), (14, 18)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
