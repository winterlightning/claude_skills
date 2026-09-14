'A person runs through an open doorway with one arm and both legs spread across its opening. Two tall jambs join across the top and end in short outward feet.\n\nConstruction: Runner crosses a door frame; jamb breaks occur where the arms pass through. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1e6b172-0589-49ee-9311-e9b8ae8c07ff'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety exit door_e1e6b172-0589-49ee-9311-e9b8ae8c07ff.svg'
AUTHOR = 'gpt-6'

class PersonRunningThroughDoorway(Solo48):
    icon_id = 'person-running-through-doorway'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('exit', 'doorway', 'running', 'person', 'escape', 'safety')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (21, 18), (27, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (27, 18), (21, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (23, 30), (20, 34))
        self.add_line('person-arms-1', (6, 28), (14, 28))
        self.add_line('person-arms-2', (14, 28), (23, 30))
        self.add_line('person-arms-3', (23, 30), (34, 32))
        self.add_line('person-arms-4', (34, 32), (42, 32))
        self.add_line('person-legs-1', (14, 42), (20, 34))
        self.add_line('person-legs-2', (20, 34), (28, 40))
        self.add_line('person-legs-3', (28, 40), (34, 40))
        self.add_line('door-top-1', (6, 18), (6, 6))
        self.add_line('door-top-2', (6, 6), (42, 6))
        self.add_line('door-top-3', (42, 6), (42, 22))
        self.add_line('door-bottom', (42, 32), (42, 42))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', 'person-arms-3', 'person-arms-4', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', 'person-legs-3', closed=False)
        self.add_contour('door-top', 'door-top-1', 'door-top-2', 'door-top-3', closed=False)
        self.relate('connect', 'person-body', 'person-arms')
        self.relate('connect', 'person-body', 'person-legs')
        self.relate('connect', 'door-bottom', 'person-arms')
