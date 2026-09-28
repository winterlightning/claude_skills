"""Circular network extent with three internal nodes and triangular links. Nodes reduced to round junction marks to keep open triangular face. Radius20 about24,24.
Lucide construction reference: network.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='3b2a855e-6ab2-51bc-8612-b388126ed3ff'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/networks/cross region data delivery_3b2a855e-6ab2-51bc-8612-b388126ed3ff.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/networks/cross region data delivery_3b2a855e-6ab2-51bc-8612-b388126ed3ff.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/cross region data delivery_3b2a855e-6ab2-51bc-8612-b388126ed3ff.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='global-network-nodes-solo-b017'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "networks"
    categories = ("primitives", "networks")
    aliases=()
    keywords=('global', 'network', 'nodes')
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

        path('extent',(4,24),[('A',20,20,True,(24,4)),('A',20,20,True,(36,8)),('A',20,20,True,(44,24)),('A',20,20,True,(24,44)),('A',20,20,True,(4,24))],True)
        self.add_polyline('network',(13,22),(29,14),(34,34),closed=True)
        self.add_line('leftlink',(4,24),(13,22));self.relate('connect','leftlink','extent');self.relate('connect','leftlink','network')
        self.add_line('rightlink',(29,14),(36,8));self.relate('connect','rightlink','network');self.relate('connect','rightlink','extent')
