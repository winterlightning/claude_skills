"""Isometric cube with three round terminal nodes attached above and at lower corners. Centerline6,6–42,42.
Lucide construction reference: box; network.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3be3c4f1-7eff-4665-918c-5125daa70608'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__isometric-cube-with-three-linked-hexagons/20260927T160114Z-thuan-mac-1/reference/scale 3d_3be3c4f1-7eff-4665-918c-5125daa70608.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/rotate d_0d0d1025-1418-574d-b291-75e0e612531c.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/rotate d_0d0d1025-1418-574d-b291-75e0e612531c.svg'
AUTHOR='gpt-6'
class IsometricCubeWithThreeLinkedHexagons(Solo48):
    icon_id='isometric-cube-with-three-linked-hexagons'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "design"
    categories = ("design", "primitives")
    aliases=()
    keywords=('isometric', 'cube', 'three', 'linked', 'hexagons')
    def build(self):

        def circle(n,x,y,r):
            # Two smooth half contours keep the six-sided terminal silhouette legible.
            self.add_bezier(n+'-upper',(x-r,y),
                ((x-r,y-2),(x-2,y-r),(x,y-r)),
                ((x+2,y-r),(x+r,y-2),(x+r,y)))
            self.add_bezier(n+'-lower',(x+r,y),
                ((x+r,y+2),(x+2,y+r),(x,y+r)),
                ((x-2,y+r),(x-r,y+2),(x-r,y)))
            self.add_contour(n,n+'-upper',n+'-lower',closed=True)
        def path(n,start,commands,closed=False):
            p=start;members=[]
            for i,c in enumerate(commands):
                m=n+str(i);q=c[-1]
                if c[0]=='L':self.add_line(m,p,q)
                elif c[0]=='A':self.add_arc(m,p,q,radius_x=c[1],radius_y=c[2],sweep=c[3])
                elif c[0]=='B':self.add_bezier(m,p,(c[1],c[2],q))
                members.append(m);p=q
            self.add_contour(n,*members,closed=closed)

        self.add_polyline('cube',(14,20),(24,14),(34,20),(32,30),(24,36),(16,30),closed=True)
        self.add_polyline('faces',(14,20),(24,25),(34,20));self.add_line('edge',(24,25),(24,36))
        for n in ('faces','edge'):self.relate('connect','cube',n)
        self.relate('connect','faces','edge')
        for n,x,y,r,a,b in [('top',24,9,3,(24,12),(24,14)),('left',9,39,3,(12,39),(16,30)),('right',39,39,3,(36,39),(32,30))]:
         circle(n,x,y,r);self.add_line('link'+n,a,b);self.relate('connect',n,'link'+n);self.relate('connect','cube','link'+n)
