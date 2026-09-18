"""Independent 32px profile of text-mid-frequency-label-5fa35620.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '5fa35620-2fcb-44a7-abec-ee26db38fc8d'
SOURCE_PATH = 'icon_set/dist/text32/text-mid-frequency-label-5fa35620.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5fa35620-2fcb-44a7-abec-ee26db38fc8d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/mid (text)_5fa35620-2fcb-44a7-abec-ee26db38fc8d.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-mid-frequency-label-5fa35620',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-m-uppercase', 'letter-i-uppercase', 'letter-d-uppercase')
REFERENCE_EXPORT_SHA256 = '40c7e7d5d932fb4183880f925d2df8e26a8f3656313fc78afd104acd9ef02456'

class Drawing(TextSub32):
    icon_id = 'text-mid-frequency-label-5fa35620-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 75
    text_ink_bounds = (0.0, 0.0, 75.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (53, 2), (61, 2))
        self.add_bezier('p1-r1-2', (61, 2), ((69, 2), (73, 9), (73, 16)))
        self.add_bezier('p1-r1-3', (73, 16), ((73, 23), (69, 30), (61, 30)))
        self.add_line('p1-r1-4', (61, 30), (53, 30))
        self.add_line('p1-r1-5', (53, 30), (53, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (36, 2), (46, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (41, 2), (41, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (36, 30), (46, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 30), (2, 2))
        self.add_line('p5-r1-2', (2, 2), (15, 20))
        self.add_line('p5-r1-3', (15, 20), (28, 2))
        self.add_line('p5-r1-4', (28, 2), (28, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
