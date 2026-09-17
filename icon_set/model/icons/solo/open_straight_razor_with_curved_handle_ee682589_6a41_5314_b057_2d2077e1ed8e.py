from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ee682589-6a41-5314-b057-2d2077e1ed8e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/razor_ee682589-6a41-5314-b057-2d2077e1ed8e.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'open-straight-razor-with-curved-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('razor', 'shaving', 'blade', 'handle', 'folding', 'grooming', 'barber', 'tool')

    def build(self):
        # Plan: open blade and curved handle meet at a common pivot; intentionally diagonal.
        # Centerline envelope: (4,8)-(44,40). Reference: No close Lucide razor; coherent blade contour and sweeping handle.
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
        def join(a,b):
            self.relate('connect', a,b)

        path('blade',(8,8),(36,24),(30,30),(4,16),closed=True)
        self.add_bezier('handle',(36,24),((30,36),(16,40),(6,40)))
        join('blade','handle')
        self.add_line('tang',(36,24),(44,18));join('blade','tang');join('handle','tang')
