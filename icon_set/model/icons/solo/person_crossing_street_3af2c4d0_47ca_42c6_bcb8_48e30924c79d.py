'A person walks toward the right with one knee bent and the arms swinging apart. Two pairs of short slanted road markings flank the legs to suggest a crossing.\n\nConstruction: Walking figure above two road crossing stripes. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3af2c4d0-47ca-42c6-bcb8-48e30924c79d'
SOURCE_PATH = 'pictographic-primitives/wayfinding/walking cross street_3af2c4d0-47ca-42c6-bcb8-48e30924c79d.svg'
AUTHOR = 'gpt-6'

class PersonCrossingStreet(Solo48):
    icon_id = 'person-crossing-street'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'crossing', 'street', 'walking', 'pedestrian', 'road')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (21, 9), (27, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (27, 9), (21, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (24, 21), (22, 29))
        self.add_line('person-arms-1', (12, 27), (24, 21))
        self.add_line('person-arms-2', (24, 21), (36, 26))
        self.add_line('person-legs-1', (14, 39), (22, 29))
        self.add_line('person-legs-2', (22, 29), (31, 39))
        self.add_line('stripe-left', (6, 34), (6, 42))
        self.add_line('stripe-right', (42, 34), (42, 42))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', closed=False)
        self.relate('connect', 'person-body', 'person-arms')
        self.relate('connect', 'person-body', 'person-legs')
