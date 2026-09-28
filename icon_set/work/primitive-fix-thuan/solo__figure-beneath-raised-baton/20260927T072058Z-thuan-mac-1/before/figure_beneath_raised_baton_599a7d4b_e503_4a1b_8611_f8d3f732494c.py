from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '599a7d4b-e503-4a1b-8611-f8d3f732494c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/protester_599a7d4b-e503-4a1b-8611-f8d3f732494c.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'figure-beneath-raised-baton'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases = ()
    keywords = ('person', 'baton', 'arm', 'protester', 'figure', 'gesture', 'scene', 'uncertain')

    def build(self):
        # Plan: defensive stick figure, detached head on upright torso axis, raised left arm; baton overhead.
        # Centerline envelope: (6,6)-(42,42). Reference: human_ref/full_body_ref.png: circular head, round limbs; baton reduced to bold stroke.
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
        def join(a,b):
            self.relate('connect', a,b)

        # human_ref/full_body_ref.png; head bottom 26, torso start 34: 4u ink gap.
        circle('head',30,21,5)
        self.add_line('torso',(30,34),(30,42))
        path('arm',(30,34),(16,34),(6,14))
        join('torso','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.add_line('baton',(18,6),(42,6))
