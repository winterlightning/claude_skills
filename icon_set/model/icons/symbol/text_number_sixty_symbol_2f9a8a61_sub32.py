"""Independent 32px profile of text-number-sixty-symbol-2f9a8a61.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '2f9a8a61-0167-41cb-9976-58634897032b'
SOURCE_PATH = 'icon_set/dist/text32/text-number-sixty-symbol-2f9a8a61.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2f9a8a61-0167-41cb-9976-58634897032b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/60 (text)_2f9a8a61-0167-41cb-9976-58634897032b.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-sixty-symbol-2f9a8a61',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-6', 'digit-0')
REFERENCE_EXPORT_SHA256 = '8322d9131239cde6f8f783c2c1301b11f3df255108f291896545939ad2de4e03'

class Drawing(TextSub32):
    icon_id = 'text-number-sixty-symbol-2f9a8a61-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 51
    text_ink_bounds = (0.0, 0.0, 51.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (29, 10), (49, 10), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (49, 10), (49, 22))
        self.add_arc('p1-r1-3', (49, 22), (29, 22), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (29, 22), (29, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (2, 22), (22, 22), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_arc('p2-r1-2', (22, 22), (2, 22), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 22), (2, 12))
        self.add_bezier('p3-r1-2', (2, 12), ((2, 6), (6, 2), (12, 2)))
        self.add_line('p3-r1-3', (12, 2), (19, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
