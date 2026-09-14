"""Exponential (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0e23fae-9562-52b1-9db1-9c5e4e85aed2'
SOURCE_PATH = 'icons-json/interface-essential/exponential_f0e23fae-9562-52b1-9db1-9c5e4e85aed2.json'
AUTHOR = 'json_to_solo'

class ExponentialF0e23fae(Solo48):
    icon_id = 'exponential-f0e23fae'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('exponential', 'interface-essential')

    def build(self):
        self.add_line('e0', (44, 8), (34, 18))
        self.add_line('e1', (35, 8), (44, 18))
        self.add_line('e2', (4, 25), (9, 21))
        self.add_line('e3', (9, 21), (9, 40))
        self.add_line('e4', (4, 40), (13, 40))
        self.add_line('e5', (30, 33), (30, 27))
        self.add_bezier('e6', (30, 27), ((30, 26.537), (30.145, 26.349), (30.018, 25.903)), ((29.664, 24.682), (29.045, 23.436), (28.036, 22.552)), ((25.882, 20.665), (22.391, 20.295), (20.009, 22.029)), ((16.545, 24.547), (16.336, 32.463), (17.818, 35.992)), ((18.727, 38.164), (20.655, 39.983), (23.318, 39.983)), ((23.464, 39.992), (23.609, 39.992), (23.755, 40)), ((27.191, 40), (30, 36.065), (30, 33)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5', 'e6', closed=True)
        self.relate('connect', 'c2', 'c3')
