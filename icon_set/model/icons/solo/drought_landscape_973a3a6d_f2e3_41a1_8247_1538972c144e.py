"""A large round sun hangs above a bare branching tree at the right of a flat horizon. Angular divisions cut the exposed ground below into dry polygonal patches.

Reduced dry ground to two angular patches and retained one bare tree beneath a sun.
Construction reference: Lucide sun circle; no useful landscape match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '973a3a6d-f2e3-41a1-8247-1538972c144e'
SOURCE_PATH = 'pictographic-primitives/weather/draught_973a3a6d-f2e3-41a1-8247-1538972c144e.svg'
AUTHOR = 'gpt-6'

class DroughtLandscape(Solo48):
    icon_id = 'drought-landscape'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('drought', 'sun', 'tree', 'dry', 'ground', 'climate')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('sun-top', (6, 15), (18, 15), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('sun-bottom', (18, 15), (6, 15), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_contour('sun', 'sun-top', 'sun-bottom', closed=True)
        self.add_polyline('ground', (6, 40), (15, 31), (33, 31), (42, 40), closed=True)
        self.add_line('ground-crack', (27, 31), (21, 40))
        self.relate("connect", 'ground', 'ground-crack')
        self.add_line('tree', (35, 8), (35, 31))
        self.add_polyline('branches', (29, 17), (35, 23), (42, 15), closed=False)
        self.relate("connect", 'tree', 'branches')
        self.relate("connect", 'tree', 'ground')
