"""Fuel Pump with Hose, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a1bed3ea-2aa4-4a23-bb9b-bbe3c5562916'
SOURCE_PATH = 'pictographic-primitives/transportation/gas station_a1bed3ea-2aa4-4a23-bb9b-bbe3c5562916.svg'
AUTHOR = 'gpt-6'

class FuelPumpWithHose(Solo48):
    icon_id = 'fuel-pump-with-hose'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('fuel pump', 'gas station', 'petrol', 'gas pump', 'refuel', 'hose', 'fuel', 'car')

    def build(self) -> None:
        # Current contract centerline extremes: (6,6)-(42,42).
        self.add_polyline('pump',(6,42),(6,24),(6,6),(26,6),(26,24),(26,42),closed=True)
        self.add_line('divider',(6,24),(26,24))
        self.relate('connect','pump','divider')
        self.add_line('display',(15,15),(17,15))
        self.add_line('hose-out',(26,24),(34,24))
        self.add_line('hose-down',(34,24),(34,36))
        self.add_arc('hose-loop',(34,36),(42,36),radius_x=4,sweep=False)
        self.add_polyline('nozzle',(42,36),(42,12),(36,6))
        self.relate('connect','pump','hose-out')
        self.relate('connect','hose-out','hose-down')
        self.relate('connect','hose-down','hose-loop')
        self.relate('connect','hose-loop','nozzle')
