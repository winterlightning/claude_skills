"""A broad triangular volcano has curved slopes, a flat base, and a short level crater. A rounded three-lobed smoke plume narrows into a neck immediately above the crater.

Simplified smoke to a rounded broad plume with a narrow rising neck; removed secondary flank grooves.
Construction reference: No exact volcano match; Lucide cloud rounded lobes inform smoke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '983c250e-e7bc-551f-8647-19a0085d73ec'
SOURCE_PATH = 'pictographic-primitives/weather/natural disaster volcano_983c250e-e7bc-551f-8647-19a0085d73ec.svg'
AUTHOR = 'gpt-6'

class SmokingVolcano(Solo48):
    icon_id = 'smoking-volcano'
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
