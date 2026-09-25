'A person stands with legs spread and a flag held in each hand. The left arm rises diagonally with its flag above the head, while the right arm extends sideways with its flag hanging below.\n\nConstruction: Standing figure raises one signal flag and lowers the opposite one. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63795476-e3b5-5351-a24f-0e6e98427fff'
SOURCE_PATH = 'pictographic-primitives/wayfinding/signal flags_63795476-e3b5-5351-a24f-0e6e98427fff.svg'
AUTHOR = 'gpt-6'

class PersonHoldingTwoSignalFlags(Solo48):
    icon_id = 'person-holding-two-signal-flags'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'flags', 'semaphore', 'signal', 'communication', 'standing')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (23, 9), (29, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (29, 9), (23, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-torso-1', (24, 23), (24, 31))
        self.add_line('person-arms-1', (14, 18), (24, 23))
        self.add_line('person-arms-2', (24, 23), (34, 24))
        self.add_line('person-legs-1', (16, 42), (24, 31))
        self.add_line('person-legs-2', (24, 31), (32, 42))
        self.add_line('flag-left-1', (14, 18), (6, 18))
        self.add_line('flag-left-2', (6, 18), (6, 8))
        self.add_line('flag-left-3', (6, 8), (14, 8))
        self.add_line('flag-left-4', (14, 8), (14, 18))
        self.add_line('flag-right-1', (34, 24), (42, 24))
        self.add_line('flag-right-2', (42, 24), (42, 34))
        self.add_line('flag-right-3', (42, 34), (34, 34))
        self.add_line('flag-right-4', (34, 34), (34, 24))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-torso', 'person-torso-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', closed=False)
        self.add_contour('flag-left', 'flag-left-1', 'flag-left-2', 'flag-left-3', 'flag-left-4', closed=False)
        self.add_contour('flag-right', 'flag-right-1', 'flag-right-2', 'flag-right-3', 'flag-right-4', closed=False)
        self.relate('connect', 'person-torso', 'person-arms')
        self.relate('connect', 'person-torso', 'person-legs')
        self.relate('connect', 'flag-left', 'person-arms')
        self.relate('connect', 'flag-right', 'person-arms')
