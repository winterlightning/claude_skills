"""Horizontal outlined minus capsule: centerline extremes x4/44, y19/29. End circles of radius5 about x9/39 give exact radial20 envelope. Preserve the horizontal bar rather than inflate its height to a rectangular keyshape.
Lucide construction reference: minus.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '25da6d11-f877-4a82-af38-c6a15a4cbf59'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/subtract bold_25da6d11-f877-4a82-af38-c6a15a4cbf59.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/subtract bold_25da6d11-f877-4a82-af38-c6a15a4cbf59.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-014/references/subtract bold_25da6d11-f877-4a82-af38-c6a15a4cbf59.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'outlined-minus-bar-solo-b014'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('outlined', 'minus', 'bar')
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

        path('bar',(9,19),[('L',(39,19)),('A',5,5,True,(39,29)),('L',(9,29)),('A',5,5,True,(9,19))],True)
