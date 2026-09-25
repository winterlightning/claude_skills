"""Circular aiming reticle with four inward cardinal ticks. Outer radius20 centered24,24; equal tick length5.
Lucide construction reference: crosshair.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='dd94a8ed-861b-4f0a-8d73-32bb290a71c9'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/circle clock_dd94a8ed-861b-4f0a-8d73-32bb290a71c9.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/circle clock_dd94a8ed-861b-4f0a-8d73-32bb290a71c9.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-018/references/circle clock_dd94a8ed-861b-4f0a-8d73-32bb290a71c9.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='four-tick-aiming-reticle-solo-b018'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('four', 'tick', 'aiming', 'reticle')
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

        circle('ring',24,24,20)
        for n,a,b in [('n',(24,4),(24,9)),('s',(24,44),(24,39)),('w',(4,24),(9,24)),('e',(44,24),(39,24))]:
         self.add_line(n,a,b);self.relate('connect','ring',n)
