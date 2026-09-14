"""Bird life (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dee6f213-07ab-4305-8dd4-d656ac7937ec'
SOURCE_PATH = 'icons-json/transportation/bird life_dee6f213-07ab-4305-8dd4-d656ac7937ec.json'
AUTHOR = 'json_to_solo'

class BirdLifeTransportation(Solo48):
    icon_id = 'bird-life-transportation'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('bird', 'life', 'transportation')

    def build(self):
        self.add_line('e0', (4, 8), (16, 8))
        self.add_line('e1', (32, 8), (44, 8))
        self.add_line('e2-1', (16, 8), (19, 31))
        self.add_arc('e2-2', (19, 31), (24, 40), radius_x=9, sweep=False)
        self.add_arc('e2-3', (24, 40), (28, 35), radius_x=5, sweep=False)
        self.add_line('e2-4', (28, 35), (31, 20))
        self.add_line('e2-5', (31, 20), (32, 8))
        self.add_contour('c0', 'e0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e1')
