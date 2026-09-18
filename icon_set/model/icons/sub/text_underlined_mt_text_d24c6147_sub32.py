"""Independent 32px profile of text-underlined-mt-text-d24c6147.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'd24c6147-77b6-469c-a884-91a184b5cafb'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-mt-text-d24c6147.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d24c6147-77b6-469c-a884-91a184b5cafb', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/mt (text u)_d24c6147-77b6-469c-a884-91a184b5cafb.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-mt-text-d24c6147',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-m-uppercase', 'letter-t')
REFERENCE_EXPORT_SHA256 = '97d229046c5c49255721db1a5d8afa3a06da5dfb2fe7c426d25e6d809f566efe'

class Drawing(TextSub32):
    icon_id = 'text-underlined-mt-text-d24c6147-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 38
    text_ink_bounds = (0.0, 0.0, 38.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (36, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (31, 3), ((31, 3), (31, 8), (31, 12)))
        self.add_bezier('p2-r1-2', (31, 12), ((31, 14), (31, 16), (31, 17)))
        self.add_bezier('p2-r1-3', (31, 17), ((31, 18), (31, 20), (33, 21)))
        self.add_bezier('p2-r1-4', (33, 21), ((33, 21), (34, 21), (35, 21)))
        self.add_bezier('p2-r1-5', (35, 21), ((35, 21), (36, 21), (36, 21)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (27, 8), (35, 8))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 21), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (11, 14))
        self.add_line('p4-r1-3', (11, 14), (20, 2))
        self.add_line('p4-r1-4', (20, 2), (20, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
