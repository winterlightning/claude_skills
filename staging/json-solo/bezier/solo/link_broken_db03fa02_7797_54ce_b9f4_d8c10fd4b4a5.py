"""Link broken (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db03fa02-7797-54ce-b9f4-d8c10fd4b4a5'
SOURCE_PATH = 'icons-json/interface-essential/link broken_db03fa02-7797-54ce-b9f4-d8c10fd4b4a5.json'
AUTHOR = 'json_to_solo'

class LinkBrokenInterfaceEssential(Solo48):
    icon_id = 'link-broken-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('link', 'broken', 'interface-essential')

    def build(self):
        self.add_line('e0', (20, 4), (20, 9))
        self.add_line('e1', (22, 17), (28, 9))
        self.add_line('e2', (38, 20), (29, 31))
        self.add_line('e3', (11, 9), (15, 11))
        self.add_line('e4', (8, 18), (12, 18))
        self.add_line('e5', (16, 23), (10, 31))
        self.add_line('e6', (21, 41), (26, 36))
        self.add_bezier('e7', (28, 9), ((28.674, 8.173), (29.861, 8.109), (30.813, 7.791)), ((35.225, 6.291), (39.992, 9.818), (39.992, 14.918)), ((39.992, 14.99), (40, 15.061), (40, 15.142)), ((40, 15.143), (40, 15.144), (40, 15.145)), ((40, 15.209), (39.992, 15.273), (39.992, 15.336)), ((39.992, 16.764), (38.901, 18.936), (38, 20)))
        self.add_bezier('e8', (10, 31), ((9.234, 31.936), (8.008, 34.655), (8.008, 35.909)), ((8.008, 35.973), (8, 36.045), (8, 36.109)), ((8, 36.245), (8.008, 36.382), (8.008, 36.518)), ((8.008, 37.245), (8.278, 38.027), (8.522, 38.7)), ((9.575, 41.573), (11.865, 43.991), (14.905, 43.991)), ((15.021, 44), (15.146, 44), (15.27, 44)), ((15.272, 44), (15.274, 44), (15.276, 44)), ((15.402, 44), (15.528, 43.991), (15.655, 43.991)), ((17.676, 43.991), (19.644, 42.464), (21, 41)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5', 'e8', 'e6')
