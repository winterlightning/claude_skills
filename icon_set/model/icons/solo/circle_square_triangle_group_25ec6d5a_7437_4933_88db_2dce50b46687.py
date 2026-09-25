from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25ec6d5a-7437-4933-88db-2dce50b46687'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/shapes_25ec6d5a-7437-4933-88db-2dce50b46687.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'circle-square-triangle-group'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    aliases = ()
    keywords = ('shapes', 'circle', 'square', 'triangle', 'geometry', 'forms', 'group', 'design')

    def build(self):
        # Plan: three independent geometric shapes arranged as an open triangle.
        # Centerline extremes: (6,6)-(42,42). Construction: Lucide shapes: clear independent shape silhouettes.
        def path(name,*points,closed=False):
            self.add_polyline(name,*points,closed=closed)
        def circle(name,x,y,r):
            self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def join(a,b):
            self.relate('connect',a,b)

        circle('circle',33,15,9)
        path('square',(6,24),(18,24),(18,36),(6,36),closed=True)
        path('triangle',(33,32),(42,42),(24,42),closed=True)
