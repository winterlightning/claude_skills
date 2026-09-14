"""Lower steady large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '561dcd53-e958-43d1-9e9a-4610ebd0b529'
SOURCE_PATH = 'icons-json/arrows/lower steady large head_561dcd53-e958-43d1-9e9a-4610ebd0b529.json'
AUTHOR = 'json_to_solo'

class LowerSteadyLargeHeadArrows(Solo48):
    icon_id = 'lower-steady-large-head-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('lower', 'steady', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (6, 6), (6, 36))
        self.add_line('e1', (21, 35), (21, 25))
        self.add_line('e2', (27, 19), (42, 19))
        self.add_line('e3', (35, 26), (42, 19))
        self.add_line('e4', (35, 12), (42, 19))
        self.add_arc('e5-1', (6, 36), (13, 42), radius_x=8, sweep=False)
        self.add_line('e5-2', (13, 42), (17, 41))
        self.add_arc('e5-3', (17, 41), (21, 35), radius_x=6, sweep=False)
        self.add_arc('e6', (21, 25), (27, 19), radius_x=7)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e1', 'e6', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
