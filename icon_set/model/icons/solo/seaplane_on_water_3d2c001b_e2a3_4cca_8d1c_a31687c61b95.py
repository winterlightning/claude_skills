"""Seaplane on water; independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d2c001b-e2a3-4cca-8d1c-a31687c61b95'
SOURCE_PATH = 'pictographic-primitives/transportation/plane water_3d2c001b-e2a3-4cca-8d1c-a31687c61b95.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'SOURCE_ICON_ID': '3d2c001b-e2a3-4cca-8d1c-a31687c61b95', 'SOURCE_PATH': 'pictographic-primitives/transportation/plane water_3d2c001b-e2a3-4cca-8d1c-a31687c61b95.svg', 'AUTHOR': 'gpt-6'}, {'SOURCE_ICON_ID': 'dd8260d2-af62-4274-8fad-197640a71a42', 'SOURCE_PATH': 'pictographic-primitives/transportation/plane water_dd8260d2-af62-4274-8fad-197640a71a42.svg', 'AUTHOR': 'gpt-6'}]

class SeaplaneOnWater(Solo48):
    icon_id = 'seaplane-on-water'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('seaplane', 'on', 'water')

    def build(self) -> None:
        # HRECT_L (6,8)-(42,40). One fuselage, cockpit dome, propeller, float and water.
        self.add_polyline('body',(6,12),(10,12),(14,16),(18,16),(34,16),(42,16),(40,24),(32,24),(18,24),(12,24),(6,20),closed=True)
        self.add_arc('cockpit',(18,16),(34,16),radius_x=8,radius_y=8)
        self.relate('connect','body','cockpit')
        self.add_polyline('propeller',(42,12),(42,16),(42,24))
        self.relate('connect','propeller','body')
        self.add_polyline('float',(12,32),(18,32),(32,32),(40,32),(34,40),(16,40),closed=True)
        for name,x in [('left',18),('right',32)]:
            self.add_line(name+'-strut',(x,24),(x,32))
            self.relate('connect',name+'-strut','body')
            self.relate('connect',name+'-strut','float')
        self.add_arc('water-left',(6,40),(16,40),radius_x=6,radius_y=2)
        self.add_arc('water-right',(34,40),(42,40),radius_x=5,radius_y=2)
        self.relate('connect','water-left','float')
        self.relate('connect','water-right','float')
