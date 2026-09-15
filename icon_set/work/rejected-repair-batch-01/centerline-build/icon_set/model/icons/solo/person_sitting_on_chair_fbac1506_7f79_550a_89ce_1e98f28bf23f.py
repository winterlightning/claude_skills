'A person sits facing right with an upright torso and legs angled down and forward. A curved chair outline follows the back and runs underneath the thighs.\n\nConstruction: Upright seated figure with a bent knee and a chair back beneath the torso. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fbac1506-7f79-550a-89ce-1e98f28bf23f'
SOURCE_PATH = 'pictographic-primitives/wayfinding/sitting chair_fbac1506-7f79-550a-89ce-1e98f28bf23f.svg'
AUTHOR = 'gpt-6'

class PersonSittingOnChair(Solo48):
    icon_id = 'person-sitting-on-chair'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'sitting', 'chair', 'seat', 'rest', 'posture')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (19, 7), (25, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (25, 7), (19, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (20, 19), (24, 32))
        self.add_line('person-body-2', (24, 32), (34, 32))
        self.add_line('person-body-3', (34, 32), (40, 44))
        self.add_line('chair-1', (8, 20), (12, 42))
        self.add_line('chair-2', (12, 42), (26, 42))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', 'person-body-2', 'person-body-3', closed=False)
        self.add_contour('chair', 'chair-1', 'chair-2', closed=False)
