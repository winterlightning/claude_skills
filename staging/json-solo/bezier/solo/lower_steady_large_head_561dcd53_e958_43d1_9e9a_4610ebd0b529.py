"""Lower steady large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e5', (6, 36), ((6, 36.409), (6.221, 37.165), (6.368, 37.541)), ((7.375, 40.159), (10.115, 41.992), (12.93, 41.992)), ((12.994, 41.992), (13.059, 42), (13.123, 42)), ((13.124, 42), (13.125, 42), (13.126, 42)), ((13.29, 42), (13.462, 41.992), (13.625, 41.992)), ((16.808, 41.992), (21, 38.33), (21, 35)))
        self.add_bezier('e6', (21, 25), ((21, 22.177), (24.39, 19), (27, 19)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
