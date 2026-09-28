'A person leans forward while seated on a toilet, with bent legs below and both arms reaching toward a tall hooked cane. The toilet bowl projects behind the seated figure.\n\nConstruction: Seated person holds a hooked cane beside a low toilet bowl. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '115f3835-52a5-5ab6-8729-8649b92e053e'
SOURCE_PATH = 'pictographic-primitives/wayfinding/disability toilet_115f3835-52a5-5ab6-8729-8649b92e053e.svg'
AUTHOR = 'gpt-6'

class PersonUsingToiletWithCane(Solo48):
    icon_id = 'person-using-toilet-with-cane'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('toilet', 'cane', 'person', 'accessibility', 'seated', 'washroom')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (19, 11), (25, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (25, 11), (19, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (20, 23), (20, 32))
        self.add_line('person-body-2', (20, 32), (28, 32))
        self.add_line('person-body-3', (28, 32), (30, 40))
        self.add_line('person-arm-1', (20, 23), (30, 23))
        self.add_line('person-arm-2', (30, 23), (36, 20))
        self.add_arc('toilet-bowl', (4, 32), (20, 32), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('cane-top', (36, 20), (44, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('cane', (44, 20), (44, 40))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', 'person-body-2', 'person-body-3', closed=False)
        self.add_contour('person-arm', 'person-arm-1', 'person-arm-2', closed=False)
        self.add_contour('walking-cane', 'cane-top', 'cane', closed=False)
        self.relate('connect', 'person-body', 'person-arm')
        self.relate('connect', 'toilet-bowl', 'person-body')
        self.relate('connect', 'person-arm', 'walking-cane')
