"""Left-facing piggy bank with squared snout, ear, feet and a coin above its deposit position. Coin denomination and curled tail omitted for clear silhouette. Centerline6,6–42,42.
Lucide construction reference: piggy-bank.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='35b2e33d-7f76-56bf-a387-22ca75647071'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/money/piggy_35b2e33d-7f76-56bf-a387-22ca75647071.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/money/piggy_35b2e33d-7f76-56bf-a387-22ca75647071.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/piggy_35b2e33d-7f76-56bf-a387-22ca75647071.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='piggy-bank-receiving-coin-solo-b017'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "money"
    aliases=()
    keywords=('piggy', 'bank', 'receiving', 'coin')
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

        path('pig',(14,22),[('L',(12,16)),('L',(21,20)),('B',(32,18),(42,23),(42,30)),('B',(42,35),(39,37),(38,38)),('L',(38,42)),('L',(30,42)),('L',(30,38)),('L',(22,38)),('L',(22,42)),('L',(14,42)),('L',(14,35)),('L',(6,33)),('L',(6,25)),('L',(12,25)),('L',(14,22))],True)
        circle('coin',27,8,2)
