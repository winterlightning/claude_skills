"""Dynamic (diagrams), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea1bde8b-e7f7-4fc3-b915-1043468acb6d'
SOURCE_PATH = 'pictographic-primitives/diagrams/dynamic_ea1bde8b-e7f7-4fc3-b915-1043468acb6d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Dynamic(Solo48):
    icon_id = 'dynamic'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('dynamic', 'diagrams')

    def build(self):
        self.add_line('e0', (11, 32), (11, 26))
        self.add_line('e1', (13, 24), (35, 24))
        self.add_arc('e2-top', (6, 37), (16, 37), radius_x=5)
        self.add_arc('e2-bottom', (16, 37), (6, 37), radius_x=5)
        self.add_arc('e3-top', (32, 11), (42, 11), radius_x=5)
        self.add_arc('e3-bottom', (42, 11), (32, 11), radius_x=5)
        self.add_arc('e4', (11, 26), (13, 24), radius_x=2)
        self.add_arc('e5', (35, 24), (37, 16), radius_x=7, sweep=False)
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.relate('connect', 'c0', 'e2')
        self.relate('connect', 'c0', 'e3')
