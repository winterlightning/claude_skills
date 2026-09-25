"""Parking lights; independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e56b6a3f-709d-40dc-add6-9d68d751d1cc'
SOURCE_PATH = 'pictographic-primitives/transportation/parking light_e56b6a3f-709d-40dc-add6-9d68d751d1cc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'SOURCE_ICON_ID': 'e56b6a3f-709d-40dc-add6-9d68d751d1cc', 'SOURCE_PATH': 'pictographic-primitives/transportation/parking light_e56b6a3f-709d-40dc-add6-9d68d751d1cc.svg', 'AUTHOR': 'gpt-6'}]

class ParkingLights(Solo48):
    icon_id = 'parking-lights'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('parking', 'lights')

    def build(self) -> None:
        # HRECT_L (6,8)-(42,40). Mirrored lamp assemblies around x=24.
        for name,side in [('left',-1),('right',1)]:
            x=24+side*11
            self.add_line(name+'-flat',(x,16),(x,32))
            self.add_arc(name+'-lens',(x,32),(x,16),radius_x=6,radius_y=8,sweep=side>0)
            self.add_contour(name+'-lamp',name+'-flat',name+'-lens',closed=True)
            self.add_line(name+'-upper-ray',(24+side*20,8),(24+side*19,10))
            self.add_dot(name+'-middle-ray',(24+side*20,24))
            self.add_line(name+'-lower-ray',(24+side*19,38),(24+side*20,40))
