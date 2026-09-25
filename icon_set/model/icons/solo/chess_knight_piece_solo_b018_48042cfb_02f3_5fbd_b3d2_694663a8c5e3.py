"""Left-facing chess knight with curved neck, muzzle, upright ear and pedestal. No tiny eye or mane detail. Centerline8,4–40,44.
Lucide construction reference: chess-knight.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='48042cfb-02f3-5fbd-b3d2-694663a8c5e3'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/strategy chess_48042cfb-02f3-5fbd-b3d2-694663a8c5e3.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/strategy chess_48042cfb-02f3-5fbd-b3d2-694663a8c5e3.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-018/references/strategy chess_48042cfb-02f3-5fbd-b3d2-694663a8c5e3.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='chess-knight-piece-solo-b018'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('chess', 'knight', 'piece')
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

        path('horse',(16,34),[('B',(16,26),(25,25),(25,18)),('L',(15,21)),('L',(8,18)),('L',(8,14)),('L',(20,6)),('L',(20,4)),('B',(35,8),(36,21),(34,34))])
        path('base',(12,34),[('L',(16,34)),('L',(34,34)),('L',(36,34)),('A',4,4,True,(40,38)),('L',(40,44)),('L',(8,44)),('L',(8,38)),('A',4,4,True,(12,34))],True)
        self.relate('connect','horse','base')
