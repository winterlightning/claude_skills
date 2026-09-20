# Independent container symbol; edit separately from linked side sub-icon.
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

class DrawingVariant2ContainerSymbol(TextSub32):
    icon_id = 'text-uppercase-letters-q-and-t-08bec648-sub32-v2-symbol'
    variant_of = 'text-uppercase-letters-q-and-t-08bec648-sub32-v2'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-uppercase-letters-q-and-t-08bec648-sub32-v2'
    counterpart_icon_id = 'text-uppercase-letters-q-and-t-08bec648-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 51
    text_ink_bounds = (0.0, 0.0, 51.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (29, 2), (49, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (39, 2), (39, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (2, 15), (20, 15), radius_x=9, radius_y=13, large_arc=True, sweep=True)
        self.add_arc('p3-r1-2', (20, 15), (2, 15), radius_x=9, radius_y=13, large_arc=True, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (14, 21), (22, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'path-3-1', 'path-4-1')
