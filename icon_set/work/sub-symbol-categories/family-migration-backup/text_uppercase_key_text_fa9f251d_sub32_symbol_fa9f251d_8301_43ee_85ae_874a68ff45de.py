# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-uppercase-key-text-fa9f251d.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'fa9f251d-8301-43ee-85ae-874a68ff45de'
SOURCE_PATH = 'icon_set/dist/text32/text-uppercase-key-text-fa9f251d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fa9f251d-8301-43ee-85ae-874a68ff45de', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/key (text)_fa9f251d-8301-43ee-85ae-874a68ff45de.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-uppercase-key-text-fa9f251d',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-k-uppercase', 'letter-e-uppercase', 'letter-y-uppercase')
REFERENCE_EXPORT_SHA256 = '75ed9cc63ef03e2a525513e6a10757dd56e719eaa6502dcd8ac9883498e5adc1'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-uppercase-key-text-fa9f251d-sub32-symbol'
    variant_of = 'text-uppercase-key-text-fa9f251d-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-uppercase-key-text-fa9f251d-sub32'
    counterpart_icon_id = 'text-uppercase-key-text-fa9f251d-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 78
    text_ink_bounds = (0.0, 0.0, 78.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (54, 2), (65, 17))
        self.add_line('p1-r1-2', (65, 17), (76, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (65, 17), (65, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (46, 2), (29, 2))
        self.add_line('p3-r1-2', (29, 2), (29, 30))
        self.add_line('p3-r1-3', (29, 30), (46, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (29, 16), (43, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 2), (2, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (21, 2), (2, 17))
        self.add_line('p6-r1-2', (2, 17), (21, 30))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
