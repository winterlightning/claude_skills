"""shark-fin-in-water: HRECT_XL ink (6,6)-(42,42). Curved dorsal above two wave rows."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f00e048f-3ea9-5641-8ae4-54c29a3a97e8'
SOURCE_PATH = 'pictographic-primitives/animals/shark fin_f00e048f-3ea9-5641-8ae4-54c29a3a97e8.svg'
AUTHOR = 'gpt-6'


class SharkFinInWater(Solo48):
    icon_id = 'shark-fin-in-water'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('shark', 'fin', 'water', 'waves', 'sea', 'danger', 'ocean', 'surface')

    def build(self) -> None:
        self.add_arc('fin-1', (13, 28), (32, 6), radius_x=50, radius_y=45, sweep=True)
        self.add_arc('fin-2', (32, 6), (35, 28), radius_x=44, radius_y=44, sweep=False)
        self.add_contour('fin', 'fin-1', 'fin-2', closed=False)
        self.add_arc('wave-top-1', (6, 30), (13, 28), radius_x=8, radius_y=6, sweep=False)
        self.add_arc('wave-top-2', (13, 28), (24, 28), radius_x=7, radius_y=6, sweep=False)
        self.add_arc('wave-top-3', (24, 28), (35, 28), radius_x=7, radius_y=6, sweep=False)
        self.add_arc('wave-top-4', (35, 28), (42, 30), radius_x=8, radius_y=6, sweep=False)
        self.add_contour('wave-top', 'wave-top-1', 'wave-top-2', 'wave-top-3', 'wave-top-4', closed=False)
        self.add_arc('wave-low-1', (6, 40), (9, 42), radius_x=7, radius_y=3, sweep=False)
        self.add_bezier('wave-low-2', (9, 42), *(((12.11211023, 42), (14.96596418, 41.26025907), (16, 40)),))
        self.add_bezier('wave-low-3', (16, 40), *(((17.18175522, 41.26025907), (20.44330259, 42), (24, 42)),))
        self.add_bezier('wave-low-4', (24, 42), *(((27.55669741, 42), (30.81824478, 41.26025907), (32, 40)),))
        self.add_bezier('wave-low-5', (32, 40), *(((33.03403582, 41.26025907), (35.88788977, 42), (39, 42)),))
        self.add_arc('wave-low-6', (39, 42), (42, 40), radius_x=7, radius_y=3, sweep=False)
        self.add_contour('wave-low', 'wave-low-1', 'wave-low-2', 'wave-low-3', 'wave-low-4', 'wave-low-5', 'wave-low-6', closed=False)
        self.relate("connect", 'fin', 'wave-top')
