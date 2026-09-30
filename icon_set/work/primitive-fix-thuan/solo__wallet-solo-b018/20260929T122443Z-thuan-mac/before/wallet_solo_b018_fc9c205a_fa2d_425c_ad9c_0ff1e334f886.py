"""Upright wallet with top pocket seam and rounded fastening tab from right. Snap dot omitted inside small tab. Centerline8,4–40,44.
Lucide construction reference: wallet.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='fc9c205a-fa2d-425c-ad9c-0ff1e334f886'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/wallet_fc9c205a-fa2d-425c-ad9c-0ff1e334f886.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/wallet_fc9c205a-fa2d-425c-ad9c-0ff1e334f886.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-018/references/wallet_fc9c205a-fa2d-425c-ad9c-0ff1e334f886.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='wallet-solo-b018'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases=()
    keywords=('wallet',)
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

        path('wallet',(13,4),[('L',(35,4)),('A',5,5,True,(40,9)),('L',(40,24)),('L',(40,34)),('L',(40,39)),('A',5,5,True,(35,44)),('L',(13,44)),('A',5,5,True,(8,39)),('L',(8,14)),('L',(8,9)),('A',5,5,True,(13,4))],True)
        self.add_line('pocket',(8,14),(30,14));self.relate('connect','wallet','pocket')
        path('tab',(40,24),[('L',(29,24)),('A',5,5,False,(29,34)),('L',(40,34))]);self.relate('connect','wallet','tab')
