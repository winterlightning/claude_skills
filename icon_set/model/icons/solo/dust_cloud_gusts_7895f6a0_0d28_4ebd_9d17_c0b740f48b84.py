"""A large rounded cloud occupies the upper-left portion of the image. Three horizontal gusts extend across its open lower edge, with the upper and lower gusts curling at the left.

Retained the cloud and one large curled gust; removed crowded secondary gusts.
Construction reference: Lucide cloud-fog and wind: open cloud above separated gusts.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7895f6a0-0d28-4ebd-9d17-c0b740f48b84'
SOURCE_PATH = 'pictographic-primitives/weather/dust storm_7895f6a0-0d28-4ebd-9d17-c0b740f48b84.svg'
AUTHOR = 'gpt-6'

class DustCloudGusts(Solo48):
    icon_id = 'dust-cloud-gusts'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('dust', 'cloud', 'wind', 'gust', 'storm', 'weather')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('cloud-dome', (18, 20), (32, 14), radius_x=14, radius_y=6, sweep=True, large_arc=True)
        self.add_line('cloud-shoulder', (32, 14), (36, 14))
        self.add_arc('cloud-right', (36, 14), (36, 20), radius_x=8, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('cloud', 'cloud-dome', 'cloud-shoulder', 'cloud-right', closed=False)
        self.add_arc('gust-curl', (13, 30), (13, 40), radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_line('gust-run', (13, 40), (42, 40))
        self.add_contour('gust', 'gust-curl', 'gust-run', closed=False)
