"""Independent 32px profile of text-air-quality-index-ten-739b7594.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '739b7594-810f-489e-802a-e5f24cc60d9d'
SOURCE_PATH = 'icon_set/dist/text32/text-air-quality-index-ten-739b7594.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('739b7594-810f-489e-802a-e5f24cc60d9d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/10 AQI (text)_739b7594-810f-489e-802a-e5f24cc60d9d.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-air-quality-index-ten-739b7594',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-1', 'digit-0', 'letter-a-uppercase', 'letter-q-uppercase', 'letter-i-uppercase')
REFERENCE_EXPORT_SHA256 = 'bebec19886d0b87c15a373b8bc39f942a70af3590752fe9ee30f43f78a0cf0af'

class Drawing(TextSub32):
    icon_id = 'text-air-quality-index-ten-739b7594-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 130
    text_ink_bounds = (0.0, 0.0, 129.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (119, 2), (127, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (123, 2), (123, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (119, 27), (127, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (89, 15), ((89, 8), (93, 2), (98, 2)))
        self.add_bezier('p4-r1-2', (98, 2), ((103, 2), (108, 8), (108, 15)))
        self.add_bezier('p4-r1-3', (108, 15), ((108, 22), (103, 27), (98, 27)))
        self.add_bezier('p4-r1-4', (98, 27), ((93, 27), (89, 22), (89, 15)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (101, 21), (109, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (61, 27), (69, 3))
        self.add_bezier('p6-r1-2', (69, 3), ((69.66666666666667, 2.3333333333333335), (70, 2), (70, 2)))
        self.add_bezier('p6-r1-3', (70, 2), ((70.66666666666667, 2), (71, 2.3333333333333335), (71, 3)))
        self.add_line('p6-r1-4', (71, 3), (80, 27))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', closed=False)
        self.add_line('p7-r1-1', (64, 16), (76, 16))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_bezier('p8-r1-1', (24, 9), ((24, 5), (28, 2), (33, 2)))
        self.add_bezier('p8-r1-2', (33, 2), ((37, 2), (41, 5), (41, 9)))
        self.add_line('p8-r1-3', (41, 9), (41, 20))
        self.add_bezier('p8-r1-4', (41, 20), ((41, 24), (37, 27), (33, 27)))
        self.add_bezier('p8-r1-5', (33, 27), ((28, 27), (24, 24), (24, 20)))
        self.add_line('p8-r1-6', (24, 20), (24, 9))
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', 'p8-r1-3', 'p8-r1-4', 'p8-r1-5', 'p8-r1-6', closed=False)
        self.add_line('p9-r1-1', (8, 27), (8, 3))
        self.add_bezier('p9-r1-2', (8, 3), ((8, 2), (8, 2), (7, 2)))
        self.add_line('p9-r1-3', (7, 2), (2, 2))
        self.add_contour('path-9-1', 'p9-r1-1', 'p9-r1-2', 'p9-r1-3', closed=False)
        self.add_line('p10-r1-1', (2, 27), (14, 27))
        self.add_contour('path-10-1', 'p10-r1-1', closed=False)
