"""duck-on-water: reconstructed at native SOLO48 size."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e88202f4-9f66-425e-9f51-77c3ceeb6085'
SOURCE_PATH = 'pictographic-primitives/animals/duck water_e88202f4-9f66-425e-9f51-77c3ceeb6085.svg'
AUTHOR = 'gpt-6'


class DuckOnWater(Solo48):
    icon_id = 'duck-on-water'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('duck', 'water', 'swim', 'pond', 'bird', 'waves', 'waterfowl', 'float')

    def build(self):
        self.add_arc('duck-1', (8, 29), (4, 22), radius_x=14, radius_y=14, sweep=True)
        self.add_arc('duck-2', (4, 22), (23, 26), radius_x=26, radius_y=26, sweep=False)
        self.add_line('duck-3', (23, 26), (21, 17))
        self.add_arc('duck-4', (21, 17), (30, 8), radius_x=9, radius_y=9, sweep=True)
        self.add_arc('duck-5', (30, 8), (39, 17), radius_x=9, radius_y=9, sweep=True)
        self.add_line('duck-6', (39, 17), (46, 20))
        self.add_line('duck-7', (46, 20), (37, 24))
        self.add_arc('duck-8', (37, 24), (40, 29), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('duck', 'duck-1', 'duck-2', 'duck-3', 'duck-4', 'duck-5', 'duck-6', 'duck-7', 'duck-8', closed=False)
        self.add_dot('eye', (30, 17))
        self.add_arc('water-1', (2, 38), (13, 38), radius_x=6, radius_y=2, sweep=False)
        self.add_arc('water-2', (13, 38), (24, 38), radius_x=6, radius_y=2, sweep=True)
        self.add_arc('water-3', (24, 38), (35, 38), radius_x=6, radius_y=2, sweep=False)
        self.add_arc('water-4', (35, 38), (46, 40), radius_x=11, radius_y=2, sweep=False)
        self.add_contour('water', 'water-1', 'water-2', 'water-3', 'water-4', closed=False)
