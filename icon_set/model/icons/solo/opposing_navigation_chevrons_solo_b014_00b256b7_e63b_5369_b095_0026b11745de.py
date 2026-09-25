"""Identical outward chevrons, mirrored around x24; retain the broad central opening. Ink box (2,8)-(46,40).
Lucide construction reference: chevrons-left-right.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '00b256b7-e63b-5369-b095-0026b11745de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/scroll horizontal_00b256b7-e63b-5369-b095-0026b11745de.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/scroll horizontal_00b256b7-e63b-5369-b095-0026b11745de.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-014/references/scroll horizontal_00b256b7-e63b-5369-b095-0026b11745de.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'opposing-navigation-chevrons-solo-b014'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('opposing', 'navigation', 'chevrons')
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

        for side in (-1,1):
         self.add_polyline('chevron'+str(side),(24+side*8,10),(24+side*20,24),(24+side*8,38))
