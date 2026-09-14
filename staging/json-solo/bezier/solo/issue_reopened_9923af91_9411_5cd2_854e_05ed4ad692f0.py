"""Issue reopened (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e6', (6, 23), ((6, 22.935), (6.008, 23.043), (6.008, 22.977)), ((6.008, 22.028), (6.188, 21.038), (6.36, 20.105)), ((7.841, 12.046), (15.147, 6.016), (23.362, 6.016)), ((23.681, 6.016), (24.008, 6), (24.335, 6)), ((24.337, 6), (24.338, 6), (24.34, 6)), ((24.428, 6), (24.517, 6), (24.605, 6)), ((25.35, 6), (26.135, 6.147), (26.88, 6.262)), ((31.445, 6.965), (35.438, 9.363), (38.318, 12.963)), ((39.415, 14.329), (40.075, 15.519), (41, 17)))
        self.add_bezier('e7', (7, 31), ((8.055, 32.563), (8.954, 34.604), (10.287, 35.954)), ((13.797, 39.496), (18.518, 41.992), (23.599, 41.992)), ((23.672, 41.992), (23.752, 42), (23.825, 42)), ((23.826, 42), (23.827, 42), (23.828, 42)), ((23.984, 42), (24.131, 41.984), (24.286, 41.984)), ((31.413, 41.984), (38.318, 37.394), (40.609, 30.586)), ((40.789, 30.046), (40.885, 29.565), (41, 29)))
        self.add_contour('c0', 'e6', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e7', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
