# Variant of text-uppercase-letters-q-and-t-08bec648-sub32; parent file remains unchanged.
"""Independent 32px profile of text-uppercase-letters-q-and-t-08bec648.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '08bec648-2d52-4612-97b2-467c1570d4eb'
SOURCE_PATH = 'icon_set/dist/text32/text-uppercase-letters-q-and-t-08bec648.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('08bec648-2d52-4612-97b2-467c1570d4eb', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/qt (text)_08bec648-2d52-4612-97b2-467c1570d4eb.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-uppercase-letters-q-and-t-08bec648',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-q-uppercase', 'letter-t-uppercase')
REFERENCE_EXPORT_SHA256 = '00c601065f41e297a42e07f881d16725bc761f426cc4218a7f80b80e9cb02654'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class DrawingVariant2(TextSub32):
    icon_id = 'text-uppercase-letters-q-and-t-08bec648-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 44
    text_canvas_height = 20
    text_ink_bounds = (0.0004900000000001015, 0.0, 42.0, 20.0)

    def build(self):
        """Source-native uppercase composition for 'QT'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (11.1431, 11.7143), (18.0002, 18))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_arc('p2-r1-1', (2.00049, 9.42857), (16.85763, 9.42857), radius_x=7.42857, radius_y=7.42857, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (16.85763, 9.42857), (2.000490000000001, 9.42857), radius_x=7.42857, radius_y=7.42857, large_arc=True, sweep=False)
        self.add_line('p2-r1-3', (2.000490000000001, 9.42857), (2.00049, 9.42857))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (28, 2), (40, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (34, 18), (34.0064, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
        self.relate("connect", 'path-3-1', 'path-4-1')
