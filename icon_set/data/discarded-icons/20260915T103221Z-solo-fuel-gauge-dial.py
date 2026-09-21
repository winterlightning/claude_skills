"""Fuel Gauge Dial, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '18728730-c932-5c2a-bbae-5f3d79009993'
SOURCE_PATH = 'pictographic-primitives/transportation/gas f_18728730-c932-5c2a-bbae-5f3d79009993.svg'
AUTHOR = 'gpt-6'

class FuelGaugeDial(Solo48):
    icon_id = 'fuel-gauge-dial'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('fuel gauge', 'gauge', 'fuel', 'full', 'dashboard', 'car', 'meter', 'petrol')

    def build(self) -> None:
        # Current contract centerline extremes: (6,6)-(42,42).
        self.add_arc('gauge',(6,24),(42,24),radius_x=18)
        self.add_line('needle',(24,24),(30,18))
        self.add_polyline('full-label',(18,42),(18,40),(18,32),(26,32))
        self.add_line('full-crossbar',(18,40),(24,40))
        self.relate('connect','full-label','full-crossbar')
