"""Independent 32px profile of text-rtf-rich-text-format-091610fa.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '091610fa-d7cb-489a-a93c-f4c162f7022f'
SOURCE_PATH = 'icon_set/dist/text32/text-rtf-rich-text-format-091610fa.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('091610fa-d7cb-489a-a93c-f4c162f7022f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/rtf (text)_091610fa-d7cb-489a-a93c-f4c162f7022f.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-rtf-rich-text-format-091610fa',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-r-uppercase', 'letter-t-uppercase', 'letter-f-uppercase')
REFERENCE_EXPORT_SHA256 = '45277d8a98fcc331465b2683d679891edcea412a4fe62202236e5a9bcf527649'

class Drawing(TextSub32):
    icon_id = 'text-rtf-rich-text-format-091610fa-sub32'
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
        self.add_line('p5-r1-1', (2, 30), (2, 2))
        self.add_line('p5-r1-2', (2, 2), (12, 2))
        self.add_bezier('p5-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p5-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p5-r1-5', (12, 17), (2, 17))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
        self.add_line('p6-r1-1', (12, 17), (22, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'p5-r1-4', 'p6-r1-1')
        self.relate("connect", 'p5-r1-5', 'p6-r1-1')
