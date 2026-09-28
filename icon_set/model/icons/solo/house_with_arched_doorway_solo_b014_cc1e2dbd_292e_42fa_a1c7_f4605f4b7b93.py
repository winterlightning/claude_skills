"""Broad house front with overhanging roof, straight ground and central arch. Mirrored x24 and exact facade/roof/sill attachments. Ink box (2,6)-(46,42).
Lucide construction reference: house.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cc1e2dbd-292e-42fa-a1c7-f4605f4b7b93'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/house_cc1e2dbd-292e-42fa-a1c7-f4605f4b7b93.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house_cc1e2dbd-292e-42fa-a1c7-f4605f4b7b93.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-014/references/house_cc1e2dbd-292e-42fa-a1c7-f4605f4b7b93.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'house-with-arched-doorway-solo-b014'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "other", "primitives-generate")
    aliases = ()
    keywords = ('house', 'with', 'arched', 'doorway')
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

        self.add_polyline('roof',(4,23),(8,20),(24,8),(40,20),(44,23))
        self.add_polyline('facade',(8,20),(8,40),(18,40),(30,40),(40,40),(40,20))
        self.relate('connect','roof','facade')
        path('door',(18,40),[('L',(18,31)),('A',6,6,True,(30,31)),('L',(30,40))])
        self.relate('connect','door','facade')
