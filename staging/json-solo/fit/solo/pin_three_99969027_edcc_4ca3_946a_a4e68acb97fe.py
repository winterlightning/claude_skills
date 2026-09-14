"""Pin three (other), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '99969027-edcc-4ca3-946a-a4e68acb97fe'
SOURCE_PATH = 'icons-json/other/pin three_99969027-edcc-4ca3-946a-a4e68acb97fe.json'
AUTHOR = 'json_to_solo'

class PinThreeOther(Solo48):
    icon_id = 'pin-three-other'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('pin', 'three', 'other')

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
