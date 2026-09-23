"""Independent 32px profile of text-tiff-image-file-format-02af3840.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '02af3840-b8eb-40f6-b3ef-54661616285b'
SOURCE_PATH = 'icon_set/dist/text32/text-tiff-image-file-format-02af3840.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('02af3840-b8eb-40f6-b3ef-54661616285b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/TIFF (text)_02af3840-b8eb-40f6-b3ef-54661616285b.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-tiff-image-file-format-02af3840',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-t-uppercase', 'letter-i-uppercase', 'letter-f-uppercase', 'letter-f-uppercase')
REFERENCE_EXPORT_SHA256 = 'af0ba5f9d79256b8c42f88164cd6e0a4b9830640bc31955095a1c6aefae94b49'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-tiff-image-file-format-02af3840-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 92
    text_canvas_height = 20
    text_ink_bounds = (2.0, -1.3322676295501878e-15, 90.21000000000001, 20.0024)

    def build(self):
        """Source-native uppercase composition for 'TIFF'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (4, 2), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (10, 18), (10.0064, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (40, 18), (28, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (40, 2), (28, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (34, 2), (34, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (52.21094, 10.4907), (62.2337, 10.4907))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (52.20996, 18.0024), (52.20996, 2.3249))
        self.add_bezier('p7-r1-2', (52.20996, 2.3249), ((52.20996, 2.14546), (52.35542, 2), (52.53486, 2)))
        self.add_line('p7-r1-3', (52.53486, 2), (64.21000000000001, 2))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', closed=False)
        self.add_line('p8-r1-1', (76.21094, 10.4907), (86.2337, 10.4907))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (76.20996, 18.0024), (76.20996, 2.3249))
        self.add_bezier('p9-r1-2', (76.20996, 2.3249), ((76.20996, 2.14546), (76.35542, 2), (76.53486, 2)))
        self.add_line('p9-r1-3', (76.53486, 2), (88.21000000000001, 2))
        self.add_contour('path-9-1', 'p9-r1-1', 'p9-r1-2', 'p9-r1-3', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
        self.relate("connect", 'path-3-1', 'path-4-1')
        self.relate("connect", 'path-3-1', 'path-5-1')
        self.relate("connect", 'path-4-1', 'path-5-1')
        self.relate("connect", 'path-6-1', 'path-7-1')
        self.relate("connect", 'path-8-1', 'path-9-1')
