"""shark-fin-in-water: HRECT_XL ink (0,3)-(48,45). Curved dorsal above two wave rows."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f00e048f-3ea9-5641-8ae4-54c29a3a97e8'
SOURCE_PATH = 'pictographic-primitives/animals/shark fin_f00e048f-3ea9-5641-8ae4-54c29a3a97e8.svg'
AUTHOR = 'gpt-6'


class SharkFinInWater(Solo48):
    icon_id = 'shark-fin-in-water'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/marine"
    aliases = ()
    keywords = ('shark', 'fin', 'water', 'waves', 'sea', 'danger', 'ocean', 'surface')

    def build(self) -> None:
        self.add_arc('fin-1', (13, 28), (32, 5), radius_x=50, radius_y=45, sweep=True)
        self.add_arc('fin-2', (32, 5), (35, 28), radius_x=44, radius_y=44, sweep=False)
        self.add_contour('fin', 'fin-1', 'fin-2', closed=False)
        self.add_arc('wave-top-1', (2, 30), (13, 28), radius_x=8, radius_y=6, sweep=False)
        self.add_arc('wave-top-2', (13, 28), (24, 28), radius_x=7, radius_y=6, sweep=False)
        self.add_arc('wave-top-3', (24, 28), (35, 28), radius_x=7, radius_y=6, sweep=False)
        self.add_arc('wave-top-4', (35, 28), (46, 30), radius_x=8, radius_y=6, sweep=False)
        self.add_contour('wave-top', 'wave-top-1', 'wave-top-2', 'wave-top-3', 'wave-top-4', closed=False)
        self.add_arc('wave-low-1', (2, 40), (9, 43), radius_x=7, radius_y=3, sweep=False)
        self.add_arc('wave-low-2', (9, 43), (16, 40), radius_x=7, radius_y=3, sweep=False)
        self.add_arc('wave-low-3', (16, 40), (24, 43), radius_x=8, radius_y=3, sweep=False)
        self.add_arc('wave-low-4', (24, 43), (32, 40), radius_x=8, radius_y=3, sweep=False)
        self.add_arc('wave-low-5', (32, 40), (39, 43), radius_x=7, radius_y=3, sweep=False)
        self.add_arc('wave-low-6', (39, 43), (46, 40), radius_x=7, radius_y=3, sweep=False)
        self.add_contour('wave-low', 'wave-low-1', 'wave-low-2', 'wave-low-3', 'wave-low-4', 'wave-low-5', 'wave-low-6', closed=False)
        self.relate("connect", 'fin', 'wave-top')
