"""Two interrupted rectangular brackets surround a double-headed horizontal slide arrow. Short bracket legs leave the required clear space around arrowheads. Ink box (4,4)-(44,44).
Lucide construction reference: move-horizontal.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fd73adc7-e243-474f-95bc-cceb3254a620'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/slide tool_fd73adc7-e243-474f-95bc-cceb3254a620.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/slide tool_fd73adc7-e243-474f-95bc-cceb3254a620.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-014/references/slide tool_fd73adc7-e243-474f-95bc-cceb3254a620.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'horizontal-slide-tool-solo-b014'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('horizontal', 'slide', 'tool')
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

        self.add_polyline('upper',(16,10),(16,6),(32,6),(32,10))
        self.add_polyline('lower',(16,38),(16,42),(32,42),(32,38))
        self.add_line('shaft',(6,24),(42,24))
        for n,tip,inner in [('left',6,12),('right',42,36)]:
         self.add_polyline(n,(inner,18),(tip,24),(inner,30))
         self.relate('connect',n,'shaft')
