'A person stands in side view with a round head and a prominent rounded belly projecting left. One arm bends back toward the hip above a short flared garment and visible leg.\n\nConstruction: Side profile with a curved pregnant abdomen, circular head and an arm resting on the lower back. Bounds (8,4)-(40,44).\nLucide: person-standing: separate circular head and connected limbs.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2230e8dc-ec40-46aa-97fe-c7a3278e68e9'
SOURCE_PATH = 'pictographic-primitives/wayfinding/disability pregant_2230e8dc-ec40-46aa-97fe-c7a3278e68e9.svg'
AUTHOR = 'gpt-6'

class StandingPregnantPerson(Solo48):
    icon_id = 'standing-pregnant-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('pregnant', 'pregnancy', 'person', 'standing', 'maternity', 'belly')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('head-top', (21, 7), (27, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (27, 7), (21, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('back-1', (20, 19), (16, 34))
        self.add_line('back-2', (16, 34), (16, 44))
        self.add_arc('belly', (20, 19), (8, 34), radius_x=12, radius_y=15, large_arc=False, sweep=False)
        self.add_line('belly-base', (8, 34), (16, 34))
        self.add_line('arm-1', (20, 19), (40, 25))
        self.add_line('arm-2', (40, 25), (34, 34))
        self.add_line('leg', (16, 34), (26, 44))
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_contour('back', 'back-1', 'back-2', closed=False)
        self.add_contour('abdomen', 'belly', 'belly-base', closed=False)
        self.add_contour('arm', 'arm-1', 'arm-2', closed=False)
        self.relate('connect', 'back', 'abdomen')
        self.relate('connect', 'back', 'arm')
        self.relate('connect', 'back', 'leg')
