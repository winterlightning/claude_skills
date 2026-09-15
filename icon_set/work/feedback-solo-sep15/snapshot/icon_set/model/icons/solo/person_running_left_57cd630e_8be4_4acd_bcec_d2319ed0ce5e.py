'A person runs left with a bent forward arm and legs spread mid-stride. Four short horizontal speed strokes trail behind the rounded torso at the right.\n\nConstruction: Leftward runner with a compact pair of trailing speed marks. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57cd630e-8be4-4acd-bcec-d2319ed0ce5e'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety fire exit_57cd630e-8be4-4acd-bcec-d2319ed0ce5e.svg'
AUTHOR = 'gpt-6'

class PersonRunningLeft(Solo48):
    icon_id = 'person-running-left'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('running', 'person', 'left', 'speed', 'escape', 'motion')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (13, 9), (19, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (19, 9), (13, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-torso-1', (18, 21), (22, 30))
        self.add_line('person-arms-1', (6, 23), (12, 25))
        self.add_line('person-arms-2', (12, 25), (18, 21))
        self.add_line('person-arms-3', (18, 21), (26, 24))
        self.add_line('person-legs-1', (12, 42), (12, 34))
        self.add_line('person-legs-2', (12, 34), (22, 30))
        self.add_line('person-legs-3', (22, 30), (30, 38))
        self.add_line('speed-upper', (35, 16), (42, 16))
        self.add_line('speed-lower', (35, 26), (42, 26))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-torso', 'person-torso-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', 'person-arms-3', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', 'person-legs-3', closed=False)
        self.relate('connect', 'person-torso', 'person-arms')
        self.relate('connect', 'person-torso', 'person-legs')
