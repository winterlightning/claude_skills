"""A round sun emerges above a horizontal horizon with short rays radiating upward and sideways. Two progressively shorter horizontal reflection lines sit directly below the horizon.

Reduced rays to three and reflection/fog to two lines; central vertical symmetry.
Construction reference: Lucide sun and sunrise: semicircular sun and detached ray marks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d62c083-cb40-5ef8-97bf-29562f7c5cec'
SOURCE_PATH = 'pictographic-primitives/weather/day sunrise_1d62c083-cb40-5ef8-97bf-29562f7c5cec.svg'
AUTHOR = 'gpt-6'

class Sunrise(Solo48):
    icon_id = 'sunrise'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ()
    keywords = ('sunrise', 'sun', 'dawn', 'horizon', 'water', 'morning')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('sun', (12, 32), (36, 32), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_line('ray-top', (24, 8), (24, 11))
        self.add_line('horizon', (4, 32), (44, 32))
        self.relate("connect", 'sun', 'horizon')
        self.add_line('reflection', (16, 40), (32, 40))
