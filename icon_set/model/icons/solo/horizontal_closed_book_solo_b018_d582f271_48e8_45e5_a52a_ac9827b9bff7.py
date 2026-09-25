"""Complete horizontal closed book with rounded left spine and two long page lines. Restore right ends as an upright fore-edge. Centerline4,10–44,38.
Lucide construction reference: book.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d582f271-48e8-45e5-a52a-ac9827b9bff7'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/book close lines_d582f271-48e8-45e5-a52a-ac9827b9bff7.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/book close lines_d582f271-48e8-45e5-a52a-ac9827b9bff7.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-018/references/book close lines_d582f271-48e8-45e5-a52a-ac9827b9bff7.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='horizontal-closed-book-solo-b018'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('horizontal', 'closed', 'book')
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

        path('book',(10,10),[('L',(44,10)),('L',(44,19)),('L',(44,29)),('L',(44,38)),('L',(10,38)),('A',6,6,True,(4,32)),('L',(4,16)),('A',6,6,True,(10,10))],True)
        for y in (19,29):self.add_line('page'+str(y),(14,y),(44,y));self.relate('connect','book','page'+str(y))
