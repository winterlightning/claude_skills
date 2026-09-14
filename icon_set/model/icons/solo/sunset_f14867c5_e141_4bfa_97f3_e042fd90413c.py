"""A low half sun meets a long straight horizon along its flat lower edge. Three short rays extend above the curved crown, with the middle ray standing vertically.

Reduced rays to three and reflection/fog to two lines; central vertical symmetry.
Construction reference: Lucide sun and sunrise: semicircular sun and detached ray marks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f14867c5-e141-4bfa-97f3-e042fd90413c'
SOURCE_PATH = 'pictographic-primitives/weather/day sunset_f14867c5-e141-4bfa-97f3-e042fd90413c.svg'
AUTHOR = 'gpt-6'

class Sunset(Solo48):
    icon_id = 'sunset'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('sunset', 'sun', 'dusk', 'evening', 'horizon', 'weather')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('sun', (12, 40), (36, 40), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_line('horizon', (6, 40), (42, 40))
        self.relate("connect", 'sun', 'horizon')
        self.add_line('ray-top', (24, 8), (24, 15))
        self.add_line('ray-left', (7, 19), (11, 23))
        self.add_line('ray-right', (37, 23), (41, 19))
