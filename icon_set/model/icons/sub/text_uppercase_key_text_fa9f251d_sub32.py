"""Independent 32px profile of text-uppercase-key-text-fa9f251d.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'fa9f251d-8301-43ee-85ae-874a68ff45de'
SOURCE_PATH = 'icon_set/dist/text32/text-uppercase-key-text-fa9f251d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fa9f251d-8301-43ee-85ae-874a68ff45de', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/key (text)_fa9f251d-8301-43ee-85ae-874a68ff45de.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-uppercase-key-text-fa9f251d',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-k-uppercase', 'letter-e-uppercase', 'letter-y-uppercase')
REFERENCE_EXPORT_SHA256 = '75ed9cc63ef03e2a525513e6a10757dd56e719eaa6502dcd8ac9883498e5adc1'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-uppercase-key-text-fa9f251d-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 68.0, 20.0)

    def build(self):
        """Source-native uppercase composition for 'KEY'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (4.01709, 2), (4.01709, 18))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16.0001, 17.889), (6.1001, 9.42859))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (14.8968, 2.09521), (4, 11.1429))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (40, 17.9999), (28.26183, 18))
        self.add_bezier('p4-r1-2', (28.26183, 18), ((28.11723, 18), (28, 17.8828), (28, 17.7382)))
        self.add_line('p4-r1-3', (28, 17.7382), (28, 9.98924))
        self.add_line('p4-r1-4', (28, 9.98924), (28, 2.01314))
        self.add_line('p4-r1-5', (28, 2.01314), (40, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (36.4, 10), (28, 10))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (66, 2), (57.98389, 10.5452))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (50, 2.05579), (57.98297, 10.5452))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (57.98296, 10.5453), (57.98145, 18))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
        self.relate("connect", 'path-1-1', 'path-3-1')
        self.relate("connect", 'path-2-1', 'path-3-1')
        self.relate("connect", 'path-4-1', 'path-5-1')
        self.relate("connect", 'path-6-1', 'path-7-1')
        self.relate("connect", 'path-6-1', 'path-8-1')
        self.relate("connect", 'path-7-1', 'path-8-1')
