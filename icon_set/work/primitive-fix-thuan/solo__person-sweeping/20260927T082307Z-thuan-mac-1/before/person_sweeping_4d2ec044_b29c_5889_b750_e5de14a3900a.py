"A person grips a tall broom with both arms in front of the body. The broom's long handle slopes slightly left and ends in a curved fan of bristles beside the legs.\n\nConstruction: Standing figure grips a long broom beside a broad bristle head. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d2ec044-b29c-5889-b750-e5de14a3900a'
SOURCE_PATH = 'pictographic-primitives/wayfinding/sweeping_4d2ec044-b29c-5889-b750-e5de14a3900a.svg'
AUTHOR = 'gpt-6'

class PersonSweeping(Solo48):
    icon_id = 'person-sweeping'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'sweeping', 'broom', 'cleaning', 'floor', 'housework')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (27, 7), (33, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (33, 7), (27, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (30, 19), (30, 32))
        self.add_line('person-body-2', (30, 32), (40, 44))
        self.add_line('person-arm-1', (30, 19), (14, 24))
        self.add_line('broom-handle-1', (8, 12), (14, 24))
        self.add_line('broom-handle-2', (14, 24), (20, 34))
        self.add_line('bristles-1', (20, 34), (12, 44))
        self.add_line('bristles-2', (12, 44), (28, 44))
        self.add_line('bristles-3', (28, 44), (20, 34))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', 'person-body-2', closed=False)
        self.add_contour('person-arm', 'person-arm-1', closed=False)
        self.add_contour('broom-handle', 'broom-handle-1', 'broom-handle-2', closed=False)
        self.add_contour('bristles', 'bristles-1', 'bristles-2', 'bristles-3', closed=False)
        self.relate('connect', 'person-body', 'person-arm')
        self.relate('connect', 'broom-handle', 'person-arm')
        self.relate('connect', 'bristles', 'broom-handle')
