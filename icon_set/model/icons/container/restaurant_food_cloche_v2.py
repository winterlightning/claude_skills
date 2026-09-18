from ._construction import path, rounded_rect as rect, ellipse
'A tapered food cover with an arched handle and a shallow serving tray.\n\nVRECT_XL preserves the tall cover: ink (4,0)-(60,64), centerline (6,2)-(58,62).\nReference: supplied failed SVG; Lucide concierge-bell original and atomic-debug\ninformed the handle, cover and tray hierarchy. The tray rim now supplies the\nshared edge once; the duplicate cover bottom was removed. The subject remains\nsymmetric about x=32, with all identifying parts retained.\n\nHosting (compose.py): heart, check valid; plus blocked.\n'
from ...keyshapes import Keyshape
from ._base import Container64
SOURCE_ICON_ID = 'restaurant-food-cloche'
SOURCE_PATH = 'icon_set/dist/failed/container64/restaurant-food-cloche.svg'
AUTHOR = 'gpt-6'

class RestaurantFoodClocheVariant2(Container64):
    icon_id = 'restaurant-food-cloche-v2'
    variant_of = 'restaurant-food-cloche'
    variant_label = 'Room for native 32-unit sub-icons'
    keyshape = Keyshape.SQUARE
    aliases = ('serving-cloche', 'food-cover')
    keywords = ('restaurant', 'food', 'cloche')

    def build(self):
        line, poly = (self.add_line, self.add_polyline)

        def join(a, b):
            self.relate('connect', a, b)
        axis = 32
        self.add_arc('handle', (22, 12), (42, 12), radius_x=10)
        path(self, 'cover', (6, 54), [('L', (8, 20)), ('A', (16, 12), 8, 8, True), ('L', (48, 12)), ('A', (56, 20), 8, 8, True), ('L', (58, 54))])
        join('handle', 'cover')
        path(self, 'tray', (2, 54), [('L', (62, 54)), ('L', (62, 56)), ('A', (56, 62), 6, 6, True), ('L', (8, 62)), ('A', (2, 56), 6, 6, True), ('L', (2, 54))], True)
        join('tray', 'cover')
