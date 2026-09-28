"""Fuel Pump with Display, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cec9fb57-7707-4073-9575-5af2780bbda0'
SOURCE_PATH = 'pictographic-primitives/transportation/gas load_cec9fb57-7707-4073-9575-5af2780bbda0.svg'
AUTHOR = 'gpt-6'

class FuelPumpWithDisplay(Solo48):
    icon_id = 'fuel-pump-with-display'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('fuel pump', 'gas pump', 'petrol', 'gas station', 'refuel', 'nozzle', 'diesel', 'car')

    def build(self):
        # Lucide fuel: upright pump and a separate return hose. Hose walls 10 units apart; loop is a tangent semicircle.
        self.add_polyline('pump', (4, 40), (4, 20), (4, 8), (26, 8), (26, 20), (26, 24), (26, 40), closed=True)
        self.add_line('display', (4, 20), (26, 20))
        self.relate("connect", 'pump', 'display')
        self.add_dot('button', (15, 30))
        self.add_line('hose-start', (26, 24), (34, 24))
        self.add_line('hose-drop', (34, 24), (34, 35))
        self.add_arc('hose-turn', (34, 35), (44, 35), radius_x=5, radius_y=5, sweep=False)
        self.add_line('nozzle-1', (44, 35), (44, 16))
        self.add_line('nozzle-2', (44, 16), (38, 8))
        self.add_contour('hose', 'hose-start', 'hose-drop', 'hose-turn', 'nozzle-1', 'nozzle-2', closed=False)
        self.relate("connect", 'pump', 'hose')
