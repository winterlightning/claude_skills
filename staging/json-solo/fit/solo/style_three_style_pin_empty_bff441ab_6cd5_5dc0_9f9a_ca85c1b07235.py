"""Style three style pin empty (maps), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bff441ab-6cd5-5dc0-9f9a-ca85c1b07235'
SOURCE_PATH = 'icons-json/maps/style three style pin empty_bff441ab-6cd5-5dc0-9f9a-ca85c1b07235.json'
AUTHOR = 'json_to_solo'

class StyleThreeStylePinEmptyMaps(Solo48):
    icon_id = 'style-three-style-pin-empty-maps'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('style', 'three', 'pin', 'empty', 'maps')

    def build(self):
        self.add_arc('sym-e0', (24, 44), (8, 21), radius_x=37)
        self.add_line('sym-e1', (8, 21), (8, 20))
        self.add_line('sym-e2', (8, 20), (8, 19))
        self.add_arc('sym-e3', (8, 19), (9, 15), radius_x=14)
        self.add_arc('sym-e4', (9, 15), (24, 4), radius_x=17)
        self.add_arc('sym-e11', (24, 4), (39, 15), radius_x=17)
        self.add_arc('sym-e12', (39, 15), (40, 19), radius_x=15, sweep=False)
        self.add_line('sym-e13', (40, 19), (40, 20))
        self.add_arc('sym-e14', (40, 20), (40, 21), radius_x=25, sweep=False)
        self.add_arc('sym-e15', (40, 21), (24, 44), radius_x=37)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
