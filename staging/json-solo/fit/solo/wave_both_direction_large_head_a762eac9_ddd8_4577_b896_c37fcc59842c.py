"""Wave both direction large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a762eac9-ddd8-4577-b896-c37fcc59842c'
SOURCE_PATH = 'icons-json/arrows/wave both direction large head_a762eac9-ddd8-4577-b896-c37fcc59842c.json'
AUTHOR = 'json_to_solo'

class WaveBothDirectionLargeHeadArrows(Solo48):
    icon_id = 'wave-both-direction-large-head-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('wave', 'both', 'direction', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (35, 6), (42, 12))
        self.add_line('e1', (13, 31), (6, 36))
        self.add_line('e2', (13, 42), (6, 36))
        self.add_line('e3', (36, 17), (42, 12))
        self.add_line('e4', (42, 12), (21, 12))
        self.add_line('e5', (22, 23), (25, 23))
        self.add_line('e6', (26, 36), (6, 36))
        self.add_arc('e7-1', (21, 12), (16, 18), radius_x=5, sweep=False)
        self.add_arc('e7-2', (16, 18), (22, 23), radius_x=6, sweep=False)
        self.add_arc('e8-1', (25, 23), (32, 30), radius_x=8)
        self.add_arc('e8-2', (32, 30), (26, 36), radius_x=6)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e7-1', 'e7-2', 'e5', 'e8-1', 'e8-2', 'e6')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
