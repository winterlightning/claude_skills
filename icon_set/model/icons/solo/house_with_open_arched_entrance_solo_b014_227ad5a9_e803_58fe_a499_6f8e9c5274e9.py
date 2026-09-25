"""Mirrored house with open arched entry and rounded lower wall corners. Roof and facade reuse eave nodes; no sill across the entrance. Ink box (4,4)-(44,44).
Lucide construction reference: house.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '227ad5a9-e803-58fe-a499-6f8e9c5274e9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/house_227ad5a9-e803-58fe-a499-6f8e9c5274e9.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house_227ad5a9-e803-58fe-a499-6f8e9c5274e9.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-014/references/house_227ad5a9-e803-58fe-a499-6f8e9c5274e9.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'house-with-open-arched-entrance-solo-b014'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('house', 'with', 'open', 'arched', 'entrance')
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

        self.add_polyline('roof',(6,24),(10,20),(24,6),(38,20),(42,24))
        path('facade',(10,20),[('L',(10,40)),('A',2,2,False,(12,42)),('L',(18,42)),('L',(18,30)),('A',6,6,True,(30,30)),('L',(30,42)),('L',(36,42)),('A',2,2,False,(38,40)),('L',(38,20))])
        self.relate('connect','roof','facade')
