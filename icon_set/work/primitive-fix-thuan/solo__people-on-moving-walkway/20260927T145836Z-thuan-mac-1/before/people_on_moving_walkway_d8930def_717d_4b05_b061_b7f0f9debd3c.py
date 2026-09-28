'Two people appear as circular heads and short shoulders above a horizontal moving walkway. Its lower outline curves around a rounded left end and continues straight toward the right.\n\nConstruction: Two people above a rounded walkway band. Taller square keyshape gives each torso an eight-unit interior opening. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8930def-717d-4b05-b061-b7f0f9debd3c'
SOURCE_PATH = 'pictographic-primitives/wayfinding/moving walkway people_d8930def-717d-4b05-b061-b7f0f9debd3c.svg'
AUTHOR = 'gpt-6'

class PeopleOnMovingWalkway(Solo48):
    icon_id = 'people-on-moving-walkway'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('walkway', 'moving', 'people', 'travel', 'transport', 'airport')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('head-14-top', (11, 9), (17, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('head-14-bottom', (17, 9), (11, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('shoulder-left-14', (8, 34), (8, 28))
        self.add_arc('shoulders-14', (8, 28), (20, 28), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('shoulder-right-14', (20, 28), (20, 34))
        self.add_arc('head-35-top', (32, 9), (38, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('head-35-bottom', (38, 9), (32, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('shoulder-left-35', (29, 34), (29, 28))
        self.add_arc('shoulders-35', (29, 28), (41, 28), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('shoulder-right-35', (41, 28), (41, 34))
        self.add_line('walkway-top-joint-1', (42, 34), (41, 34))
        self.add_line('walkway-top-joint-2', (41, 34), (29, 34))
        self.add_line('walkway-top-joint-3', (29, 34), (20, 34))
        self.add_line('walkway-top-joint-4', (20, 34), (8, 34))
        self.add_arc('walkway-upper', (8, 34), (6, 36), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('walkway-side', (6, 36), (6, 40))
        self.add_arc('walkway-lower', (6, 40), (8, 42), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('walkway-bottom', (8, 42), (42, 42))
        self.add_contour('head-14', 'head-14-top', 'head-14-bottom', closed=True)
        self.add_contour('person-14', 'shoulder-left-14', 'shoulders-14', 'shoulder-right-14', closed=False)
        self.add_contour('head-35', 'head-35-top', 'head-35-bottom', closed=True)
        self.add_contour('person-35', 'shoulder-left-35', 'shoulders-35', 'shoulder-right-35', closed=False)
        self.add_contour('walkway', 'walkway-top-joint-1', 'walkway-top-joint-2', 'walkway-top-joint-3', 'walkway-top-joint-4', 'walkway-upper', 'walkway-side', 'walkway-lower', 'walkway-bottom', closed=False)
        self.relate('connect', 'person-14', 'walkway')
        self.relate('connect', 'person-35', 'walkway')
