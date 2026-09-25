"""A stack of detached horizontal bands forms a wide-topped funnel narrowing toward the bottom. The band centers shift sideways, giving the descending column a slightly crooked course.

Reduced eight bands to five; shifted centers retain the crooked funnel.
Construction reference: Lucide tornado: decreasing separated horizontal bands.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b97ffbcd-c47a-5205-aa67-a4a9de8ee3b1'
SOURCE_PATH = 'pictographic-primitives/weather/natural disaster hurricane_b97ffbcd-c47a-5205-aa67-a4a9de8ee3b1.svg'
AUTHOR = 'gpt-6'

class TornadoBands(Solo48):
    icon_id = 'tornado-bands'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ()
    keywords = ('tornado', 'hurricane', 'cyclone', 'wind', 'funnel', 'storm')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_line('band-0', (4, 8), (44, 8))
        self.add_line('band-1', (8, 16), (40, 16))
        self.add_line('band-2', (14, 24), (38, 24))
        self.add_line('band-3', (19, 32), (33, 32))
        self.add_line('band-4', (24, 40), (28, 40))
