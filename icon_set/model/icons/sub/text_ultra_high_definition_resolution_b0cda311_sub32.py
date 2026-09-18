"""Independent 32px profile of text-ultra-high-definition-resolution-b0cda311.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'b0cda311-e543-4320-895b-b795fcc497b0'
SOURCE_PATH = 'icon_set/dist/text32/text-ultra-high-definition-resolution-b0cda311.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b0cda311-e543-4320-895b-b795fcc497b0', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/UHD (text)_b0cda311-e543-4320-895b-b795fcc497b0.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-ultra-high-definition-resolution-b0cda311',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-u-uppercase', 'letter-h-uppercase', 'letter-d-uppercase')
REFERENCE_EXPORT_SHA256 = '9af3165c5cc4f73382bcc00a3c83db429491a9580088660c325bc83fc8fc436d'

class Drawing(TextSub32):
    icon_id = 'text-ultra-high-definition-resolution-b0cda311-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 79
    text_ink_bounds = (0.0, 0.0, 79.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (58, 2), (66, 2))
        self.add_bezier('p1-r1-2', (66, 2), ((73, 2), (77, 9), (77, 16)))
        self.add_bezier('p1-r1-3', (77, 16), ((77, 23), (73, 30), (66, 30)))
        self.add_line('p1-r1-4', (66, 30), (58, 30))
        self.add_line('p1-r1-5', (58, 30), (58, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (30, 2), (30, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (50, 2), (50, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, 16), (50, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 2), (2, 20))
        self.add_bezier('p5-r1-2', (2, 20), ((2, 27), (7, 30), (12, 30)))
        self.add_bezier('p5-r1-3', (12, 30), ((17, 30), (22, 27), (22, 20)))
        self.add_line('p5-r1-4', (22, 20), (22, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
