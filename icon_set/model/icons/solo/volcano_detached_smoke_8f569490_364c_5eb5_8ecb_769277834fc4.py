"""A low volcano has curved flanks and a flat open crater. A large rounded plume floats above it, narrowing into two inward-curving ends that stop just short of the rim.

Simplified smoke to a rounded broad plume with a narrow rising neck; removed secondary flank grooves.
Construction reference: No exact volcano match; Lucide cloud rounded lobes inform smoke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f569490-364c-5eb5-8ecb-769277834fc4'
SOURCE_PATH = 'pictographic-primitives/weather/volcano eruption smoke_8f569490-364c-5eb5-8ecb-769277834fc4.svg'
AUTHOR = 'gpt-6'

class VolcanoDetachedSmoke(Solo48):
    icon_id = 'volcano-detached-smoke'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('volcano', 'smoke', 'mountain', 'eruption', 'plume', 'geology')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_polyline('mountain', (6, 40), (15, 29), (20, 29), (28, 29), (33, 29), (42, 40), closed=False)
        self.add_line('smoke-neck-left', (20, 29), (20, 22))
        self.add_line('smoke-base-left', (20, 22), (15, 22))
        self.add_arc('smoke-left', (15, 22), (10, 17), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('smoke-top', (10, 17), (38, 17), radius_x=14, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('smoke-right', (38, 17), (33, 22), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('smoke-base-right', (33, 22), (28, 22))
        self.add_line('smoke-neck-right', (28, 22), (28, 29))
        self.add_contour('smoke', 'smoke-neck-left', 'smoke-base-left', 'smoke-left', 'smoke-top', 'smoke-right', 'smoke-base-right', 'smoke-neck-right', closed=False)
        self.relate("connect", 'smoke', 'mountain')
