"""Independent 32px profile of text-mov-video-file-format-a126e323.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'a126e323-d53b-4fec-a13c-409a222a15c7'
SOURCE_PATH = 'icon_set/dist/text32/text-mov-video-file-format-a126e323.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a126e323-d53b-4fec-a13c-409a222a15c7', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mov (text)_a126e323-d53b-4fec-a13c-409a222a15c7.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-mov-video-file-format-a126e323',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-m-uppercase', 'letter-o-uppercase', 'letter-v-uppercase')
REFERENCE_EXPORT_SHA256 = 'a6ff874c9a98595bedb02bf7e02a0a3ed48ae89a09af9d19a1995732fd07dfcf'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-mov-video-file-format-a126e323-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (0.0, -1.9539862061712654e-06, 66.9998, 20.000587807857475)

    def build(self):
        """Source-native uppercase composition for 'MOV'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (2, 18), (2, 2.4248))
        self.add_bezier('p1-r1-2', (2, 2.4248), ((2, 2.01632), (2.53474, 1.84408), (2.78474, 2.17204)))
        self.add_line('p1-r1-3', (2.78474, 2.17204), (9.65053, 11.1787))
        self.add_bezier('p1-r1-4', (9.65053, 11.1787), ((9.82456, 11.407), (10.1754, 11.407), (10.3495, 11.1787)))
        self.add_line('p1-r1-5', (10.3495, 11.1787), (17.2153, 2.17204))
        self.add_bezier('p1-r1-6', (17.2153, 2.17204), ((17.4653, 1.84408), (18, 2.01632), (18, 2.4248)))
        self.add_line('p1-r1-7', (18, 2.4248), (18, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_arc('p2-r1-1', (26, 10), (42, 10), radius_x=8, radius_y=8, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (42, 10), (26, 10), radius_x=8, radius_y=8, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (56.55127, 16.7027), ((56.704660000000004, 17.0778), (56.871719999999996, 17.3883), (57.04542, 17.617)))
        self.add_bezier('p3-r1-2', (57.04542, 17.617), ((57.20183, 17.7576), (57.44708, 17.8964), (57.70229, 17.9762)))
        self.add_bezier('p3-r1-3', (57.70229, 17.9762), ((57.95375, 18.0094), (58.137299999999996, 18.0049), (58.2933, 17.9853)))
        self.add_bezier('p3-r1-4', (58.2933, 17.9853), ((58.5154, 17.9252), (58.727000000000004, 17.828), (58.9257, 17.6775)))
        self.add_bezier('p3-r1-5', (58.9257, 17.6775), ((59.072, 17.5137), (59.1652, 17.3721), (59.2973, 17.1142)))
        self.add_line('p3-r1-6', (59.2973, 17.1142), (59.6865, 16.1038))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.add_line('p4-r1-1', (51, 2.02786), (56.552080000000004, 16.7029))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (59.6865, 16.1039), (64.9998, 2.00055))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'path-3-1', 'path-4-1')
        self.relate("connect", 'path-3-1', 'path-5-1')
        self.relate("connect", 'path-4-1', 'path-5-1')
