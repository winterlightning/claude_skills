# Variant of swan-on-water; parent file remains unchanged.
"""A swan above a calm straight waterline, with an open raised wing and a rounded neck return. HRECT_XL preserves the broad silhouette. Lucide bird informs the reduced wing; right-facing asymmetry is intentional."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '42f8bd3b-a505-5e06-aa4e-65cccbc46650'
SOURCE_PATH = 'pictographic-primitives/animals/swan water_42f8bd3b-a505-5e06-aa4e-65cccbc46650.svg'
AUTHOR = 'gpt-6'

class SwanOnWaterVariant3(Solo48):
    icon_id = 'swan-on-water-v3'
    variant_of = 'swan-on-water'
    variant_label = 'Open wing and smooth waterline'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('swan', 'water', 'float', 'pond', 'bird', 'waterfowl', 'waves', 'elegant')

    def build(self) -> None:
        self.add_line('beak', (46, 18), (42, 15))
        self.add_arc('head-right', (42, 15), (32, 5), radius_x=10, sweep=False)
        self.add_arc('head-left', (32, 5), (22, 15), radius_x=10, sweep=False)
        self.add_line('neck', (22, 15), (22, 22))
        self.add_arc('neck-return', (22, 22), (16, 28), radius_x=6, sweep=True)
        self.add_arc('wing-top', (16, 28), (7, 18), radius_x=20, sweep=False)
        self.add_contour('neck-wing', 'head-right', 'head-left', 'neck', 'neck-return', 'wing-top')
        self.relate('connect', 'beak', 'neck-wing')
        self.add_arc('head-inner', (42, 15), (34, 17), radius_x=7, sweep=True)
        self.add_arc('inner-neck', (34, 17), (40, 27), radius_x=15, sweep=False)
        self.add_arc('front', (40, 27), (30, 34), radius_x=10, radius_y=7, sweep=True)
        self.add_contour('front-neck', 'head-inner', 'inner-neck', 'front')
        self.relate('connect', 'neck-wing', 'front-neck')
        self.add_line('hull-base', (30, 34), (20, 34))
        self.add_arc('hull-back', (20, 34), (2, 18), radius_x=18, radius_y=16, sweep=True)
        self.add_line('tail', (2, 18), (7, 18))
        self.add_contour('hull', 'hull-base', 'hull-back', 'tail')
        self.relate('connect', 'hull', 'front-neck')
        self.relate('connect', 'hull', 'neck-wing')
        self.add_line('water', (2, 43), (46, 43))
