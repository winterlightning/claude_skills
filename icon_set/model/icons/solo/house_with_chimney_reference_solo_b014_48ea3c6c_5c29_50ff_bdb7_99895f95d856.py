"""Symmetric house and open arch, with a deliberately detached upper-right chimney matching the source. Mirror the facade, keep the chimney asymmetric. Ink box (4,4)-(44,44).
Lucide construction reference: house.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '48ea3c6c-5c29-50ff-bdb7-99895f95d856'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/house chimney_48ea3c6c-5c29-50ff-bdb7-99895f95d856.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house chimney_48ea3c6c-5c29-50ff-bdb7-99895f95d856.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-014/references/house chimney_48ea3c6c-5c29-50ff-bdb7-99895f95d856.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'house-with-chimney-reference-solo-b014'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface/controls"
    aliases = ()
    keywords = ('house', 'with', 'chimney', 'reference')
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

        self.add_polyline('roof',(6,28),(10,24),(24,10),(38,24),(42,28))
        path('facade',(10,24),[('L',(10,40)),('A',2,2,False,(12,42)),('L',(18,42)),('L',(18,32)),('A',6,6,True,(30,32)),('L',(30,42)),('L',(36,42)),('A',2,2,False,(38,40)),('L',(38,24))])
        self.relate('connect','roof','facade')
        self.add_polyline('chimney',(32,6),(40,6),(40,14))
