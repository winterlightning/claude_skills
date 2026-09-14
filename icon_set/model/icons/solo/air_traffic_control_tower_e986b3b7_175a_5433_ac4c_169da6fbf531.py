"""A glazed control cab on twin supports with a roof antenna.

Construction: tower-control: tapered cab, roof antenna and paired supports.
Reduction: Consolidated the two stacked cabs into one large observation deck.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e986b3b7-175a-5433-ac4c-169da6fbf531'
SOURCE_PATH = 'pictographic-primitives/travel/airport_e986b3b7-175a-5433-ac4c-169da6fbf531.svg'
AUTHOR = 'gpt-6'


class AirTrafficControlTower(Solo48):
    icon_id = 'air-traffic-control-tower'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/travel"
    aliases = ()
    keywords = ('airport', 'control', 'tower', 'air-traffic', 'aviation', 'building', 'travel')

    def build(self) -> None:
        # VRECT_L centerline extremes (8,6)-(40,42); cab and supports share x=24.
        self.add_polyline('cab',(8,12),(24,12),(40,12),(38,20),(36,28),(32,28),(16,28),(12,28),(10,20),closed=True)
        self.add_line('window-band',(10,20),(38,20))
        self.add_line('antenna',(24,6),(24,12))
        self.relate('connect','cab','window-band')
        self.relate('connect','cab','antenna')
        for i,x in enumerate((16,32)):
         self.add_line(f'support-{i}',(x,28),(x,44))
         self.relate('connect','cab',f'support-{i}')
