"""Independent 32px profile of text-letters-y-and-m-ec50a81c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'ec50a81c-8df0-4c5c-b865-eaaf10e57c57'
SOURCE_PATH = 'icon_set/dist/text32/text-letters-y-and-m-ec50a81c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ec50a81c-8df0-4c5c-b865-eaaf10e57c57', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/ym (text)_ec50a81c-8df0-4c5c-b865-eaaf10e57c57.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-letters-y-and-m-ec50a81c',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-y-uppercase', 'letter-m-uppercase')
REFERENCE_EXPORT_SHA256 = 'b3dc9aaaa33393013d58edd9404f2349837b5a0bc58f0592f4f28280d71d557e'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-letters-y-and-m-ec50a81c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 44
    text_canvas_height = 20
    text_ink_bounds = (0.0, -1.9539862061712654e-06, 44.0, 20.0)

    def build(self):
        """Source-native uppercase composition for 'YM'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (18, 2), (9.98389, 10.5452))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 2.05579), (9.98297, 10.5452))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (9.98296, 10.5453), (9.98145, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (26, 18), (26, 2.4248))
        self.add_bezier('p4-r1-2', (26, 2.4248), ((26, 2.01632), (26.53474, 1.84408), (26.78474, 2.17204)))
        self.add_line('p4-r1-3', (26.78474, 2.17204), (33.65053, 11.1787))
        self.add_bezier('p4-r1-4', (33.65053, 11.1787), ((33.82456, 11.407), (34.175399999999996, 11.407), (34.3495, 11.1787)))
        self.add_line('p4-r1-5', (34.3495, 11.1787), (41.2153, 2.17204))
        self.add_bezier('p4-r1-6', (41.2153, 2.17204), ((41.4653, 1.84408), (42, 2.01632), (42, 2.4248)))
        self.add_line('p4-r1-7', (42, 2.4248), (42, 18))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
        self.relate("connect", 'path-1-1', 'path-3-1')
        self.relate("connect", 'path-2-1', 'path-3-1')
