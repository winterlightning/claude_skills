"""Independent 32px profile of text-letter-c-and-number-3-e25b306f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'e25b306f-5fbe-4a45-bb8e-44ae5a82269e'
SOURCE_PATH = 'icon_set/dist/text32/text-letter-c-and-number-3-e25b306f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e25b306f-5fbe-4a45-bb8e-44ae5a82269e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/C3 (text)_e25b306f-5fbe-4a45-bb8e-44ae5a82269e.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-letter-c-and-number-3-e25b306f',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'digit-3')
REFERENCE_EXPORT_SHA256 = '5463c0b5a91da01aa41abba9b645afbf036781a2196c0e989bf5c57e1695739d'

class Drawing(TextSub32):
    icon_id = 'text-letter-c-and-number-3-e25b306f-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 47
    text_ink_bounds = (0.001457877762348403, 0.0, 47.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (27, 2), (38, 2))
        self.add_bezier('p1-r1-2', (38, 2), ((42, 2), (45, 5), (45, 9)))
        self.add_bezier('p1-r1-3', (45, 9), ((45, 13), (42, 16), (38, 16)))
        self.add_line('p1-r1-4', (38, 16), (34, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (35, 16), (38, 16))
        self.add_bezier('p2-r1-2', (38, 16), ((42, 16), (45, 19), (45, 23)))
        self.add_bezier('p2-r1-3', (45, 23), ((45, 27), (42, 30), (38, 30)))
        self.add_line('p2-r1-4', (38, 30), (27, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_arc('p3-r1-1', (19, 6), (19, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
