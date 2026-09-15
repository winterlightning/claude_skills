"A person stands in profile facing a tall wall urinal at the right. The knees bend slightly and the hands sit at waist level above the urinal's curved projecting bowl.\n\nConstruction: Standing person faces a wall-mounted urinal and reaches toward it. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3fab3c5-ba7f-5ddc-bffc-006d5f47d770'
SOURCE_PATH = 'pictographic-primitives/wayfinding/wayfinding urinal_e3fab3c5-ba7f-5ddc-bffc-006d5f47d770.svg'
AUTHOR = 'gpt-6'

class PersonUsingUrinal(Solo48):
    icon_id = 'person-using-urinal'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'urinal', 'toilet', 'restroom', 'bathroom', 'standing')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (17, 7), (23, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (23, 7), (17, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (16, 19), (12, 30))
        self.add_line('person-arms-1', (16, 19), (22, 27))
        self.add_line('person-legs-1', (8, 44), (12, 30))
        self.add_line('person-legs-2', (12, 30), (20, 36))
        self.add_line('person-legs-3', (20, 36), (18, 44))
        self.add_line('urinal-1', (40, 14), (32, 14))
        self.add_line('urinal-2', (32, 14), (32, 30))
        self.add_line('urinal-3', (32, 30), (28, 34))
        self.add_line('urinal-4', (28, 34), (32, 40))
        self.add_line('urinal-5', (32, 40), (32, 44))
        self.add_line('urinal-6', (32, 44), (40, 44))
        self.add_line('urinal-7', (40, 44), (40, 14))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', 'person-legs-3', closed=False)
        self.add_contour('urinal', 'urinal-1', 'urinal-2', 'urinal-3', 'urinal-4', 'urinal-5', 'urinal-6', 'urinal-7', closed=False)
        self.relate('connect', 'person-body', 'person-arms')
        self.relate('connect', 'person-body', 'person-legs')
