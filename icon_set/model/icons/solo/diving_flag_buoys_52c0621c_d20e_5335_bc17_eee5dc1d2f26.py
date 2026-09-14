'Diving flag buoy: clean flag diagonal, circular buoy and exact staff endpoints; remove the converted stray arc.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '52c0621c-d20e-5335-bc17-eee5dc1d2f26'
SOURCE_PATH = 'icons-json/outdoors/diving flag buoys_52c0621c-d20e-5335-bc17-eee5dc1d2f26.json'
AUTHOR = 'gpt-6'

class DivingFlagBuoys(Solo48):
    icon_id = 'diving-flag-buoys'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('diving', 'flag', 'buoys', 'outdoors')

    def build(self) -> None:
        # Flag, vertical staff and buoy share exact structural attachment points.
        self.add_polyline('flag',(13,4),(40,4),(40,21),(13,21),closed=True)
        self.add_line('stripe',(13,4),(40,21));self.relate('connect','stripe','flag')
        self.add_polyline('staff',(13,4),(13,21),(13,30))
        self.relate('connect','staff','flag');self.relate('connect','staff','stripe')
        self.add_arc('buoy-a',(9,34),(17,34),radius_x=4)
        self.add_arc('buoy-b',(17,34),(9,34),radius_x=4)
        self.add_contour('buoy','buoy-a','buoy-b',closed=True)
        self.add_line('lower-staff',(13,38),(13,44))
        self.add_polyline('base',(8,44),(13,44),(20,44))
        self.relate('connect','staff','buoy');self.relate('connect','lower-staff','buoy');self.relate('connect','lower-staff','base')
