"""A swan above a calm straight waterline, with an open raised wing and a rounded neck return. HRECT_XL preserves the broad silhouette. Lucide bird informs the reduced wing; right-facing asymmetry is intentional."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '42f8bd3b-a505-5e06-aa4e-65cccbc46650'
SOURCE_PATH = 'pictographic-primitives/animals/swan water_42f8bd3b-a505-5e06-aa4e-65cccbc46650.svg'
AUTHOR = 'gpt-6'

class SwanOnWater(Solo48):
    icon_id = 'swan-on-water'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('swan', 'water', 'float', 'pond', 'bird', 'waterfowl', 'waves', 'elegant')

    def build(self) -> None:
        self.add_line('beak', (42, 18), (42, 15))
        self.add_bezier('head-right', (42, 15), *(((41.48458019, 9.87098707), (37.15478068, 6), (32, 6)),))
        self.add_bezier('head-left', (32, 6), *(((26.84521932, 6), (22.51541981, 9.87098707), (22, 15)),))
        self.add_line('neck', (22, 15), (22, 18))
        self.add_arc('neck-return', (22, 18), (16, 24), radius_x=6, sweep=True)
        self.add_bezier('wing-top',(16,24),((16,23),(16,22),(16,21)))
        self.add_contour('neck-wing', 'head-right', 'head-left', 'neck', 'neck-return', 'wing-top')
        self.relate('connect', 'beak', 'neck-wing')
        self.add_arc('head-inner', (42, 15), (34, 17), radius_x=7, sweep=True)
        self.add_arc('inner-neck', (34, 17), (40, 27), radius_x=15, sweep=False)
        self.add_arc('front', (40, 27), (30, 33), radius_x=10, radius_y=7, sweep=True)
        self.add_contour('front-neck', 'head-inner', 'inner-neck', 'front')
        self.relate('connect', 'neck-wing', 'front-neck')
        self.add_line('hull-base', (30, 33), (20, 33))
        self.add_bezier('hull-back',(20,33),((10,33),(6,26),(6,14)))
        self.add_contour('hull', 'hull-base', 'hull-back')
        self.relate('connect', 'hull', 'front-neck')
        self.add_line('water', (6, 42), (42, 42))
