"""Independent 32px profile of text-polonium-chemical-element-symbol-2655bf29.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '2655bf29-58fa-41d7-9d26-17149d8456f7'
SOURCE_PATH = 'icon_set/dist/text32/text-polonium-chemical-element-symbol-2655bf29.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2655bf29-58fa-41d7-9d26-17149d8456f7', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/po (text u)_2655bf29-58fa-41d7-9d26-17149d8456f7.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-polonium-chemical-element-symbol-2655bf29',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-o')
REFERENCE_EXPORT_SHA256 = 'f43dff4a965d9c139fc4b33c65f95ac7ddcfcba09625276d9aafd302bdefaf1f'

class Drawing(TextSub32):
    icon_id = 'text-polonium-chemical-element-symbol-2655bf29-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 37
    text_ink_bounds = (0.0, 0.0, 37.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (35, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (29, 21), ((32, 21), (35, 18), (35, 15)))
        self.add_bezier('p2-r1-2', (35, 15), ((35, 11), (32, 8), (29, 8)))
        self.add_bezier('p2-r1-3', (29, 8), ((25, 8), (22, 11), (22, 15)))
        self.add_bezier('p2-r1-4', (22, 15), ((22, 18), (25, 21), (29, 21)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 21), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (9, 2))
        self.add_bezier('p3-r1-3', (9, 2), ((13, 2), (15, 5), (15, 7)))
        self.add_bezier('p3-r1-4', (15, 7), ((15, 10), (13, 12), (9, 12)))
        self.add_line('p3-r1-5', (9, 12), (2, 12))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
