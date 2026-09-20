"""Independent 32px profile of text-http-web-protocol-symbol-66c7680f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '66c7680f-d797-49cc-a62c-69dba4799c3a'
SOURCE_PATH = 'icon_set/dist/text32/text-http-web-protocol-symbol-66c7680f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('66c7680f-d797-49cc-a62c-69dba4799c3a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/http (text)_66c7680f-d797-49cc-a62c-69dba4799c3a.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-http-web-protocol-symbol-66c7680f',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-h-uppercase', 'letter-t-uppercase', 'letter-t-uppercase', 'letter-p-uppercase')
REFERENCE_EXPORT_SHA256 = '5859a96caed8f631efc7eba3d22f68e144594204660c0fd28959150646be8290'

class Drawing(TextSub32):
    icon_id = 'text-http-web-protocol-symbol-66c7680f-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 111
    text_ink_bounds = (0.0, 0.0, 111.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (89, 30), (89, 2))
        self.add_line('p1-r1-2', (89, 2), (99, 2))
        self.add_bezier('p1-r1-3', (99, 2), ((106, 2), (109, 6), (109, 9)))
        self.add_bezier('p1-r1-4', (109, 9), ((109, 13), (106, 17), (99, 17)))
        self.add_line('p1-r1-5', (99, 17), (89, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (60, 2), (81, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (71, 2), (71, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, 2), (52, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (41, 2), (41, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (2, 2), (2, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (22, 2), (22, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (2, 16), (22, 16))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
