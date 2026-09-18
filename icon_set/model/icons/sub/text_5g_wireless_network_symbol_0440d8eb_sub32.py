"""Independent 32px profile of text-5g-wireless-network-symbol-0440d8eb.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '0440d8eb-b611-409c-b5fd-71315e26622e'
SOURCE_PATH = 'icon_set/dist/text32/text-5g-wireless-network-symbol-0440d8eb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0440d8eb-b611-409c-b5fd-71315e26622e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/5g (text)_0440d8eb-b611-409c-b5fd-71315e26622e.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-5g-wireless-network-symbol-0440d8eb',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-5', 'letter-g-uppercase')
REFERENCE_EXPORT_SHA256 = 'c63d250c4b2d7e388e1a177bc0e9e6afac9b8d9c1dc8028eac1234f9a79149c3'

class Drawing(TextSub32):
    icon_id = 'text-5g-wireless-network-symbol-0440d8eb-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 51
    text_ink_bounds = (0.0, 0.0, 51.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (47, 6), ((45, 4), (42, 2), (40, 2)))
        self.add_bezier('p1-r1-2', (40, 2), ((35, 2), (29, 9), (29, 17)))
        self.add_bezier('p1-r1-3', (29, 17), ((29, 18), (30, 20), (30, 21)))
        self.add_bezier('p1-r1-4', (30, 21), ((32, 27), (35, 29), (39, 29)))
        self.add_bezier('p1-r1-5', (39, 29), ((44, 29), (49, 24), (49, 16)))
        self.add_line('p1-r1-6', (49, 16), (42, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (19, 2), (3, 2))
        self.add_bezier('p2-r1-2', (3, 2), ((2, 2), (2, 2), (2, 3)))
        self.add_line('p2-r1-3', (2, 3), (2, 13))
        self.add_bezier('p2-r1-4', (2, 13), ((2, 13), (2, 14), (3, 14)))
        self.add_line('p2-r1-5', (3, 14), (13, 14))
        self.add_bezier('p2-r1-6', (13, 14), ((18, 14), (21, 18), (21, 22)))
        self.add_bezier('p2-r1-7', (21, 22), ((21, 24), (21, 26), (19, 28)))
        self.add_bezier('p2-r1-8', (19, 28), ((18, 29), (15, 30), (13, 30)))
        self.add_line('p2-r1-9', (13, 30), (3, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', closed=False)
