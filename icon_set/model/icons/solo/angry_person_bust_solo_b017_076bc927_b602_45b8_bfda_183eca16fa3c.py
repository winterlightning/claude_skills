"""Angry frontal bust: circular head and broad shoulders follow human_ref/user.svg. Joined inward brows preserve anger; tiny mouth omitted for facial clearance. Head radius13 cy19 ends32; shoulder top40 gives exact4 ink gap. Centerline6,6–42,42.
Lucide construction reference: human_ref/user.svg.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='076bc927-b602-45b8-bfda-183eca16fa3c'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/angry person_076bc927-b602-45b8-bfda-183eca16fa3c.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/angry person_076bc927-b602-45b8-bfda-183eca16fa3c.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/angry person_076bc927-b602-45b8-bfda-183eca16fa3c.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='angry-person-bust-solo-b017'
    keyshape=Keyshape.VRECT_L
    human_construction="bust"
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases=()
    keywords=('angry', 'person', 'bust')
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

        circle('head',24,20,16)
        self.add_line('leftbrow',(18,16),(20,17))
        self.add_line('rightbrow',(28,17),(30,16))
        self.add_polyline('frown',(22,27),(24,26),(26,27))
        self.add_arc('shoulders',(8,44),(40,44),radius_x=34,sweep=True)
        self.relate('connect','head','shoulders')
