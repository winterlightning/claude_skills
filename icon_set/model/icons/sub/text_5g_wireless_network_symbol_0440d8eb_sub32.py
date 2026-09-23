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


































TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-5g-wireless-network-symbol-0440d8eb-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 44
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 44.00000000000002, 20.00000000000001)

    def build(self):
        """Source-native uppercase composition for '5G'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (15.1498, 2.00001), (4.54829, 2.00001))
        self.add_bezier('p1-r1-2', (4.54829, 2.00001), ((4.24548, 2.00001), (4, 2.20899), (4, 2.46678)))
        self.add_line('p1-r1-3', (4, 2.46678), (4, 8.20519))
        self.add_bezier('p1-r1-4', (4, 8.20519), ((4, 8.46299), (4.24548, 8.67197), (4.54829, 8.67197)))
        self.add_line('p1-r1-5', (4.54829, 8.67197), (10.5106, 8.67197))
        self.add_bezier('p1-r1-6', (10.5106, 8.67197), ((15.3427, 8.67197), (17.8085, 13.6102), (14.4555, 16.5724)))
        self.add_bezier('p1-r1-7', (14.4555, 16.5724), ((13.4229, 17.4846), (11.9988, 18), (10.5106, 18)))
        self.add_line('p1-r1-8', (10.5106, 18), (4.60888, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_bezier('p2-r1-1', (38.8699, 3.51954), ((37.5334, 2.56364), (35.8896, 2), (34.1123, 2)))
        self.add_bezier('p2-r1-2', (34.1123, 2), ((29.631990000000002, 2), (26, 5.58172), (26, 10)))
        self.add_bezier('p2-r1-3', (26, 10), ((26, 14.4183), (29.631990000000002, 18), (34.1123, 18)))
        self.add_bezier('p2-r1-4', (34.1123, 18), ((38.373599999999996, 18), (41.6686, 14.5166), (42, 10.3983)))
        self.add_line('p2-r1-5', (42, 10.3983), (35.9716, 10.3983))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
