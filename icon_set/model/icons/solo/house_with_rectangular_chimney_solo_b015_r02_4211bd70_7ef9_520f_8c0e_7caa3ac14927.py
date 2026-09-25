"""Chimney house with softened lower walls and doorway corners. Detached chimney keeps the right slope readable at48. Centerline6,6–42,42.
Construction reference: house.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='4211bd70-7ef9-520f-8c0e-7caa3ac14927'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/house chimney_4211bd70-7ef9-520f-8c0e-7caa3ac14927.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house chimney_4211bd70-7ef9-520f-8c0e-7caa3ac14927.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-015/references/house chimney_4211bd70-7ef9-520f-8c0e-7caa3ac14927.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='house-with-rectangular-chimney-solo-b015-r02'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "interface-essential"
    aliases=()
    keywords=('house', 'with', 'rectangular', 'chimney')
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

        self.add_polyline('roof',(6,29),(10,25),(24,11),(38,25),(42,29))
        path('walls',(10,25),[('L',(10,39)),('A',3,3,False,(13,42)),('L',(18,42)),('L',(18,32)),('A',3,3,True,(21,29)),('L',(27,29)),('A',3,3,True,(30,32)),('L',(30,42)),('L',(35,42)),('A',3,3,False,(38,39)),('L',(38,25))])
        self.add_polyline('chimney',(33,6),(42,6),(42,15));self.relate('connect','roof','walls')
