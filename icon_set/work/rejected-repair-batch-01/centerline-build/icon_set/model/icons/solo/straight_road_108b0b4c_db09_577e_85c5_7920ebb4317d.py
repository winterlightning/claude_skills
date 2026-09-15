from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '108b0b4c-db09-577e-85c5-7920ebb4317d'
SOURCE_PATH = 'pictographic-primitives/transportation/road straight_108b0b4c-db09-577e-85c5-7920ebb4317d.svg'
AUTHOR = 'gpt-6'

class StraightRoad(Solo48):
    icon_id = 'straight-road'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('road', 'straight', 'highway', 'lane', 'street', 'perspective', 'driving', 'route')

    def build(self):
        self.add_line('left-edge',(14,4),(8,44))
        self.add_line('right-edge',(34,4),(40,44))
        for n,(a,b) in enumerate(((4,10),(20,26),(36,44))):
            self.add_line(f'centre-dash-{n}',(24,a),(24,b))
