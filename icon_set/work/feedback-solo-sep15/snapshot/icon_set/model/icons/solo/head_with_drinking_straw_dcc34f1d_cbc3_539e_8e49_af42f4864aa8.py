"""A human head in left-facing profile has a projecting nose, rounded skull and open neck. A bent drinking straw enters the top and meets a wavy liquid line inside the head.
Left-facing head with physical straw and liquid. Deliberate asymmetric profile. No useful exact Lucide head match; broad circular skull construction.
Keyshape VRECT_L; centerline extremes (8,6)-(40,42). Tall envelope fits the upright subject. Source inspected as a standalone physical or conceptual subject."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dcc34f1d-cbc3-539e-8e49-af42f4864aa8'
SOURCE_PATH = 'pictographic-primitives/work/creative juice head_dcc34f1d-cbc3-539e-8e49-af42f4864aa8.svg'
AUTHOR = 'gpt-6'

class HeadWithDrinkingStraw(Solo48):
    icon_id = 'head-with-drinking-straw'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/work'
    aliases = ()
    keywords = ('head', 'profile', 'straw', 'drink', 'creativity', 'thinking')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_arc('forehead', (21, 10), (10, 23), radius_x=11, radius_y=13, sweep=False, large_arc=False)
        self.add_line('face-1', (10, 23), (8, 29))
        self.add_line('face-2', (8, 29), (13, 29))
        self.add_line('face-3', (13, 29), (13, 35))
        self.add_arc('chin', (13, 35), (20, 42), radius_x=7, radius_y=7, sweep=False, large_arc=False)
        self.add_line('neck-front', (20, 42), (20, 44))
        self.add_contour('face-outline', 'forehead', 'face-1', 'face-2', 'face-3', 'chin', 'neck-front', closed=False)
        self.add_arc('skull', (38, 17), (35, 34), radius_x=17, radius_y=17, sweep=True, large_arc=False)
        self.add_line('neck-back', (35, 34), (34, 44))
        self.add_contour('back-outline', 'skull', 'neck-back', closed=False)
        self.add_polyline('straw', (40, 4), (32, 4), (27, 26), closed=False)
        self.add_arc('liquid', (22, 26), (27, 26), radius_x=8, radius_y=3, sweep=True, large_arc=False)
        self.relate('connect', 'liquid', 'straw')
