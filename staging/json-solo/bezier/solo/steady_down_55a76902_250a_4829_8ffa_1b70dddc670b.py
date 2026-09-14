"""Steady down (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e3', (6, 6), ((6.008, 6.025), (6.008, 6.049), (6.016, 6.082)), ((6.016, 6.646), (6.18, 7.235), (6.254, 7.792)), ((6.597, 10.295), (7.219, 12.791), (8.037, 15.18)), ((12.693, 28.803), (24.412, 38), (39, 38)))
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
