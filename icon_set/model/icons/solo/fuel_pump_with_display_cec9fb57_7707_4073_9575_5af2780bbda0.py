"""Fuel Pump with Display, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cec9fb57-7707-4073-9575-5af2780bbda0'
SOURCE_PATH = 'pictographic-primitives/transportation/gas load_cec9fb57-7707-4073-9575-5af2780bbda0.svg'
AUTHOR = 'gpt-6'

class FuelPumpWithDisplay(Solo48):
    icon_id = 'fuel-pump-with-display'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('fuel pump', 'gas pump', 'petrol', 'gas station', 'refuel', 'nozzle', 'diesel', 'car')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        self.add_polyline('pump',(6,40),(6,20),(6,8),(28,8),(28,20),(28,24),(28,40),closed=True)
        self.add_line('display-divider',(6,20),(28,20))
        self.relate('connect','pump','display-divider')
        self.add_dot('button',(16,30))
        self.add_line('hose-start-1',(28,24),(36,24))
        self.add_line('hose-start-2',(36,24),(36,34))
        self.add_arc('hose-loop',(36,34),(42,34),radius_x=4,sweep=False)
        self.add_line('hose-end-1',(42,34),(42,14))
        self.add_line('hose-end-2',(42,14),(38,8))
        self.add_contour('hose',*[f'hose-start-{i}' for i in (1,2)],'hose-loop',*[f'hose-end-{i}' for i in (1,2)])
        self.relate('connect','pump','hose')
