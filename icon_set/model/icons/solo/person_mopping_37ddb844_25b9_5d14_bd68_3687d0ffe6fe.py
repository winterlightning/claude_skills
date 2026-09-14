'A person leans forward with staggered legs and both arms reaching toward a long diagonal mop handle. The handle ends in a wide rounded cleaning head resting at the lower-left.\n\nConstruction: Circular head, leaning stick figure and long mop handle. Limbs share shoulder and hip nodes; reduced filled clothing outline. Bounds (6,6)-(42,42).\nLucide: person-standing: circle head and shared limb junctions.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37ddb844-25b9-5d14-bd68-3687d0ffe6fe'
SOURCE_PATH = 'pictographic-primitives/wayfinding/cleanser moping_37ddb844-25b9-5d14-bd68-3687d0ffe6fe.svg'
AUTHOR = 'gpt-6'

class PersonMopping(Solo48):
    icon_id = 'person-mopping'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'mop', 'mopping', 'cleaning', 'floor', 'housework')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('head-top', (25, 9), (31, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (31, 9), (25, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('body-1', (30, 21), (25, 29))
        self.add_line('body-2', (25, 29), (31, 34))
        self.add_line('body-3', (31, 34), (35, 42))
        self.add_line('rear-leg-1', (25, 29), (20, 42))
        self.add_line('arm-1', (30, 21), (23, 25))
        self.add_line('arm-2', (23, 25), (17, 25))
        self.add_line('mop-shaft', (17, 25), (10, 34))
        self.add_line('mop-head-0', (10, 34), (14, 34))
        self.add_arc('mop-head-1', (14, 34), (18, 38), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('mop-head-2', (18, 38), (18, 38))
        self.add_arc('mop-head-3', (18, 38), (14, 42), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('mop-head-4', (14, 42), (10, 42))
        self.add_arc('mop-head-5', (10, 42), (6, 38), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('mop-head-6', (6, 38), (6, 38))
        self.add_arc('mop-head-7', (6, 38), (10, 34), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('far-arm', (30, 21), (38, 25))
        self.add_line('foot', (35, 42), (42, 42))
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', closed=False)
        self.add_contour('rear-leg', 'rear-leg-1', closed=False)
        self.add_contour('arm', 'arm-1', 'arm-2', closed=False)
        self.add_contour('mop-head', 'mop-head-0', 'mop-head-1', 'mop-head-2', 'mop-head-3', 'mop-head-4', 'mop-head-5', 'mop-head-6', 'mop-head-7', closed=True)
        self.relate('connect', 'body', 'rear-leg')
        self.relate('connect', 'body', 'arm')
        self.relate('connect', 'arm', 'mop-shaft')
        self.relate('connect', 'mop-shaft', 'mop-head')
        self.relate('connect', 'body', 'far-arm')
        self.relate('connect', 'body', 'foot')
