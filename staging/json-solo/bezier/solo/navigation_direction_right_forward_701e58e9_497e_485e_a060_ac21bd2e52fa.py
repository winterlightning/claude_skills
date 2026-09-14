"""Navigation direction right forward (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '701e58e9-497e-485e-a060-ac21bd2e52fa'
SOURCE_PATH = 'icons-json/interface-essential/navigation direction right forward_701e58e9-497e-485e-a060-ac21bd2e52fa.json'
AUTHOR = 'json_to_solo'

class NavigationDirectionRightForwardInterfaceEssential(Solo48):
    icon_id = 'navigation-direction-right-forward-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'direction', 'right', 'forward', 'interface-essential')

    def build(self):
        self.add_line('e0', (28, 8), (28, 17))
        self.add_line('e1', (28, 17), (20, 17))
        self.add_line('e2', (17, 31), (28, 31))
        self.add_line('e3', (28, 31), (28, 40))
        self.add_line('e4', (28, 40), (43, 25))
        self.add_line('e5', (44, 24), (28, 8))
        self.add_bezier('e6', (4, 40), ((4, 39.722), (4, 39.278), (4, 39)))
        self.add_bezier('e7', (20, 17), ((19.245, 17), (18.745, 17.465), (17.982, 17.541)), ((9.491, 18.392), (4.018, 24.968), (4.018, 32.707)), ((4.018, 32.952), (4, 33.204), (4, 33.457)), ((4, 33.811), (4.018, 34.156), (4.018, 34.509)), ((4.018, 34.964), (4.018, 35.419), (4.018, 35.874)), ((4.018, 35.899), (4.009, 35.924), (4.009, 35.949)), ((4.009, 37.019), (4, 38.088), (4, 39.158)), ((4.664, 38.223), (5.318, 37.297), (5.982, 36.362)), ((6, 36.337), (6.027, 36.303), (6.045, 36.278)), ((8.027, 33.491), (11.255, 31.638), (14.782, 31.015)), ((15.4, 30.905), (16.373, 31), (17, 31)))
        self.add_bezier('e8', (43, 25), ((43.291, 24.714), (43.7, 24.278), (44, 24)))
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e0', 'e1', 'e7', 'e2', 'e3', 'e4', 'e8', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
