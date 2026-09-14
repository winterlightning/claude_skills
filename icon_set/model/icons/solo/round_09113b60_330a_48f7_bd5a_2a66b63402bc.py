"""Round (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09113b60-330a-48f7-bd5a-2a66b63402bc'
SOURCE_PATH = 'icons-json/arrows/round_09113b60-330a-48f7-bd5a-2a66b63402bc.json'
AUTHOR = 'json_to_solo'

class Round(Solo48):
    icon_id = 'round'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('round', 'arrows')

    def build(self):
        self.add_line('e0', (13, 33), (10, 31))
        self.add_line('e1', (10, 31), (8, 31))
        self.add_line('e2', (6, 36), (8, 31))
        self.add_bezier('e3', (7, 24), ((7.115, 21.341), (7.366, 18.739), (8.446, 16.293)), ((10.95, 10.598), (17.16, 6.008), (23.517, 6.008)), ((23.646, 6.008), (23.783, 6), (23.912, 6)), ((23.914, 6), (23.916, 6), (23.918, 6)), ((24.147, 6), (24.376, 6.008), (24.605, 6.008)), ((33.761, 6.008), (41.992, 14.305), (41.992, 23.452)), ((41.992, 23.589), (42, 23.718), (42, 23.854)), ((42, 23.857), (42, 23.859), (42, 23.861)), ((42, 24.164), (41.992, 24.466), (41.992, 24.769)), ((41.992, 33.785), (33.9, 41.992), (24.867, 41.992)), ((24.787, 41.992), (24.706, 42), (24.626, 42)), ((24.624, 42), (24.623, 42), (24.622, 42)), ((24.278, 42), (23.926, 41.992), (23.583, 41.992)), ((18.044, 41.992), (12.652, 38.4), (9.584, 33.957)), ((8.839, 32.885), (8.622, 32.137), (8, 31)))
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e0', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
