'A person sits facing right on a curved-backed chair with bent legs. A pendant lamp hangs above and ahead of the head, with a domed shade and short suspension line.\n\nConstruction: Seated visitor beneath a hanging dome lamp at upper-right. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '792a93a1-5358-4e2a-bec7-9ae27256ac06'
SOURCE_PATH = 'pictographic-primitives/wayfinding/waiting room lamp_792a93a1-5358-4e2a-bec7-9ae27256ac06.svg'
AUTHOR = 'gpt-6'

class PersonSeatedUnderLamp(Solo48):
    icon_id = 'person-seated-under-lamp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('person', 'seated', 'lamp', 'waiting', 'room', 'chair')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (12, 22), (18, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (18, 22), (12, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (16, 34), (26, 34))
        self.add_line('person-body-2', (26, 34), (30, 42))
        self.add_line('chair-1', (6, 30), (8, 42))
        self.add_line('chair-2', (8, 42), (18, 42))
        self.add_line('lamp-cord', (34, 6), (34, 10))
        self.add_arc('shade-joint-1', (26, 18), (34, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('shade-joint-2', (34, 10), (42, 18), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('shade-rim', (42, 18), (26, 18))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', 'person-body-2', closed=False)
        self.add_contour('chair', 'chair-1', 'chair-2', closed=False)
        self.add_contour('lamp', 'shade-joint-1', 'shade-joint-2', 'shade-rim', closed=True)
        self.relate('connect', 'lamp-cord', 'lamp')
