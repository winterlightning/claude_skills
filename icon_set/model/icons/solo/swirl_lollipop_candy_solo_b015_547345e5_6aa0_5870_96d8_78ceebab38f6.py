"""Lollipop spiral and diagonal stick. Head uses coherent circular arcs with inward curl; stick reduced to a single stroke to preserve clearance. Centerline8,4–40,44.
Lucide construction reference: No useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='547345e5-6aa0-5870-96d8-78ceebab38f6'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/baby family lolipop_547345e5-6aa0-5870-96d8-78ceebab38f6.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/baby family lolipop_547345e5-6aa0-5870-96d8-78ceebab38f6.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-015/references/baby family lolipop_547345e5-6aa0-5870-96d8-78ceebab38f6.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='swirl-lollipop-candy-solo-b015'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/controls"
    aliases=()
    keywords=('swirl', 'lollipop', 'candy')
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

        circle('head',26,18,14)
        self.add_arc('curl',(21,18),(31,18),radius_x=5,sweep=True)
        self.add_line('stick',(8,44),(26,32));self.relate('connect','head','stick')
