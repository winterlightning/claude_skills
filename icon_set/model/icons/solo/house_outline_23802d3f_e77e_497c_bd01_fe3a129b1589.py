"""House. Retains the identifying silhouette and visible features.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide house: pitched roof and rounded lower corners; source specifies an empty interior and overhanging eaves.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23802d3f-e77e-497c-bd01-fe3a129b1589'
SOURCE_PATH = 'pictographic-primitives/symbol/empty house_23802d3f-e77e-497c-bd01-fe3a129b1589.svg'
AUTHOR = 'gpt-6'


class HouseOutline(Solo48):
    icon_id = 'house-outline'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('house', 'home', 'building', 'residence', 'property', 'real-estate', 'main', 'dwelling')

    def build(self) -> None:
        self.add_polyline('roof', (6, 24), (10, 20), (24, 6), (34, 16), (38, 20), (42, 24))
        self.add_line('right-wall', (38, 20), (38, 38))
        self.add_arc('se', (38, 38), (34, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_line('floor', (34, 42), (14, 42))
        self.add_arc('sw', (14, 42), (10, 38), radius_x=4, radius_y=4, sweep=True)
        self.add_line('left-wall', (10, 38), (10, 20))
        self.add_contour('walls', 'right-wall', 'se', 'floor', 'sw', 'left-wall')
        self.relate("connect", 'roof', 'walls')
