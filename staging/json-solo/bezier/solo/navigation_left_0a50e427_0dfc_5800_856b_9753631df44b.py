"""Navigation left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a50e427-0dfc-5800-856b-9753631df44b'
SOURCE_PATH = 'icons-json/interface-essential/navigation left_0a50e427-0dfc-5800-856b-9753631df44b.json'
AUTHOR = 'json_to_solo'

class NavigationLeft0a50e427(Solo48):
    icon_id = 'navigation-left-0a50e427'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (27, 16), (19, 24))
        self.add_line('e1', (19, 24), (44, 24))
        self.add_line('e2', (44, 24), (44, 8))
        self.add_line('e3', (44, 8), (20, 8))
        self.add_line('e4', (19, 40), (44, 40))
        self.add_line('e5', (27, 32), (19, 24))
        self.add_bezier('e6', (20, 8), ((19.855, 8.008), (20.064, 8.008), (19.918, 8.017)), ((18.3, 8.017), (16.564, 8.48), (15.073, 9.019)), ((9.491, 11.015), (5.4, 15.225), (4.345, 20.766)), ((4.209, 21.499), (4.009, 22.291), (4.009, 23.04)), ((4.009, 23.231), (4, 23.421), (4, 23.612)), ((4, 23.615), (4, 23.618), (4, 23.621)), ((4, 23.882), (4.018, 24.143), (4.018, 24.404)), ((4.018, 30.813), (8.609, 36.396), (14.818, 38.846)), ((15.882, 39.267), (17.855, 40), (19, 40)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e6', 'e4')
        self.add_contour('c1', 'e5')
