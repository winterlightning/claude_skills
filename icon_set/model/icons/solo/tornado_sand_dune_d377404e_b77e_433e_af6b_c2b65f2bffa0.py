"""Five horizontal bands shorten downward into a compact storm funnel above a sand dune. The dune has a pointed ridge toward the left and a long curved right slope.

Kept an off-center dune ridge and reduced overhead weather bands to fit; removed secondary dune groove.
Construction reference: Lucide tornado or wind: separated horizontal bands and coherent curl.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd377404e-b77e-433e-af6b-c2b65f2bffa0'
SOURCE_PATH = 'pictographic-primitives/weather/sand storm_d377404e-b77e-433e-af6b-c2b65f2bffa0.svg'
AUTHOR = 'gpt-6'

class TornadoSandDune(Solo48):
    icon_id = 'tornado-sand-dune'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    categories = ("weather", "primitives")
    aliases = ()
    keywords = ('sand', 'dune', 'tornado', 'storm', 'desert', 'wind')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_line('funnel-0', (4, 8), (44, 8))
        self.add_line('funnel-1', (12, 16), (38, 16))
        self.add_line('funnel-2', (20, 24), (32, 24))
        self.add_arc('dune-left', (4, 40), (15, 34), radius_x=24, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('dune-right', (15, 34), (44, 40), radius_x=38, radius_y=13, sweep=True, large_arc=False)
        self.add_contour('dune', 'dune-left', 'dune-right', closed=False)
