"A person's circular head and short upper body rise behind an escalator balustrade. The long enclosed rail climbs diagonally from lower-left to upper-right with rounded horizontal ends.\n\nConstruction: One upright passenger behind an ascending escalator band. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9afef0ba-76dd-58ef-a48e-cda905a50b5c'
SOURCE_PATH = 'pictographic-primitives/wayfinding/escalator person_9afef0ba-76dd-58ef-a48e-cda905a50b5c.svg'
AUTHOR = 'gpt-6'

class PersonOnEscalator(Solo48):
    icon_id = 'person-on-escalator'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('escalator', 'person', 'transport', 'stairs', 'moving', 'wayfinding')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('head-top', (11, 11), (17, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (17, 11), (11, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('body', (14, 23), (14, 28))
        self.add_line('escalator-1', (4, 40), (16, 40))
        self.add_line('escalator-2', (16, 40), (36, 24))
        self.add_line('escalator-3', (36, 24), (44, 24))
        self.add_line('escalator-4', (44, 24), (44, 14))
        self.add_line('escalator-5', (44, 14), (32, 14))
        self.add_line('escalator-6', (32, 14), (14, 28))
        self.add_line('escalator-7', (14, 28), (4, 28))
        self.add_line('escalator-8', (4, 28), (4, 40))
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_contour('escalator', 'escalator-1', 'escalator-2', 'escalator-3', 'escalator-4', 'escalator-5', 'escalator-6', 'escalator-7', 'escalator-8', closed=True)
        self.relate('connect', 'body', 'escalator')
