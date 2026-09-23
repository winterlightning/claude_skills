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































TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-camera-iso-sensitivity-icon-dc80c148-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 68.0, 20.000000000000004)

    def build(self):
        """Source-native uppercase composition for 'ISO'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (16, 18), (4, 18))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16, 2), (4, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (10, 2), (10, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (39.9314, 2), (32.77906, 2))
        self.add_bezier('p4-r1-2', (32.77906, 2), ((27.70172, 2), (26.21029, 7.42857), (30.98284, 9.42857)))
        self.add_line('p4-r1-3', (30.98284, 9.42857), (37.4623, 11.608))
        self.add_bezier('p4-r1-4', (37.4623, 11.608), ((41.7211, 13.4286), (40.2526, 18), (35.7787, 18)))
        self.add_line('p4-r1-5', (35.7787, 18), (28, 18))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_arc('p5-r1-1', (50, 10), (66, 10), radius_x=8, radius_y=8, large_arc=True, sweep=False)
        self.add_arc('p5-r1-2', (66, 10), (50, 10), radius_x=8, radius_y=8, large_arc=True, sweep=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
        self.relate("connect", 'path-1-1', 'path-3-1')
        self.relate("connect", 'path-2-1', 'path-3-1')
