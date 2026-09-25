'A front-facing person stands with a circular head, straight torso and joined legs. One arm reaches diagonally down to a slender upright cane at the left side.\n\nConstruction: Upright stick figure with a separate hooked walking cane held at the left. Bounds (8,4)-(40,44).\nLucide: person-standing: circle head and node-based limbs.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a800daf7-9ae0-4343-8f29-26aa7acbf5fd'
SOURCE_PATH = 'pictographic-primitives/wayfinding/disability cane_a800daf7-9ae0-4343-8f29-26aa7acbf5fd.svg'
AUTHOR = 'gpt-6'

class PersonWithWalkingCane(Solo48):
    icon_id = 'person-with-walking-cane'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('person', 'cane', 'walking', 'mobility', 'accessibility', 'support')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('head-top', (23, 7), (29, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (29, 7), (23, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('body-1', (26, 19), (26, 31))
        self.add_line('body-2', (26, 31), (20, 44))
        self.add_line('leg-1', (26, 31), (32, 44))
        self.add_line('arms-1', (14, 27), (26, 19))
        self.add_line('arms-2', (26, 19), (40, 27))
        self.add_arc('cane-hook', (14, 27), (8, 33), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('cane', (8, 33), (8, 44))
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_contour('body', 'body-1', 'body-2', closed=False)
        self.add_contour('leg', 'leg-1', closed=False)
        self.add_contour('arms', 'arms-1', 'arms-2', closed=False)
        self.add_contour('walking-cane', 'cane-hook', 'cane', closed=False)
        self.relate('connect', 'body', 'leg')
        self.relate('connect', 'body', 'arms')
        self.relate('connect', 'walking-cane', 'arms')
