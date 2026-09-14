"""Astronomy planet pluto (science), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '538b81e2-4f12-5deb-8847-decaad176f32'
SOURCE_PATH = 'icons-json/science/astronomy planet pluto_538b81e2-4f12-5deb-8847-decaad176f32.json'
AUTHOR = 'json_to_solo'

class AstronomyPlanetPluto(Solo48):
    icon_id = 'astronomy-planet-pluto'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('astronomy', 'planet', 'pluto', 'science')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_line('e1-1', (44, 24), (40, 23))
        self.add_arc('e1-2', (40, 23), (35, 18), radius_x=10)
        self.add_arc('e1-3', (35, 18), (31, 16), radius_x=8, sweep=False)
        self.add_arc('e1-4', (31, 16), (26, 17), radius_x=8, sweep=False)
        self.add_arc('e1-5', (26, 17), (22, 28), radius_x=9, sweep=False)
        self.add_line('e1-6', (22, 28), (28, 34))
        self.add_arc('e1-7', (28, 34), (24, 44), radius_x=12)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.relate('connect', 'c0', 'e0')
        self.relate('connect', 'c0', 'e0')
