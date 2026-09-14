"""Navigation direction left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd246a2fd-8a0d-50c5-a0a7-5e7a3544282a'
SOURCE_PATH = 'icons-json/interface-essential/navigation direction left_d246a2fd-8a0d-50c5-a0a7-5e7a3544282a.json'
AUTHOR = 'json_to_solo'

class NavigationDirectionLeftD246a2fd(Solo48):
    icon_id = 'navigation-direction-left-d246a2fd'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'direction', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (17, 4), (8, 15))
        self.add_line('e1', (8, 15), (27, 15))
        self.add_line('e2', (29, 44), (21, 44))
        self.add_line('e3', (17, 26), (8, 15))
        self.add_bezier('e4', (27, 15), ((27.674, 15), (28.859, 15.155), (29.524, 15.3)), ((35.411, 16.627), (39.983, 22.6), (39.983, 29.127)), ((39.983, 29.427), (40, 29.727), (40, 30.027)), ((40, 30.031), (40, 30.034), (40, 30.037)), ((40, 30.252), (39.992, 30.467), (39.992, 30.673)), ((39.992, 31.418), (39.815, 32.182), (39.663, 32.909)), ((38.804, 36.927), (36.438, 40.491), (33.069, 42.482)), ((31.949, 43.145), (31.2, 43.291), (30.072, 43.727)), ((29.903, 43.791), (29.777, 44), (29.592, 44)), ((29.415, 44), (29.177, 44), (29, 44)))
        self.add_contour('c0', 'e0', 'e1', 'e4', 'e2')
        self.add_contour('c1', 'e3')
