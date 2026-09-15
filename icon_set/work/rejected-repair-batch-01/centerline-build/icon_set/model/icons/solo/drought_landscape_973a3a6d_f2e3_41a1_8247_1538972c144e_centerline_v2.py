"""Attach the dry tree trunk exactly to the ground corner and angle the ground crack toward its own side of the parched slab.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '973a3a6d-f2e3-41a1-8247-1538972c144e'
SOURCE_PATH = 'pictographic-primitives/weather/draught_973a3a6d-f2e3-41a1-8247-1538972c144e.svg'
AUTHOR = 'gpt-6'

class DroughtLandscape(Solo48):
    icon_id = 'drought-landscape-centerline-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('drought', 'sun', 'tree', 'dry', 'ground', 'climate')

    def build(self) -> None:
        self.add_arc('sun-top', (4, 15), (18, 15), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('sun-bottom', (18, 15), (4, 15), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_contour('sun', 'sun-top', 'sun-bottom', closed=True)
        self.add_polyline('ground', (4, 40), (15, 31), (33, 31), (44, 40), closed=True)
        self.add_line('ground-crack', (25, 31), (18, 40))
        self.relate('connect', 'ground', 'ground-crack')
        self.add_line('tree', (33, 8), (33, 31))
        self.add_polyline('branches', (27, 17), (33, 23), (44, 15), closed=False)
        self.relate('connect', 'tree', 'branches')
        self.relate('connect', 'tree', 'ground')
    variant_of = 'drought-landscape'
    variant_label = 'Batch 01 centerline repair'
