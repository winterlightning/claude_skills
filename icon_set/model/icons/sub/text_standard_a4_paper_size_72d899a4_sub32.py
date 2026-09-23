"""V2 typeface composition for Standard A4 Paper Size."""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '72d899a4-6d14-40d7-81f0-a36e3773ca36'
SOURCE_PATH = 'published/gallery/combination-originals/72d899a4-6d14-40d7-81f0-a36e3773ca36.svg'
AUTHOR = 'codex'
SOURCE_REFERENCES = (('72d899a4-6d14-40d7-81f0-a36e3773ca36', 'published/gallery/combination-originals/72d899a4-6d14-40d7-81f0-a36e3773ca36.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-72d899a4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'digit-4')


REFERENCE_EXPORT_SHA256 = '560ac46f4de5e685136e6c4f96d98a13207b6ad3162653ce41435399824f88d4'






















TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-standard-a4-paper-size-72d899a4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 44
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 42.0, 20.0001)

    def build(self):
        """Source-native uppercase composition for 'A4'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (4, 18), ((4, 18), (5.26667, 2), (10.1333, 2)))
        self.add_bezier('p1-r1-2', (10.1333, 2), ((15, 2), (16, 18), (16, 18)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p1-r2-1', (4.49782, 13.9921), (15.5709, 14.0032))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
        self.add_line('p2-r1-1', (40, 12.8572), (28.40861, 12.8572))
        self.add_bezier('p2-r1-2', (28.40861, 12.8572), ((28.18045, 12.8572), (27.81423, 12.5715), (28.11142, 12.2858)))
        self.add_line('p2-r1-3', (28.11142, 12.2858), (37.622299999999996, 2.00009))
        self.add_line('p2-r1-4', (37.622299999999996, 2.00009), (37.622299999999996, 18.0001))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
