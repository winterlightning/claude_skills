# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-letters-y-and-m-ec50a81c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'ec50a81c-8df0-4c5c-b865-eaaf10e57c57'
SOURCE_PATH = 'icon_set/dist/text32/text-letters-y-and-m-ec50a81c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ec50a81c-8df0-4c5c-b865-eaaf10e57c57', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/ym (text)_ec50a81c-8df0-4c5c-b865-eaaf10e57c57.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-letters-y-and-m-ec50a81c',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-y-uppercase', 'letter-m')
REFERENCE_EXPORT_SHA256 = 'b3dc9aaaa33393013d58edd9404f2349837b5a0bc58f0592f4f28280d71d557e'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-letters-y-and-m-ec50a81c-sub32-symbol'
    variant_of = 'text-letters-y-and-m-ec50a81c-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-letters-y-and-m-ec50a81c-sub32'
    counterpart_icon_id = 'text-letters-y-and-m-ec50a81c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 62
    text_ink_bounds = (0.0, 0.0, 62.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (46, 18), (46, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (32, 30), (32, 18))
        self.add_bezier('p2-r1-2', (32, 18), ((32, 14), (35, 11), (39, 11)))
        self.add_bezier('p2-r1-3', (39, 11), ((42, 11), (46, 14), (46, 18)))
        self.add_bezier('p2-r1-4', (46, 18), ((46, 14), (49, 11), (53, 11)))
        self.add_bezier('p2-r1-5', (53, 11), ((56, 11), (60, 14), (60, 18)))
        self.add_line('p2-r1-6', (60, 18), (60, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (2, 2), (13, 17))
        self.add_line('p3-r1-2', (13, 17), (24, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (13, 17), (13, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-1', 'p2-r1-4')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
