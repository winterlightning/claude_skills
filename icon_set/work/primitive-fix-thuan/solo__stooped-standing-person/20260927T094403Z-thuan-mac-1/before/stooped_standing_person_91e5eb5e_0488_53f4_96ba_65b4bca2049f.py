'A person stands in profile with the head lowered and the upper back rounded forward. The long body drops nearly vertically, with a short bent arm hanging near the chest.\n\nConstruction: Circular head and connected shoulder/hip graph preserve the reference posture; clothing outlines and minor folds omitted. Bounds (8,4)-(40,44).\nLucide: person-standing: separate round head, common limb junctions.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91e5eb5e-0488-53f4-96ba-65b4bca2049f'
SOURCE_PATH = 'pictographic-primitives/wayfinding/standing stooped_91e5eb5e-0488-53f4-96ba-65b4bca2049f.svg'
AUTHOR = 'gpt-6'

class StoopedStandingPerson(Solo48):
    icon_id = 'stooped-standing-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'stooped', 'standing', 'posture', 'bending', 'figure')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (29, 7), (35, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (35, 7), (29, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (24, 19), (16, 30))
        self.add_line('person-body-2', (16, 30), (16, 44))
        self.add_line('person-arm-1', (24, 19), (28, 32))
        self.add_line('person-back-foot-1', (16, 30), (8, 44))
        self.add_line('person-hand-1', (28, 32), (40, 32))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', 'person-body-2', closed=False)
        self.add_contour('person-arm', 'person-arm-1', closed=False)
        self.add_contour('person-back-foot', 'person-back-foot-1', closed=False)
        self.add_contour('person-hand', 'person-hand-1', closed=False)
        self.relate('connect', 'person-body', 'person-arm')
        self.relate('connect', 'person-body', 'person-back-foot')
        self.relate('connect', 'person-arm', 'person-hand')
