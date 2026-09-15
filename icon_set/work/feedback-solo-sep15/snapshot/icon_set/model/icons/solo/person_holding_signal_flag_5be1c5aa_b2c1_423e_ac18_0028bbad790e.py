'A front-facing person stretches both arms horizontally. A short flagpole rises from the right hand and carries a small rectangular flag near its upper end.\n\nConstruction: Standing figure with an outstretched arm holding a rectangular signal flag. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5be1c5aa-b2c1-423e-ac18-0028bbad790e'
SOURCE_PATH = 'pictographic-primitives/wayfinding/signal flag_5be1c5aa-b2c1-423e-ac18-0028bbad790e.svg'
AUTHOR = 'gpt-6'

class PersonHoldingSignalFlag(Solo48):
    icon_id = 'person-holding-signal-flag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'flag', 'signal', 'semaphore', 'communication', 'standing')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (19, 9), (25, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (25, 9), (19, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-torso-1', (22, 21), (22, 31))
        self.add_line('person-arms-1', (6, 21), (22, 21))
        self.add_line('person-arms-2', (22, 21), (34, 21))
        self.add_line('person-legs-1', (14, 42), (22, 31))
        self.add_line('person-legs-2', (22, 31), (30, 42))
        self.add_line('flag-1', (34, 29), (34, 21))
        self.add_line('flag-2-joint-1', (34, 21), (34, 14))
        self.add_line('flag-2-joint-2', (34, 14), (34, 6))
        self.add_line('flag-3', (34, 6), (42, 6))
        self.add_line('flag-4', (42, 6), (42, 14))
        self.add_line('flag-5', (42, 14), (34, 14))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-torso', 'person-torso-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', closed=False)
        self.add_contour('flag', 'flag-1', 'flag-2-joint-1', 'flag-2-joint-2', 'flag-3', 'flag-4', 'flag-5', closed=False)
        self.relate('connect', 'person-torso', 'person-arms')
        self.relate('connect', 'person-torso', 'person-legs')
        self.relate('connect', 'flag', 'person-arms')
