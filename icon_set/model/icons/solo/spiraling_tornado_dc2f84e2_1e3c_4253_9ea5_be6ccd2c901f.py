"""A broad elliptical curl forms the upper body of a funnel-shaped storm. Two shorter detached curved strokes descend beneath it, narrowing toward the small rounded bottom.

Opened the spiral turn and retained a smaller curved funnel tail; removed one intermediate band.
Construction reference: Lucide wind and tornado: one coherent curl, decreasing band widths.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc2f84e2-1e3c-4253-9ea5-be6ccd2c901f'
SOURCE_PATH = 'pictographic-primitives/weather/hurricane_dc2f84e2-1e3c-4253-9ea5-be6ccd2c901f.svg'
AUTHOR = 'gpt-6'

class SpiralingTornado(Solo48):
    icon_id = 'spiraling-tornado'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('tornado', 'hurricane', 'cyclone', 'wind', 'storm', 'funnel')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('outer', (24, 8), (4, 18), radius_x=20, radius_y=10, sweep=False, large_arc=False)
        self.add_arc('lower', (4, 18), (44, 18), radius_x=20, radius_y=10, sweep=False, large_arc=False)
        self.add_arc('inner', (44, 18), (26, 18), radius_x=9, radius_y=3, sweep=False, large_arc=False)
        self.add_contour('spiral', 'outer', 'lower', 'inner', closed=False)
        self.add_arc('tail', (18, 37), (34, 37), radius_x=8, radius_y=3, sweep=False, large_arc=False)
