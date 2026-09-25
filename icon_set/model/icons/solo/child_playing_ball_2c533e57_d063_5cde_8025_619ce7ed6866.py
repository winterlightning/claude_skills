'A child moves toward a small ball at the left with one leg extended and the other bent beneath the body. The arms spread in opposite directions around a circular head.\n\nConstruction: A child raises one arm and kicks toward a detached ball. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c533e57-d063-5cde-8025-619ce7ed6866'
SOURCE_PATH = 'pictographic-primitives/wayfinding/family child play ball_2c533e57-d063-5cde-8025-619ce7ed6866.svg'
AUTHOR = 'gpt-6'

class ChildPlayingBall(Solo48):
    icon_id = 'child-playing-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('child', 'ball', 'play', 'kicking', 'sport', 'person')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (24, 9), (30, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (30, 9), (24, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (26, 23), (23, 30))
        self.add_line('person-arm-1', (20, 23), (26, 23))
        self.add_line('person-arm-2', (26, 23), (38, 18))
        self.add_line('person-legs-1', (15, 39), (23, 30))
        self.add_line('person-legs-2', (23, 30), (32, 34))
        self.add_line('person-legs-3', (32, 34), (35, 42))
        self.add_arc('ball-top', (6, 28), (12, 28), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('ball-bottom', (12, 28), (6, 28), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('raised-hand', (38, 18), (42, 18))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', closed=False)
        self.add_contour('person-arm', 'person-arm-1', 'person-arm-2', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', 'person-legs-3', closed=False)
        self.add_contour('ball', 'ball-top', 'ball-bottom', closed=True)
        self.relate('connect', 'person-body', 'person-arm')
        self.relate('connect', 'person-body', 'person-legs')
        self.relate('connect', 'raised-hand', 'person-arm')
