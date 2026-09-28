"""Two outward arrows mirror about x24; central divider is detached by 8 centerline units. Ink box (2,8)-(46,40).
Lucide construction reference: move-horizontal.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3cd9562a-4ab1-4edc-bc5f-dd0abab98a01'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/expand horizontal 2_3cd9562a-4ab1-4edc-bc5f-dd0abab98a01.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/expand horizontal 2_3cd9562a-4ab1-4edc-bc5f-dd0abab98a01.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-014/references/expand horizontal 2_3cd9562a-4ab1-4edc-bc5f-dd0abab98a01.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'outward-arrows-from-divider-solo-b014'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface/controls"
    aliases = ()
    keywords = ('outward', 'arrows', 'from', 'divider')
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
         tip=24+side*20;inner=24+side*8
         self.add_polyline('head'+str(side),(inner,10),(tip,24),(inner,38))
         self.add_line('shaft'+str(side),(tip,24),(inner,24))
         self.relate('connect','head'+str(side),'shaft'+str(side))
        self.add_line('divider',(24,10),(24,38))
