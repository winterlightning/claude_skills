"""Pin three (other), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '99969027-edcc-4ca3-946a-a4e68acb97fe'
SOURCE_PATH = 'icons-json/other/pin three_99969027-edcc-4ca3-946a-a4e68acb97fe.json'
AUTHOR = 'json_to_solo'

class PinThree(Solo48):
    icon_id = 'pin-three'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('pin', 'three', 'other')

    def build(self):
        self.add_bezier('sym-e0', (24, 44), ((17.971, 38.355), (8, 30.509), (8, 21)))
        self.add_bezier('sym-e1', (8, 21), ((8, 20.782), (8, 20.218), (8, 20)))
        self.add_bezier('sym-e2', (8, 20), ((8, 19.709), (8, 19.291), (8, 19)))
        self.add_bezier('sym-e3', (8, 19), ((8, 17.436), (8.453, 16.427), (9, 15)))
        self.add_bezier('sym-e4', (9, 15), ((11.417, 8.718), (17.676, 4), (24, 4)))
        self.add_bezier('sym-e5', (24, 4), ((24.067, 4), (23.933, 4), (24, 4)))
        self.add_bezier('sym-e6', (24, 4), ((24.021, 4), (23.979, 4), (24, 4)))
        self.add_bezier('sym-e7', (24, 4), ((24.01, 4), (23.99, 4), (24, 4)))
        self.add_bezier('sym-e8', (24, 4), ((24.01, 4), (23.99, 4), (24, 4)))
        self.add_bezier('sym-e9', (24, 4), ((24.021, 4), (23.979, 4), (24, 4)))
        self.add_bezier('sym-e10', (24, 4), ((24.067, 4), (23.933, 4), (24, 4)))
        self.add_bezier('sym-e11', (24, 4), ((30.324, 4), (36.583, 8.718), (39, 15)))
        self.add_bezier('sym-e12', (39, 15), ((39.547, 16.427), (40, 17.436), (40, 19)))
        self.add_bezier('sym-e13', (40, 19), ((40, 19.291), (40, 19.709), (40, 20)))
        self.add_bezier('sym-e14', (40, 20), ((40, 20.218), (40, 20.782), (40, 21)))
        self.add_bezier('sym-e15', (40, 21), ((40, 30.509), (30.029, 38.355), (24, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
