"""Amazon web service game tech (_uncategorized_02), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7558136-8e09-4d56-8e82-dd4c66e81553'
SOURCE_PATH = 'icons-json/_uncategorized_02/amazon web service game tech_a7558136-8e09-4d56-8e82-dd4c66e81553.json'
AUTHOR = 'json_to_solo'

class AmazonWebServiceGameTechUncategorized02(Solo48):
    icon_id = 'amazon-web-service-game-tech-uncategorized-02'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_02'
    aliases = ()
    keywords = ('amazon', 'web', 'service', 'game', 'tech', '_uncategorized_02')

    def build(self):
        self.add_line('e0', (5, 17), (4, 34))
        self.add_line('e1', (12, 38), (17, 31))
        self.add_line('e2', (18, 30), (30, 30))
        self.add_line('e3', (31, 31), (36, 38))
        self.add_line('e4', (44, 34), (43, 17))
        self.add_line('e5', (29, 12), (19, 12))
        self.add_arc('e6-1', (4, 34), (6, 39), radius_x=8, sweep=False)
        self.add_line('e6-2', (6, 39), (9, 40))
        self.add_arc('e6-3', (9, 40), (12, 38), radius_x=5)
        self.add_line('e7', (17, 31), (18, 30))
        self.add_line('e8', (30, 30), (31, 31))
        self.add_line('e9-1', (36, 38), (39, 40))
        self.add_line('e9-2', (39, 40), (42, 39))
        self.add_arc('e9-3', (42, 39), (44, 34), radius_x=8, sweep=False)
        self.add_arc('e10-1', (43, 17), (35, 8), radius_x=9, sweep=False)
        self.add_arc('e10-2', (35, 8), (29, 12), radius_x=10, sweep=False)
        self.add_arc('e11-1', (19, 12), (12, 8), radius_x=9, sweep=False)
        self.add_arc('e11-2', (12, 8), (5, 17), radius_x=8, sweep=False)
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e6-3', 'e1', 'e7', 'e2', 'e8', 'e3', 'e9-1', 'e9-2', 'e9-3', 'e4', 'e10-1', 'e10-2', 'e5', 'e11-1', 'e11-2', closed=True)
