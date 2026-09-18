"""Horizontal capsule containing two equal vertical marks toward left. No invented toggle knob. Centerline4,10–44,38.
Lucide construction reference: toggle-left.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='5aacf220-3104-5628-83e3-8dddf6e85cbc'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/settings off_5aacf220-3104-5628-83e3-8dddf6e85cbc.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/settings off_5aacf220-3104-5628-83e3-8dddf6e85cbc.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-015/references/settings off_5aacf220-3104-5628-83e3-8dddf6e85cbc.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='capsule-switch-with-two-strokes-solo-b015'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/controls"
    aliases=()
    keywords=('capsule', 'switch', 'with', 'two', 'strokes')
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

        path('capsule',(18,10),[('L',(30,10)),('A',14,14,True,(30,38)),('L',(18,38)),('A',14,14,True,(18,10))],True)
        for x in (16,24):self.add_line('mark'+str(x),(x,20),(x,28))
