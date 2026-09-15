'A seated person faces right with an arm extended forward and legs bending downward. A curved chair supports the back and thighs, and a tall hooked cane stands beside the hand.\n\nConstruction: Sideways seated figure reaching toward a hooked cane; reduced chair to its seat. Bounds (8,4)-(40,44).\nLucide: person-standing: node-based human construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1ea697d7-e80d-4a42-b015-acd8cd95ff6c'
SOURCE_PATH = 'pictographic-primitives/wayfinding/disability sit cane_1ea697d7-e80d-4a42-b015-acd8cd95ff6c.svg'
AUTHOR = 'gpt-6'

class SeatedPersonWithCane(Solo48):
    icon_id = 'seated-person-with-cane'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'seated', 'cane', 'chair', 'accessibility', 'mobility')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (12, 7), (18, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (18, 7), (12, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (12, 19), (16, 32))
        self.add_line('person-body-2', (16, 32), (26, 32))
        self.add_line('person-body-3', (26, 32), (28, 44))
        self.add_line('person-arm-1', (12, 19), (24, 21))
        self.add_line('seat', (8, 40), (18, 40))
        self.add_arc('cane-hook', (32, 24), (40, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('cane-shaft', (40, 24), (40, 44))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', 'person-body-2', 'person-body-3', closed=False)
        self.add_contour('person-arm', 'person-arm-1', closed=False)
        self.add_contour('cane', 'cane-hook', 'cane-shaft', closed=False)
        self.relate('connect', 'person-body', 'person-arm')
