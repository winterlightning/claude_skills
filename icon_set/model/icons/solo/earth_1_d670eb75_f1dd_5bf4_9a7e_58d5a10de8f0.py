'Earth: preserve curved continent edges with a circular globe and distinct open ocean space.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd670eb75-f1dd-5bf4-9a7e-58d5a10de8f0'
SOURCE_PATH = 'icons-json/maps/earth 1_d670eb75-f1dd-5bf4-9a7e-58d5a10de8f0.json'
AUTHOR = 'gpt-6'

class Earth1Maps(Solo48):
    icon_id = 'earth-1-maps'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('earth', 'maps')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)

        self.add_bezier('north-west',(24,4),((21,8),(23,13),(18,16)),((15,18),(8,18),(4,24)))
        self.add_bezier('south-west',(4,24),((10,24),(15,25),(19,29)),((22,33),(16,35),(16,40)))
        self.add_bezier('east',(44,24),((38,22),(32,26),(32,20)),((32,13),(35,10),(36,8)))
        for name in ('north-west','south-west','east'):self.relate('connect',name,'rim')
        self.relate('connect','north-west','south-west')
