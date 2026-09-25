'A front-facing person stands with knees and legs crossed. Both arms curve inward so the hands meet low in front of the body below the circular head.\n\nConstruction: Front-facing figure holds both hands low with crossed legs. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb4a3a21-81c2-4505-9136-3a3335da3b2e'
SOURCE_PATH = 'pictographic-primitives/wayfinding/toilet need_eb4a3a21-81c2-4505-9136-3a3335da3b2e.svg'
AUTHOR = 'gpt-6'

class PersonNeedingToilet(Solo48):
    icon_id = 'person-needing-toilet'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('person', 'toilet', 'urgency', 'restroom', 'crossed', 'legs')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (21, 7), (27, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (27, 7), (21, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (24, 19), (24, 31))
        self.add_line('person-arms-1', (24, 19), (8, 21))
        self.add_line('person-arms-2', (8, 21), (12, 30))
        self.add_line('person-arms-3', (12, 30), (24, 34))
        self.add_line('person-arms-4', (24, 34), (36, 30))
        self.add_line('person-arms-5', (36, 30), (40, 21))
        self.add_line('person-arms-6', (40, 21), (24, 19))
        self.add_line('person-legs-1', (16, 44), (24, 34))
        self.add_line('person-legs-2', (24, 34), (32, 44))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', 'person-arms-3', 'person-arms-4', 'person-arms-5', 'person-arms-6', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', closed=False)
        self.relate('connect', 'person-body', 'person-arms')
        self.relate('connect', 'person-arms', 'person-legs')
