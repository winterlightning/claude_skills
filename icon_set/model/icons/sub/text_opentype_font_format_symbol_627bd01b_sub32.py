"""Independent 32px profile of text-opentype-font-format-symbol-627bd01b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '627bd01b-45cf-459f-b69e-c79619557db2'
SOURCE_PATH = 'icon_set/dist/text32/text-opentype-font-format-symbol-627bd01b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('627bd01b-45cf-459f-b69e-c79619557db2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/otf (text)_627bd01b-45cf-459f-b69e-c79619557db2.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-opentype-font-format-symbol-627bd01b',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-o-uppercase', 'letter-t-uppercase', 'letter-f-uppercase')
REFERENCE_EXPORT_SHA256 = '04fba72429985eecb2a0bfe647442a519f03fa5504b852b196e87401ea6c89dd'

class Drawing(TextSub32):
    icon_id = 'text-opentype-font-format-symbol-627bd01b-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 79
    text_ink_bounds = (0.0, 0.0, 79.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (77, 2), (60, 2))
        self.add_line('p1-r1-2', (60, 2), (60, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (60, 16), (74, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (30, 2), (52, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (41, 2), (41, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_arc('p5-r1-1', (2, 16), (22, 16), radius_x=10, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('p5-r1-2', (22, 16), (2, 16), radius_x=10, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
