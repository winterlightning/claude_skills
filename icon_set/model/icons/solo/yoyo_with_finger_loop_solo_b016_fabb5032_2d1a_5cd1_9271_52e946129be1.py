"""Yoyo with concentric face and curved string to upper-right finger loop. Head ring and loop circular; intentional asymmetric string. Centerline6,6–42,42.
Lucide construction reference: No useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='fabb5032-2d1a-5cd1-9271-52e946129be1'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/yoyo_fabb5032-2d1a-5cd1-9271-52e946129be1.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/yoyo_fabb5032-2d1a-5cd1-9271-52e946129be1.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/yoyo_fabb5032-2d1a-5cd1-9271-52e946129be1.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='yoyo-with-finger-loop-solo-b016'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/toys"
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

        circle('yoyo',19,29,13);circle('hub',19,29,4);circle('loop',38,10,4)
        path('string',(32,29),[('B',(38,29),(42,23),(38,14))]);self.relate('connect','string','yoyo');self.relate('connect','string','loop')
