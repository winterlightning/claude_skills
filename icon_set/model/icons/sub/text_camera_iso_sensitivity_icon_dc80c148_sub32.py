"""Independent 32px profile of text-camera-iso-sensitivity-icon-dc80c148.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'dc80c148-de1e-4700-9ef2-909189454c97'
SOURCE_PATH = 'icon_set/dist/text32/text-camera-iso-sensitivity-icon-dc80c148.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dc80c148-de1e-4700-9ef2-909189454c97', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/iso (text)_dc80c148-de1e-4700-9ef2-909189454c97.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-camera-iso-sensitivity-icon-dc80c148',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-i-uppercase', 'letter-s-uppercase', 'letter-o-uppercase')
REFERENCE_EXPORT_SHA256 = 'b8359e794cdac03f54c7af35e983fbec36e5c3dce8c45ddea58948e0a2a3d10f'

class Drawing(TextSub32):
    icon_id = 'text-camera-iso-sensitivity-icon-dc80c148-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 68
    text_ink_bounds = (0.0, 0.0, 68.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (45, 16), ((45, 8), (50, 2), (56, 2)))
        self.add_bezier('p1-r1-2', (56, 2), ((61, 2), (66, 8), (66, 16)))
        self.add_bezier('p1-r1-3', (66, 16), ((66, 24), (61, 30), (56, 30)))
        self.add_bezier('p1-r1-4', (56, 30), ((50, 30), (45, 24), (45, 16)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (37, 6), ((36, 3), (32, 2), (29, 2)))
        self.add_bezier('p2-r1-2', (29, 2), ((25, 2), (21, 4), (20, 9)))
        self.add_bezier('p2-r1-3', (20, 9), ((20, 9), (20, 9), (20, 10)))
        self.add_bezier('p2-r1-4', (20, 10), ((20, 17), (37, 13), (38, 22)))
        self.add_bezier('p2-r1-5', (38, 22), ((38, 22), (38, 22), (38, 23)))
        self.add_bezier('p2-r1-6', (38, 23), ((38, 28), (33, 30), (28, 30)))
        self.add_bezier('p2-r1-7', (28, 30), ((25, 30), (21, 29), (19, 26)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_line('p3-r1-1', (2, 2), (11, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (7, 2), (7, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 30), (11, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
