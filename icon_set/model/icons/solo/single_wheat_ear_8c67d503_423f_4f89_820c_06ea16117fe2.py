"""Single Ear of Wheat."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c67d503-423f-4f89-820c-06ea16117fe2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/protein gluten wheat_8c67d503-423f-4f89-820c-06ea16117fe2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-wheat-ear'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('single', 'wheat', 'ear')

    def build(self):
        # Plan: Diagonal broad wheat ear retains a curved overlapping grain division and short stem. Lucide wheat informs the growth axis. Fewer, wider pointed lobes preserve clear gaps at 48 pixels.
        # Envelope: SQUARE; visible ink (4, 4, 44, 44) on SOLO48.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('ear',(12,38),[('C',(6,28),(8,36),(6,32)),('C',(12,16),(6,23),(8,20)),('L',(19,11)),('L',(24,6)),('L',(29,16)),('L',(42,6)),('L',(42,14)),('C',(42,28),(42,20),(42,24)),('L',(36,34)),('L',(28,42)),('L',(18,42)),('C',(12,38),(14,42),(12,40))],True)
        path('grain-edge',(19,11),[('C',(36,34),(16,24),(23,34))]);join('grain-edge','ear')
        line('stem',(6,42),(12,38));join('stem','ear')
