from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dfec1c77-8ff8-47df-9c1f-74790132a8ba'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/vectors anchor circle_dfec1c77-8ff8-47df-9c1f-74790132a8ba.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'circular-vector-path-with-four-nodes'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    categories = ("design", "primitives")
    aliases = ()
    keywords = ('vector', 'path', 'circle', 'nodes', 'anchors', 'editing', 'handles', 'curve')

    def build(self):
        # Plan: four identical round nodes on a circular vector path; ring stops at node boundaries.
        # Centerline extremes: radial radius 20 at (24,24). Construction: Lucide vector-square: path interrupted by complete editing nodes.
        def path(name,*points,closed=False):
            self.add_polyline(name,*points,closed=closed)
        def circle(name,x,y,r):
            self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def join(a,b):
            self.relate('connect',a,b)

        for name,x,y in (('top',24,8),('right',40,24),('bottom',24,40),('left',8,24)):circle('node-'+name,x,y,4)
        arcs=(('top-left',(20,8),(14,8),(8,14),(8,20),'top','left'),('bottom-left',(8,28),(8,34),(14,40),(20,40),'left','bottom'),('bottom-right',(28,40),(34,40),(40,34),(40,28),'bottom','right'),('top-right',(40,20),(40,14),(34,8),(28,8),'right','top'))
        for name,a,c1,c2,z,n1,n2 in arcs:
            self.add_bezier(name,a,(c1,c2,z))
            join(name,'node-'+n1);join(name,'node-'+n2)
