"""Clipped memory card with attached notched ribbon and lower strip. Contact marks omitted to keep lower strip readable. Centerline6,6–42,42.
Lucide construction reference: bookmark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='5995040d-c60a-445f-aba5-86c33132c6d0'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/data tag_5995040d-c60a-445f-aba5-86c33132c6d0.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/data tag_5995040d-c60a-445f-aba5-86c33132c6d0.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-018/references/data tag_5995040d-c60a-445f-aba5-86c33132c6d0.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='storage-card-with-attached-bookmark-solo-b018'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('storage', 'card', 'with', 'attached', 'bookmark')
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

        path('card',(10,6),[('L',(16,6)),('L',(28,6)),('L',(34,6)),('L',(42,14)),('L',(42,32)),('L',(42,38)),('A',4,4,True,(38,42)),('L',(10,42)),('A',4,4,True,(6,38)),('L',(6,32)),('L',(6,10)),('A',4,4,True,(10,6))],True)
        self.add_polyline('bookmark',(16,6),(16,22),(22,18),(28,22),(28,6));self.relate('connect','bookmark','card')
        self.add_line('strip',(6,32),(42,32));self.relate('connect','strip','card')
