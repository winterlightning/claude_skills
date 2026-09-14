'Two front-facing human figures stand side by side with matching circular heads and simple bodies. The left figure has a continuous outline, while the right figure is traced with separated dashes.\n\nConstruction: Two standing people, one continuous and one broken into spaced segments. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58fce536-ad33-4c76-86df-d52bb405808c'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety missing people_58fce536-ad33-4c76-86df-d52bb405808c.svg'
AUTHOR = 'gpt-6'

class MissingPersonPair(Solo48):
    icon_id = 'missing-person-pair'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('missing', 'person', 'people', 'absence', 'outline', 'safety')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('present-head-top', (11, 11), (17, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('present-head-bottom', (17, 11), (11, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('present-body-1', (14, 23), (14, 30))
        self.add_line('present-arms-1', (4, 28), (14, 23))
        self.add_line('present-arms-2', (14, 23), (22, 28))
        self.add_line('present-legs-1', (8, 40), (14, 30))
        self.add_line('present-legs-2', (14, 30), (20, 40))
        self.add_arc('missing-head-top', (33, 11), (39, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('missing-head-bottom', (39, 11), (33, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('missing-body', (36, 23), (36, 27))
        self.add_line('missing-leg-left', (30, 36), (28, 40))
        self.add_line('missing-leg-right', (40, 36), (44, 40))
        self.add_contour('present-head', 'present-head-top', 'present-head-bottom', closed=True)
        self.add_contour('present-body', 'present-body-1', closed=False)
        self.add_contour('present-arms', 'present-arms-1', 'present-arms-2', closed=False)
        self.add_contour('present-legs', 'present-legs-1', 'present-legs-2', closed=False)
        self.add_contour('missing-head', 'missing-head-top', 'missing-head-bottom', closed=True)
        self.relate('connect', 'present-body', 'present-arms')
        self.relate('connect', 'present-body', 'present-legs')
