# Variant of text-hqx-capital-letters-e167c65e-sub32; parent file remains unchanged.
"""Independent 32px profile of text-hqx-capital-letters-e167c65e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'e167c65e-bbc2-4b60-8391-90d28768985a'
SOURCE_PATH = 'icon_set/dist/text32/text-hqx-capital-letters-e167c65e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e167c65e-bbc2-4b60-8391-90d28768985a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/hqx (text)_e167c65e-bbc2-4b60-8391-90d28768985a.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-hqx-capital-letters-e167c65e',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-h-uppercase', 'letter-q-uppercase', 'letter-x-uppercase')
REFERENCE_EXPORT_SHA256 = '066abee6e2d2cd152f7e8db11cc440b3738931a507876cc140a93b1489f650bc'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class DrawingVariant2(TextSub32):
    icon_id = 'text-hqx-capital-letters-e167c65e-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 67.0, 20.0)

    def build(self):
        """Source-native uppercase composition for 'HQX'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (15.9998, 10), (4, 10))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16, 18), (15.9998, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p2-r2-1', (4.00021, 18), (4, 2))
        self.add_contour('path-2-2', 'p2-r2-1', closed=False)
        self.add_line('p3-r1-1', (35.143100000000004, 11.7143), (42.0002, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (26.00049, 9.42857), (40.85763, 9.42857), radius_x=7.42857, radius_y=7.42857, large_arc=True, sweep=False)
        self.add_arc('p4-r1-2', (40.85763, 9.42857), (26.00049, 9.42857), radius_x=7.42857, radius_y=7.42857, large_arc=True, sweep=False)
        self.add_line('p4-r1-3', (26.00049, 9.42857), (26.00049, 9.42857))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.add_line('p5-r1-1', (51, 2.00003), (65, 17.9909))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (51.02295, 18), (64.96379999999999, 2.04587))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
        self.relate("connect", 'path-3-1', 'path-4-1')
        self.relate("connect", 'path-5-1', 'path-6-1')
