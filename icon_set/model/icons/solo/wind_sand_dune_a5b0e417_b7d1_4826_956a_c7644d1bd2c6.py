"""Three long horizontal wind strokes with curled left ends sweep above a sand dune. The dune rises to an off-center ridge and descends in a long curved slope to the right.

Reduced three curls to two gusts and omitted the secondary dune groove.
Construction reference: Lucide tornado or wind: separated horizontal bands and coherent curl.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a5b0e417-b7d1-4826-956a-c7644d1bd2c6'
SOURCE_PATH = 'pictographic-primitives/weather/sand storm_a5b0e417-b7d1-4826-956a-c7644d1bd2c6.svg'
AUTHOR = 'gpt-6'

class WindSandDune(Solo48):
    icon_id = 'wind-sand-dune'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('sand', 'dune', 'wind', 'storm', 'desert', 'gust')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_line('gust-run', (4, 18), (38, 18))
        self.add_arc('gust-curl', (38, 18), (38, 8), radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_contour('gust', 'gust-run', 'gust-curl', closed=False)
        self.add_line('lower-wind', (29, 27), (44, 27))
        self.add_arc('dune-left', (4, 40), (15, 34), radius_x=24, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('dune-right', (15, 34), (42, 40), radius_x=38, radius_y=13, sweep=True, large_arc=False)
        self.add_contour('dune', 'dune-left', 'dune-right', closed=False)
