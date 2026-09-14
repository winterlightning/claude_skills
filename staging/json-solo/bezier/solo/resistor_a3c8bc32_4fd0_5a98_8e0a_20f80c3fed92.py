"""Resistor (electronics), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3c8bc32-4fd0-5a98-8e0a-20f80c3fed92'
SOURCE_PATH = 'icons-json/electronics/resistor_a3c8bc32-4fd0-5a98-8e0a-20f80c3fed92.json'
AUTHOR = 'json_to_solo'

class ResistorElectronics(Solo48):
    icon_id = 'resistor-electronics'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('resistor', 'electronics')

    def build(self):
        self.add_line('e0', (19, 8), (16, 25))
        self.add_line('e1', (16, 25), (4, 25))
        self.add_line('e2', (24, 40), (19, 8))
        self.add_line('e3', (24, 39), (29, 8))
        self.add_line('e4', (29, 8), (34, 34))
        self.add_line('e5', (34, 34), (36, 25))
        self.add_line('e6', (36, 25), (44, 25))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e4', 'e5', 'e6')
