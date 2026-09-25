from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4b657b7-882a-591a-a004-d3b56ac8a9fa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/right distance_b4b657b7-882a-591a-a004-d3b56ac8a9fa.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'square-with-right-alignment-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    aliases = ()
    keywords = ('alignment', 'square', 'arrow', 'right', 'boundary', 'spacing', 'layout', 'diagram')

    def build(self):
        # Plan: alignment diagram: square and attached right arrow, separate full-height boundary.
        # Centerline extremes: (6,6)-(42,42). Construction: Source diagram interpreted as one attached spatial relationship.
        def path(name,*points,closed=False):
            self.add_polyline(name,*points,closed=closed)
        def circle(name,x,y,r):
            self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def join(a,b):
            self.relate('connect',a,b)

        path('square',(6,16),(18,16),(18,24),(18,32),(6,32),closed=True)
        self.add_line('shaft',(18,24),(34,24));join('shaft','square')
        path('arrowhead',(28,18),(34,24),(28,30));join('shaft','arrowhead')
        self.add_line('boundary',(42,6),(42,42))
