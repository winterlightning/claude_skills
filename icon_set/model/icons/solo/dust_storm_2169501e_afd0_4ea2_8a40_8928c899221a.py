"""Several detached horizontal gusts span the image, with open curls turning around their left ends. Short straight fragments interrupt the flow above and to the right.

Reduced detached fragments and one curl; preserved three left-facing dust gusts.
Construction reference: Lucide wind: tangent horizontal runs ending in semicircular curls.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2169501e-afd0-4ea2-8a40-8928c899221a'
SOURCE_PATH = 'pictographic-primitives/weather/dust storm 1_2169501e-afd0-4ea2-8a40-8928c899221a.svg'
AUTHOR = 'gpt-6'

class DustStorm(Solo48):
    icon_id = 'dust-storm'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ()
    keywords = ('dust', 'storm', 'wind', 'gust', 'swirl', 'weather')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('upper-curl', (9, 8), (9, 18), radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_line('upper-run', (9, 18), (44, 18))
        self.add_contour('upper', 'upper-curl', 'upper-run', closed=False)
        self.add_line('middle', (6, 27), (44, 27))
        self.add_arc('lower-curl', (24, 40), (24, 36), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_line('lower-run', (24, 36), (44, 36))
        self.add_contour('lower', 'lower-curl', 'lower-run', closed=False)
