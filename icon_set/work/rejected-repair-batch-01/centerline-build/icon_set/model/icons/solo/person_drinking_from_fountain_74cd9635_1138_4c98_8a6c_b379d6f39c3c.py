'A person bends forward toward a wall-mounted drinking fountain on the right. The arms gather below the face, and a short arcing stream rises above the shallow curved basin.\n\nConstruction: Bent figure leans toward a wall fountain and short water arc. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '74cd9635-1138-4c98-8a6c-b379d6f39c3c'
SOURCE_PATH = 'pictographic-primitives/wayfinding/water fountain drink_74cd9635-1138-4c98-8a6c-b379d6f39c3c.svg'
AUTHOR = 'gpt-6'

class PersonDrinkingFromFountain(Solo48):
    icon_id = 'person-drinking-from-fountain'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'drinking', 'fountain', 'water', 'basin', 'hydration')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (23, 11), (29, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (29, 11), (23, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (17, 22), (8, 28))
        self.add_line('person-body-2', (8, 28), (4, 40))
        self.add_line('person-arm-1', (17, 22), (20, 31))
        self.add_line('person-arm-2', (20, 31), (32, 26))
        self.add_arc('bowl', (32, 26), (44, 38), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_line('wall-1', (32, 26), (44, 26))
        self.add_line('wall-2-joint-1', (44, 26), (44, 38))
        self.add_line('wall-2-joint-2', (44, 38), (44, 40))
        self.add_arc('water', (36, 17), (44, 17), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', 'person-body-2', closed=False)
        self.add_contour('person-arm', 'person-arm-1', 'person-arm-2', closed=False)
        self.add_contour('wall', 'wall-1', 'wall-2-joint-1', 'wall-2-joint-2', closed=False)
        self.relate('connect', 'person-body', 'person-arm')
        self.relate('connect', 'bowl', 'wall')
        self.relate('connect', 'person-arm', 'bowl')
        self.relate('connect', 'person-arm', 'wall')
