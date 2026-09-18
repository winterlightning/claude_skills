"""Independent 32px profile of text-new-label-text-indicator-bceaa99b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'bceaa99b-b0d8-47fc-bb91-5b01dcec3319'
SOURCE_PATH = 'icon_set/dist/text32/text-new-label-text-indicator-bceaa99b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bceaa99b-b0d8-47fc-bb91-5b01dcec3319', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/NEW_bceaa99b-b0d8-47fc-bb91-5b01dcec3319.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-new-label-text-indicator-bceaa99b',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-n-uppercase', 'letter-e-uppercase', 'letter-w-uppercase')
REFERENCE_EXPORT_SHA256 = 'f806a9d648fbd72c2325a2da9acd138301834863edd150c9a999b9f9e949e258'

class Drawing(TextSub32):
    icon_id = 'text-new-label-text-indicator-bceaa99b-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 87
    text_ink_bounds = (0.0, 0.0, 87.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (55, 2), (61, 28))
        self.add_bezier('p1-r1-2', (61, 28), ((61.666666666666664, 29.333333333333332), (62, 30), (62, 30)))
        self.add_bezier('p1-r1-3', (62, 30), ((62, 30), (62.333333333333336, 29.333333333333332), (63, 28)))
        self.add_line('p1-r1-4', (63, 28), (69, 4))
        self.add_bezier('p1-r1-5', (69, 4), ((69, 3.3333333333333335), (69.33333333333333, 3), (70, 3)))
        self.add_bezier('p1-r1-6', (70, 3), ((70, 3), (70.33333333333333, 3.3333333333333335), (71, 4)))
        self.add_line('p1-r1-7', (71, 4), (77, 28))
        self.add_bezier('p1-r1-8', (77, 28), ((77, 29.333333333333332), (77.33333333333333, 30), (78, 30)))
        self.add_bezier('p1-r1-9', (78, 30), ((78, 30), (78, 29.333333333333332), (78, 28)))
        self.add_line('p1-r1-10', (78, 28), (85, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (47, 2), (30, 2))
        self.add_line('p2-r1-2', (30, 2), (30, 30))
        self.add_line('p2-r1-3', (30, 30), (47, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (30, 16), (44, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 30), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (22, 30))
        self.add_line('p4-r1-3', (22, 30), (22, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
