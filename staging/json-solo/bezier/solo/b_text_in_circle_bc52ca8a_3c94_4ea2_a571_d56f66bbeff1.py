"""B text in circle (state), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc52ca8a-3c94-4ea2-a571-d56f66bbeff1'
SOURCE_PATH = 'icons-json/state/b text in circle_bc52ca8a-3c94-4ea2-a571-d56f66bbeff1.json'
AUTHOR = 'json_to_solo'

class BTextInCircleState(Solo48):
    icon_id = 'b-text-in-circle-state'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('b', 'text', 'in', 'circle', 'state')

    def build(self):
        self.add_line('e0', (24, 14), (18, 14))
        self.add_line('e1', (18, 14), (18, 34))
        self.add_line('e2', (18, 34), (22, 34))
        self.add_line('e3', (25, 24), (18, 24))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e5', (22, 34), ((23.155, 34), (24.591, 34.091), (25.736, 33.845)), ((28.282, 33.282), (30.055, 31.3), (30.009, 28.645)), ((29.982, 26.873), (28.891, 25.455), (27.318, 24.727)), ((26.836, 24.5), (26.309, 24.373), (25.791, 24.236)), ((25.673, 24.209), (25.373, 24.136), (25.255, 24.109)), ((25.136, 24.073), (25.027, 24.036), (24.909, 24)), ((26.4, 23.418), (27.691, 23.064), (28.536, 21.545)), ((30.518, 17.964), (28.036, 14), (24, 14)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e5', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
