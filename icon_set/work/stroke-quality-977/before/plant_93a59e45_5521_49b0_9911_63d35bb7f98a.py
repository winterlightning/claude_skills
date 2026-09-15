"""Plant (nature), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '93a59e45-5521-49b0-9911-63d35bb7f98a'
SOURCE_PATH = 'pictographic-primitives/nature/plant_93a59e45-5521-49b0-9911-63d35bb7f98a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Plant93a59e45(Solo48):
    icon_id = 'plant-93a59e45'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature'
    aliases = ()
    keywords = ('plant', 'nature')

    def build(self):
        self.add_line('e0', (24, 35), (22, 29))
        self.add_line('e1', (22, 29), (20, 26))
        self.add_line('e2', (29, 26), (31, 23))
        self.add_line('e3', (19, 23), (20, 26))
        self.add_line('e4', (24, 42), (24, 36))
        self.add_arc('e5', (29, 26), (24, 35), radius_x=37, sweep=False)
        self.add_arc('e6-1', (31, 23), (42, 20), radius_x=21)
        self.add_arc('e6-2', (42, 20), (24, 36), radius_x=17)
        self.add_arc('e7-1', (29, 26), (24, 6), radius_x=18, sweep=False)
        self.add_arc('e7-2', (24, 6), (19, 23), radius_x=17, sweep=False)
        self.add_line('e8', (19, 25), (20, 26))
        self.add_arc('e9-1', (20, 26), (6, 20), radius_x=19, sweep=False)
        self.add_arc('e9-2', (6, 20), (24, 36), radius_x=17, sweep=False)
        self.add_contour('c0', 'e5', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6-1', 'e6-2')
        self.add_contour('c2', 'e7-1', 'e7-2', 'e3')
        self.add_contour('c3', 'e8')
        self.add_contour('c4', 'e9-1', 'e9-2')
        self.add_contour('c5', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c3', 'c4')
