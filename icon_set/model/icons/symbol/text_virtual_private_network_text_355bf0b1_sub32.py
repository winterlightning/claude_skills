"""Independent 32px profile of text-virtual-private-network-text-355bf0b1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '355bf0b1-d1a1-4408-b75a-628f1ed00e52'
SOURCE_PATH = 'icon_set/dist/text32/text-virtual-private-network-text-355bf0b1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('355bf0b1-d1a1-4408-b75a-628f1ed00e52', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/VPN_355bf0b1-d1a1-4408-b75a-628f1ed00e52.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-virtual-private-network-text-355bf0b1',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-v-uppercase', 'letter-p-uppercase', 'letter-n-uppercase')
REFERENCE_EXPORT_SHA256 = '05fe41f3ce3a9fdfc4c3a4955e1cd7417d81380f2850e9f6ff5a98a77c132ace'

class Drawing(TextSub32):
    icon_id = 'text-virtual-private-network-text-355bf0b1-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 81
    text_ink_bounds = (0.0, 0.0, 81.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (58, 30), (58, 2))
        self.add_line('p1-r1-2', (58, 2), (79, 30))
        self.add_line('p1-r1-3', (79, 30), (79, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (31, 30), (31, 2))
        self.add_line('p2-r1-2', (31, 2), (41, 2))
        self.add_bezier('p2-r1-3', (41, 2), ((47, 2), (50, 6), (50, 9)))
        self.add_bezier('p2-r1-4', (50, 9), ((50, 13), (47, 17), (41, 17)))
        self.add_line('p2-r1-5', (41, 17), (31, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (2, 2), (11, 28))
        self.add_bezier('p3-r1-2', (11, 28), ((11.666666666666666, 29.333333333333332), (12.333333333333334, 30), (13, 30)))
        self.add_bezier('p3-r1-3', (13, 30), ((13, 30), (13.333333333333334, 29.333333333333332), (14, 28)))
        self.add_line('p3-r1-4', (14, 28), (23, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
