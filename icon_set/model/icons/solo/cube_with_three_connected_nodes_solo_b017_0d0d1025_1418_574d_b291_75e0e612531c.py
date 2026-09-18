"""Isometric cube with three round terminal nodes attached above and at lower corners. Centerline6,6–42,42.
Lucide construction reference: box; network.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0d0d1025-1418-574d-b291-75e0e612531c'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/rotate d_0d0d1025-1418-574d-b291-75e0e612531c.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/rotate d_0d0d1025-1418-574d-b291-75e0e612531c.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/rotate d_0d0d1025-1418-574d-b291-75e0e612531c.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='cube-with-three-connected-nodes-solo-b017'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/everyday"
    aliases=()
    keywords=('cube', 'with', 'three', 'connected', 'nodes')
    def build(self):

        def circle(n,x,y,r):
            pts=((x-r,y),(x,y-r),(x+r,y),(x,y+r));members=[]
            for i in range(4):
                m=n+str(i);self.add_arc(m,pts[i],pts[(i+1)%4],radius_x=r);members.append(m)
            self.add_contour(n,*members,closed=True)
        def path(n,start,commands,closed=False):
            p=start;members=[]
            for i,c in enumerate(commands):
                m=n+str(i);q=c[-1]
                if c[0]=='L':self.add_line(m,p,q)
                elif c[0]=='A':self.add_arc(m,p,q,radius_x=c[1],radius_y=c[2],sweep=c[3])
                elif c[0]=='B':self.add_bezier(m,p,(c[1],c[2],q))
                members.append(m);p=q
            self.add_contour(n,*members,closed=closed)

        self.add_polyline('cube',(14,20),(24,14),(34,20),(34,30),(24,36),(14,30),closed=True)
        self.add_polyline('faces',(14,20),(24,26),(34,20));self.add_line('edge',(24,26),(24,36))
        for n in ('faces','edge'):self.relate('connect','cube',n)
        self.relate('connect','faces','edge')
        for n,x,y,r,a,b in [('top',24,9,3,(24,12),(24,14)),('left',8,40,2,(10,40),(14,30)),('right',40,40,2,(38,40),(34,30))]:
         circle(n,x,y,r);self.add_line('link'+n,a,b);self.relate('connect',n,'link'+n);self.relate('connect','cube','link'+n)
