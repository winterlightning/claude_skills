"""Feeding bottle with rounded wide body and shaped nipple. Neck seam is single horizontal division. Centerline10,4–38,44.
Lucide construction reference: milk.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='787783f6-901a-45ae-a710-84ce8a165876'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/drop bottle_787783f6-901a-45ae-a710-84ce8a165876.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/drop bottle_787783f6-901a-45ae-a710-84ce8a165876.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/drop bottle_787783f6-901a-45ae-a710-84ce8a165876.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='baby-feeding-bottle-solo-b017'
    keyshape=Keyshape.VRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('baby', 'feeding', 'bottle')
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

        path('bottle',(14,20),[('L',(14,16)),('B',(14,12),(20,12),(20,8)),('A',4,4,True,(28,8)),('B',(28,12),(34,12),(34,16)),('L',(34,20)),('A',4,4,True,(38,24)),('L',(38,38)),('A',6,6,True,(32,44)),('L',(16,44)),('A',6,6,True,(10,38)),('L',(10,24)),('A',4,4,True,(14,20))],True)
        self.add_line('neck',(14,20),(34,20));self.relate('connect','neck','bottle')
