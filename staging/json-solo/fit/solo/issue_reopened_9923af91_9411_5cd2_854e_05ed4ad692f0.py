"""Issue reopened (programing), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9923af91-9411-5cd2-854e-05ed4ad692f0'
SOURCE_PATH = 'icons-json/programing/issue reopened_9923af91-9411-5cd2-854e-05ed4ad692f0.json'
AUTHOR = 'json_to_solo'

class IssueReopenedPrograming(Solo48):
    icon_id = 'issue-reopened-programing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('issue', 'reopened', 'programing')

    def build(self):
        self.add_line('e0', (41, 17), (42, 13))
        self.add_line('e1', (36, 16), (41, 17))
        self.add_line('e2', (7, 31), (12, 33))
        self.add_line('e3', (6, 35), (7, 31))
        self.add_line('e4', (41, 29), (42, 25))
        self.add_arc('e5-top', (19, 24), (29, 24), radius_x=5)
        self.add_arc('e5-bottom', (29, 24), (19, 24), radius_x=5)
        self.add_arc('e6-1', (6, 23), (18, 7), radius_x=17)
        self.add_arc('e6-2', (18, 7), (24, 6), radius_x=19)
        self.add_arc('e6-3', (24, 6), (41, 17), radius_x=19)
        self.add_arc('e7-1', (7, 31), (24, 42), radius_x=20, sweep=False)
        self.add_arc('e7-2', (24, 42), (41, 29), radius_x=18, sweep=False)
        self.add_contour('c0', 'e6-1', 'e6-2', 'e6-3', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e7-1', 'e7-2', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
