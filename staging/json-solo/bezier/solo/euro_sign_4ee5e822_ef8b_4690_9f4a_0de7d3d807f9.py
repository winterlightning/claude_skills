"""Euro sign (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ee5e822-ef8b-4690-9f4a-0de7d3d807f9'
SOURCE_PATH = 'icons-json/symbol/euro sign_4ee5e822-ef8b-4690-9f4a-0de7d3d807f9.json'
AUTHOR = 'json_to_solo'

class EuroSignSymbol(Solo48):
    icon_id = 'euro-sign-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('euro', 'sign', 'symbol')

    def build(self):
        self.add_line('e0', (14, 32), (12, 25))
        self.add_line('e1', (8, 25), (18, 25))
        self.add_bezier('e2', (40, 8), ((36.968, 5.909), (33.701, 4.018), (30.004, 4.018)), ((29.869, 4.009), (29.735, 4.009), (29.6, 4)), ((29.599, 4), (29.598, 4), (29.597, 4)), ((29.531, 4), (29.464, 4.009), (29.398, 4.009)), ((20.943, 4.009), (13.592, 12.336), (12.867, 21.2)), ((12.766, 22.445), (12.865, 23.773), (13, 25)))
        self.add_bezier('e3', (40, 40), ((37.213, 42.127), (33.819, 43.991), (30.341, 43.991)), ((30.076, 43.991), (29.811, 44), (29.537, 44)), ((29.533, 44), (29.529, 44), (29.524, 44)), ((29.255, 44), (28.985, 43.982), (28.707, 43.982)), ((23.166, 43.982), (17.305, 39.355), (14.779, 34.2)), ((14.476, 33.582), (14.16, 32.682), (14, 32)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3', 'e0')
        self.add_contour('c2', 'e1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
