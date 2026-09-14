"""Steady down (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55a76902-250a-4829-8ffa-1b70dddc670b'
SOURCE_PATH = 'icons-json/arrows/steady down_55a76902-250a-4829-8ffa-1b70dddc670b.json'
AUTHOR = 'json_to_solo'

class SteadyDown55a76902(Solo48):
    icon_id = 'steady-down-55a76902'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('steady', 'down', 'arrows')

    def build(self):
        self.add_line('e0', (39, 38), (42, 38))
        self.add_line('e1', (38, 42), (42, 38))
        self.add_line('e2', (38, 34), (42, 38))
        self.add_arc('e3-1', (6, 6), (14, 26), radius_x=39, sweep=False)
        self.add_arc('e3-2', (14, 26), (39, 38), radius_x=32, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
