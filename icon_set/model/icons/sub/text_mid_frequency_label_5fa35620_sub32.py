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

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-mid-frequency-label-5fa35620-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (0.0, -1.9539862061712654e-06, 66.00000000000004, 20.0)

    def build(self):
        """Source-native uppercase composition for 'MID'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (2, 18), (2, 2.4248))
        self.add_bezier('p1-r1-2', (2, 2.4248), ((2, 2.01632), (2.53474, 1.84408), (2.78474, 2.17204)))
        self.add_line('p1-r1-3', (2.78474, 2.17204), (9.65053, 11.1787))
        self.add_bezier('p1-r1-4', (9.65053, 11.1787), ((9.82456, 11.407), (10.1754, 11.407), (10.3495, 11.1787)))
        self.add_line('p1-r1-5', (10.3495, 11.1787), (17.2153, 2.17204))
        self.add_bezier('p1-r1-6', (17.2153, 2.17204), ((17.4653, 1.84408), (18, 2.01632), (18, 2.4248)))
        self.add_line('p1-r1-7', (18, 2.4248), (18, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (40, 18), (28, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (40, 2), (28, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (34, 2), (34, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (52, 2), (56.88681, 2))
        self.add_bezier('p5-r1-2', (56.88681, 2), ((60.8153, 2), (64, 5.58172), (64, 10)))
        self.add_bezier('p5-r1-3', (64, 10), ((64, 14.4183), (60.8153, 18), (56.88681, 18)))
        self.add_line('p5-r1-4', (56.88681, 18), (52, 18))
        self.add_line('p5-r1-5', (52, 18), (52, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
        self.relate("connect", 'path-2-1', 'path-3-1')
        self.relate("connect", 'path-2-1', 'path-4-1')
        self.relate("connect", 'path-3-1', 'path-4-1')
