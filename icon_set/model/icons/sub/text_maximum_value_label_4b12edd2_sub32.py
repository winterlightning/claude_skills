"""Independent 32px profile of text-maximum-value-label-4b12edd2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '4b12edd2-eaa6-4637-8b66-5e60cd53e0ed'
SOURCE_PATH = 'icon_set/dist/text32/text-maximum-value-label-4b12edd2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4b12edd2-eaa6-4637-8b66-5e60cd53e0ed', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/max (text)_4b12edd2-eaa6-4637-8b66-5e60cd53e0ed.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-maximum-value-label-4b12edd2',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-m-uppercase', 'letter-a-uppercase', 'letter-x-uppercase')
REFERENCE_EXPORT_SHA256 = 'f84f23d7a9eac6f0a95824594f43bd73ae9f85000f5fab747681dde6a55f3647'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-maximum-value-label-4b12edd2-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (0.0, -1.9539862061712654e-06, 67.0, 20.0)

    def build(self):
        """Source-native uppercase composition for 'MAX'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (2, 18), (2, 2.4248))
        self.add_bezier('p1-r1-2', (2, 2.4248), ((2, 2.01632), (2.53474, 1.84408), (2.78474, 2.17204)))
        self.add_line('p1-r1-3', (2.78474, 2.17204), (9.65053, 11.1787))
        self.add_bezier('p1-r1-4', (9.65053, 11.1787), ((9.82456, 11.407), (10.1754, 11.407), (10.3495, 11.1787)))
        self.add_line('p1-r1-5', (10.3495, 11.1787), (17.2153, 2.17204))
        self.add_bezier('p1-r1-6', (17.2153, 2.17204), ((17.4653, 1.84408), (18, 2.01632), (18, 2.4248)))
        self.add_line('p1-r1-7', (18, 2.4248), (18, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_bezier('p2-r1-1', (28, 18), ((28, 18), (29.26667, 2), (34.1333, 2)))
        self.add_bezier('p2-r1-2', (34.1333, 2), ((39, 2), (40, 18), (40, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p2-r2-1', (28.49782, 13.9921), (39.5709, 14.0032))
        self.add_contour('path-2-2', 'p2-r2-1', closed=False)
        self.add_line('p3-r1-1', (51, 2.00003), (65, 17.9909))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (51.02295, 18), (64.96379999999999, 2.04587))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'path-3-1', 'path-4-1')
