"""Arched orca with dorsal fin, pectoral fin and notched fluke; preserves source left tail and right snout."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c27c974-982c-51c2-b118-2da9443f5956'
SOURCE_PATH = 'pictographic-primitives/animals/orca whale_2c27c974-982c-51c2-b118-2da9443f5956.svg'
AUTHOR = 'gpt-6'


class LeapingOrca(Solo48):
    icon_id = 'leaping-orca'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('leaping', 'orca')

    def build(self) -> None:
        # Centerline extremes from HRECT_L: (0, 6, 48, 42)
        self.add_arc('back', (10, 26), (25, 15), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_line('dorsal-rise', (25, 15), (25, 8))
        self.add_arc('dorsal-fall', (25, 8), (35, 17), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('head', (35, 17), (46, 34), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('nose', (46, 34), (41, 37), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('chin', (41, 37), (33, 33))
        self.add_arc('pectoral', (33, 33), (23, 37), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_line('fin-front', (23, 37), (26, 30))
        self.add_arc('belly', (26, 30), (13, 31), radius_x=14, radius_y=14, sweep=False, large_arc=False)
        self.add_line('tail-top', (13, 31), (10, 40))
        self.add_line('notch', (10, 40), (7, 32))
        self.add_line('fluke', (7, 32), (2, 30))
        self.add_arc('tail-back', (2, 30), (10, 26), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_contour('outline', 'back', 'dorsal-rise', 'dorsal-fall', 'head', 'nose', 'chin', 'pectoral', 'fin-front', 'belly', 'tail-top', 'notch', 'fluke', 'tail-back', closed=True)
