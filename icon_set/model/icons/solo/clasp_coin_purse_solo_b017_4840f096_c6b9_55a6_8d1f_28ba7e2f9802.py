"""Bulbous clasp coin purse with broad base, arched mouth and two clasp stems. Double rim and tiny clasp knobs reduced to two rounded diagonal strokes. Centerline6,6–42,42.
Lucide construction reference: No useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='4840f096-c6b9-55a6-8d1f-28ba7e2f9802'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/money/coin purse_4840f096-c6b9-55a6-8d1f-28ba7e2f9802.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/money/coin purse_4840f096-c6b9-55a6-8d1f-28ba7e2f9802.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/coin purse_4840f096-c6b9-55a6-8d1f-28ba7e2f9802.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='clasp-coin-purse-solo-b017'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "money"
    categories = ("primitives", "money")
    aliases=()
    keywords=('clasp', 'coin', 'purse')
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

        path('purse',(14,16),[('L',(24,16)),('L',(34,16)),('B',(36,20),(42,26),(42,33)),('A',9,9,True,(33,42)),('L',(15,42)),('A',9,9,True,(6,33)),('B',(6,26),(12,20),(14,16))],True)
        self.add_polyline('clasp',(17,6),(24,16),(31,6));self.relate('connect','clasp','purse')
