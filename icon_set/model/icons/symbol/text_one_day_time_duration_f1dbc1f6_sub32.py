"""Independent 32px profile of text-one-day-time-duration-f1dbc1f6.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'f1dbc1f6-7ce5-41b6-98fd-726c2d1d0f09'
SOURCE_PATH = 'icon_set/dist/text32/text-one-day-time-duration-f1dbc1f6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f1dbc1f6-7ce5-41b6-98fd-726c2d1d0f09', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/1day (text)_f1dbc1f6-7ce5-41b6-98fd-726c2d1d0f09.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-one-day-time-duration-f1dbc1f6',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-1', 'letter-d-uppercase', 'letter-a-uppercase', 'letter-y-uppercase')
REFERENCE_EXPORT_SHA256 = '4f7ffb7fa227a7b6472a230b24968c2788f90a12ebe33e4fe344076a582adbe3'

class Drawing(TextSub32):
    icon_id = 'text-one-day-time-duration-f1dbc1f6-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 122
    text_ink_bounds = (0.0, 0.0, 121.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (98, 2), (109, 17))
        self.add_line('p1-r1-2', (109, 17), (119, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (109, 17), (109, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (66, 30), (76, 3))
        self.add_bezier('p3-r1-2', (76, 3), ((76, 2.3333333333333335), (76.33333333333333, 2), (77, 2)))
        self.add_bezier('p3-r1-3', (77, 2), ((77, 2), (77.33333333333333, 2.3333333333333335), (78, 3)))
        self.add_line('p3-r1-4', (78, 3), (87, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (70, 18), (83, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (36, 2), (44, 2))
        self.add_bezier('p5-r1-2', (44, 2), ((52, 2), (56, 9), (56, 16)))
        self.add_bezier('p5-r1-3', (56, 16), ((56, 23), (52, 30), (44, 30)))
        self.add_line('p5-r1-4', (44, 30), (36, 30))
        self.add_line('p5-r1-5', (36, 30), (36, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
        self.add_line('p6-r1-1', (9, 30), (9, 3))
        self.add_bezier('p6-r1-2', (9, 3), ((9, 2), (8, 2), (8, 2)))
        self.add_line('p6-r1-3', (8, 2), (2, 2))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', closed=False)
        self.add_line('p7-r1-1', (2, 30), (15, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
