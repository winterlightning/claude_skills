"""Independent 32px profile of text-no-outlet-traffic-sign-41d30216.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '41d30216-b4f5-4dc3-8d59-6adf5e3f2bac'
SOURCE_PATH = 'icon_set/dist/text32/text-no-outlet-traffic-sign-41d30216.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('41d30216-b4f5-4dc3-8d59-6adf5e3f2bac', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/transportation/no outlet_41d30216-b4f5-4dc3-8d59-6adf5e3f2bac.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-no-outlet-traffic-sign-41d30216',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-n-uppercase', 'letter-o-uppercase', 'letter-o-uppercase', 'letter-u-uppercase', 'letter-t-uppercase', 'letter-l-uppercase', 'letter-e-uppercase', 'letter-t-uppercase')
REFERENCE_EXPORT_SHA256 = '1c34d06b5bda9fe35901ac8cc98f2253c7eebce8c19bb477d1f8eab89736d955'

class Drawing(TextSub32):
    icon_id = 'text-no-outlet-traffic-sign-41d30216-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 246
    text_ink_bounds = (0.0, 0.0, 246.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (222, 2), (244, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (233, 2), (233, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (211, 2), (194, 2))
        self.add_line('p3-r1-2', (194, 2), (194, 30))
        self.add_line('p3-r1-3', (194, 30), (211, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (194, 16), (208, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (167, 2), (167, 30))
        self.add_line('p5-r1-2', (167, 30), (184, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (135, 2), (157, 2))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (146, 2), (146, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (105, 2), (105, 20))
        self.add_bezier('p8-r1-2', (105, 20), ((105, 27), (110, 30), (115, 30)))
        self.add_bezier('p8-r1-3', (115, 30), ((120, 30), (125, 27), (125, 20)))
        self.add_line('p8-r1-4', (125, 20), (125, 2))
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', 'p8-r1-3', 'p8-r1-4', closed=False)
        self.add_bezier('p9-r1-1', (74, 16), ((74, 8), (79, 2), (84, 2)))
        self.add_bezier('p9-r1-2', (84, 2), ((90, 2), (94, 8), (94, 16)))
        self.add_bezier('p9-r1-3', (94, 16), ((94, 24), (90, 30), (84, 30)))
        self.add_bezier('p9-r1-4', (84, 30), ((79, 30), (74, 24), (74, 16)))
        self.add_contour('path-9-1', 'p9-r1-1', 'p9-r1-2', 'p9-r1-3', 'p9-r1-4', closed=False)
        self.add_bezier('p10-r1-1', (33, 16), ((33, 8), (37, 2), (43, 2)))
        self.add_bezier('p10-r1-2', (43, 2), ((48, 2), (53, 8), (53, 16)))
        self.add_bezier('p10-r1-3', (53, 16), ((53, 24), (48, 30), (43, 30)))
        self.add_bezier('p10-r1-4', (43, 30), ((37, 30), (33, 24), (33, 16)))
        self.add_contour('path-10-1', 'p10-r1-1', 'p10-r1-2', 'p10-r1-3', 'p10-r1-4', closed=False)
        self.add_line('p11-r1-1', (2, 30), (2, 2))
        self.add_line('p11-r1-2', (2, 2), (22, 30))
        self.add_line('p11-r1-3', (22, 30), (22, 2))
        self.add_contour('path-11-1', 'p11-r1-1', 'p11-r1-2', 'p11-r1-3', closed=False)
