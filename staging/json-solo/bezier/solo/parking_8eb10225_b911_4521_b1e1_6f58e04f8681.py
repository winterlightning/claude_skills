"""Parking (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8eb10225-b911-4521-b1e1-6f58e04f8681'
SOURCE_PATH = 'icons-json/transportation/parking_8eb10225-b911-4521-b1e1-6f58e04f8681.json'
AUTHOR = 'json_to_solo'

class ParkingTransportation(Solo48):
    icon_id = 'parking-transportation'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('parking', 'transportation')

    def build(self):
        self.add_line('e0', (8, 29), (28, 29))
        self.add_line('e1', (26, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 44))
        self.add_bezier('e3', (28, 29), ((29.2, 28.655), (30.52, 27.936), (31.69, 27.445)), ((36.13, 25.555), (40, 21.127), (40, 16.527)), ((40, 16.525), (40, 16.523), (40, 16.521)), ((40, 16.387), (39.99, 16.262), (39.98, 16.127)), ((39.98, 10.727), (35.33, 6.3), (29.94, 4.673)), ((28.84, 4.336), (27.65, 4.009), (26.47, 4.009)), ((26.39, 4.009), (26.32, 4), (26.24, 4)), ((26.16, 4), (26.08, 4), (26, 4)))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e2')
