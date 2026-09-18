"""Closed padlock: both shackle ends share body-top nodes; round body corners and keyhole plus short slot. Reduce the tiny pointed/round-ended stem to a single readable stroke. Ink box (6,2)-(42,46).
 Keyhole radius reduced to two and slot ends at y35, leaving nine units to the body edge.
Lucide construction reference: lock-keyhole.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'be7db261-3d14-5327-ba7f-e5380ebe04a8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/lock_be7db261-3d14-5327-ba7f-e5380ebe04a8.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/lock_be7db261-3d14-5327-ba7f-e5380ebe04a8.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-014/references/lock_be7db261-3d14-5327-ba7f-e5380ebe04a8.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'padlock-with-rounded-keyhole-solo-b014'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface/controls"
    aliases = ()
    keywords = ('padlock', 'with', 'rounded', 'keyhole')
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

        path('body',(8+4,20),[('L',(16,20)),('L',(32,20)),('L',(36,20)),('A',4,4,True,(40,24)),('L',(40,40)),('A',4,4,True,(36,44)),('L',(12,44)),('A',4,4,True,(8,40)),('L',(8,24)),('A',4,4,True,(12,20))],True)
        path('shackle',(16,20),[('L',(16,12)),('A',8,8,True,(32,12)),('L',(32,20))])
        self.relate('connect','body','shackle')
        circle('keyhole',24,32,2)
        self.add_line('slot',(24,34),(24,35))
        self.relate('connect','keyhole','slot')
