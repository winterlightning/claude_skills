"A person leans forward while walking behind a wheeled support frame. Both arms reach to its horizontal top rail, and the frame's two visible legs end in small round wheels.\n\nConstruction: Forward-leaning figure gripping a two-legged walking frame. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de20bd32-9f49-4bd0-b839-0dc64ce6f8ae'
SOURCE_PATH = 'pictographic-primitives/wayfinding/disability walking help_de20bd32-9f49-4bd0-b839-0dc64ce6f8ae.svg'
AUTHOR = 'gpt-6'

class PersonUsingWalkingFrame(Solo48):
    icon_id = 'person-using-walking-frame'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('walker', 'frame', 'person', 'walking', 'mobility', 'accessibility')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (11, 9), (17, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (17, 9), (11, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (14, 21), (12, 31))
        self.add_line('person-legs-1', (6, 42), (12, 31))
        self.add_line('person-legs-2', (12, 31), (20, 42))
        self.add_line('person-arm-1', (14, 21), (24, 25))
        self.add_line('frame-1', (24, 42), (26, 25))
        self.add_line('frame-2', (26, 25), (40, 25))
        self.add_line('frame-3', (40, 25), (42, 42))
        self.add_line('grip', (24, 25), (26, 25))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', closed=False)
        self.add_contour('person-arm', 'person-arm-1', closed=False)
        self.add_contour('frame', 'frame-1', 'frame-2', 'frame-3', closed=False)
        self.relate('connect', 'person-body', 'person-legs')
        self.relate('connect', 'person-body', 'person-arm')
        self.relate('connect', 'grip', 'person-arm')
        self.relate('connect', 'grip', 'frame')
