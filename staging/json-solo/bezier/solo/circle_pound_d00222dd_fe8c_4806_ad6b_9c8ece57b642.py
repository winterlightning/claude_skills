"""Circle pound (state), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd00222dd-fe8c-4806-ad6b-9c8ece57b642'
SOURCE_PATH = 'icons-json/state/circle pound_d00222dd-fe8c-4806-ad6b-9c8ece57b642.json'
AUTHOR = 'json_to_solo'

class CirclePoundState(Solo48):
    icon_id = 'circle-pound-state'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('circle', 'pound', 'state')

    def build(self):
        self.add_line('e0', (21, 18), (21, 24))
        self.add_line('e1', (21, 24), (18, 24))
        self.add_line('e2', (21, 24), (27, 24))
        self.add_line('e3', (30, 34), (18, 34))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e5', (30, 18), ((29.627, 16.445), (29.291, 14.809), (27.736, 14.164)), ((25.436, 13.209), (22.555, 13.836), (21.618, 16.364)), ((21.491, 16.718), (21, 17.627), (21, 18)))
        self.add_bezier('e6', (18, 34), ((18.118, 33.927), (17.491, 34.018), (17.636, 34)), ((18.555, 33.909), (19.373, 32.873), (19.909, 32.109)), ((21.236, 30.245), (21, 26.273), (21, 24)))
        self.add_contour('c0', 'e5', 'e0', 'e1')
        self.add_contour('c1', 'e6', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c1')
