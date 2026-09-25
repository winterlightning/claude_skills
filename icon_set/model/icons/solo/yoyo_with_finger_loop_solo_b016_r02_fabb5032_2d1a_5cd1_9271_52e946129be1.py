"""Yoyo disk with concentric face ring and upper-right finger loop. Curved string shares cardinal endpoints. Centerline6,6–42,42.
Construction reference: No useful exact Lucide match; supplied reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='fabb5032-2d1a-5cd1-9271-52e946129be1'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/yoyo_fabb5032-2d1a-5cd1-9271-52e946129be1.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/yoyo_fabb5032-2d1a-5cd1-9271-52e946129be1.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/yoyo_fabb5032-2d1a-5cd1-9271-52e946129be1.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='yoyo-with-finger-loop-solo-b016-r02'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "kids"
    aliases=()
    keywords=('yoyo', 'with', 'finger', 'loop')
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

        circle('disk',18,30,12);circle('hub',18,30,3);circle('loop',37,11,5)
        path('string',(30,30),[('B',(38,31),(41,22),(37,16))]);self.relate('connect','disk','string');self.relate('connect','loop','string')
