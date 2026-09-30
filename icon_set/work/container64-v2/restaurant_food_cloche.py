"""v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (restaurant-food-cloche SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'restaurant-food-cloche'
SOURCE_PATH = 'icon_set/dist/failed/container64/restaurant-food-cloche.svg'
AUTHOR = 'claude-opus-5-5'


class RestaurantFoodCloche(Container64):
    icon_id = 'restaurant-food-cloche'
    keyshape = Keyshape.SQUARE
    aliases = ('serving-cloche', 'food-cover')
    keywords = ('restaurant', 'food', 'cloche')

    def build(self) -> None:
        self.add_arc('handle', (24, 14), (40, 14), radius_x=8)
        self.add_line('cover-0', (10, 50), (12, 24))
        self.add_arc('cover-1', (12, 24), (20, 16), radius_x=8)
        self.add_line('cover-2', (20, 16), (44, 16))
        self.add_arc('cover-3', (44, 16), (52, 24), radius_x=8)
        self.add_line('cover-4', (52, 24), (54, 50))
        self.add_line('tray-0', (6, 50), (58, 50))
        self.add_line('tray-1', (58, 50), (58, 52))
        self.add_arc('tray-2', (58, 52), (52, 58), radius_x=6)
        self.add_line('tray-3', (52, 58), (12, 58))
        self.add_arc('tray-4', (12, 58), (6, 52), radius_x=6)
        self.add_line('tray-5', (6, 52), (6, 50))
        self.add_contour('cover', 'cover-0', 'cover-1', 'cover-2', 'cover-3', 'cover-4')
        self.add_contour('tray', 'tray-0', 'tray-1', 'tray-2', 'tray-3', 'tray-4', 'tray-5', closed=True)
        self.relate('connect', 'handle', 'cover')
        self.relate('connect', 'tray', 'cover')
