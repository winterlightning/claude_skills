# Variant of swan-on-water; parent file remains unchanged.
"""Swan with an open raised wing above smooth circular ripples. HRECT_XL centerline extremes (2,5)-(46,43). Lucide bird informs the simple wing; waves-horizontal informs repeated tangent-continuous lobes. The facing-right silhouette is deliberately asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '42f8bd3b-a505-5e06-aa4e-65cccbc46650'
SOURCE_PATH = 'pictographic-primitives/animals/swan water_42f8bd3b-a505-5e06-aa4e-65cccbc46650.svg'
AUTHOR = 'gpt-6'

class SwanOnWaterVariant2(Solo48):
    icon_id = 'swan-on-water--v2'
    variant_of = 'swan-on-water'
    variant_label = 'Smooth ripples and open wing'
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
        self.add_arc('neck', (22, 15), (28, 20), radius_x=12, sweep=False)
        self.add_arc('neck-return', (28, 20), (22, 24), radius_x=4, sweep=True)
        self.add_arc('wing-top', (22, 24), (7, 16), radius_x=40, sweep=False)
        self.add_contour('neck-wing', 'head-right', 'head-left', 'neck', 'neck-return', 'wing-top')
        self.relate('connect', 'beak', 'neck-wing')
        self.add_arc('head-inner', (42, 15), (34, 17), radius_x=7, sweep=True)
        self.add_arc('inner-neck', (34, 17), (40, 27), radius_x=15, sweep=False)
        self.add_arc('front', (40, 27), (30, 32), radius_x=10, radius_y=5, sweep=True)
        self.add_contour('front-neck', 'head-inner', 'inner-neck', 'front')
        self.relate('connect', 'neck-wing', 'front-neck')
        self.add_line('hull-base', (30, 32), (20, 32))
        self.add_arc('hull-back', (20, 32), (2, 16), radius_x=18, radius_y=16, sweep=True)
        self.add_line('tail', (2, 16), (7, 16))
        self.add_contour('hull', 'hull-base', 'hull-back', 'tail')
        self.relate('connect', 'hull', 'front-neck')
        self.relate('connect', 'hull', 'neck-wing')
        # Equal circular lobes share tangents at the inflection (22, 41).
        self.add_arc('wave-left', (2, 41), (12, 43), radius_x=26, sweep=False)
        self.add_arc('wave-middle', (12, 43), (22, 41), radius_x=26, sweep=False)
        self.add_arc('wave-right', (22, 41), (32, 39), radius_x=26, sweep=True)
        self.add_arc('wave-end', (32, 39), (42, 41), radius_x=26, sweep=True)
        self.add_contour('water', 'wave-left', 'wave-middle', 'wave-right', 'wave-end')
