'Two blank rounded square cards are offset diagonally, with the front card sitting higher and to the left. The rear card remains visible along the right and bottom edges of the overlapping pair.\nPlan: Full front card and occluded rear card with shared T-junctions.\nConstruction reference: Lucide copy original and atomic-debug: occlusion and repeated round-corner boxes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd45616b6-1630-467a-b2b0-1324e090298c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/replica_d45616b6-1630-467a-b2b0-1324e090298c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-stacked-rounded-cards'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('two', 'stacked', 'rounded', 'cards')

    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)

        path('front',(10,6),[('L',(28,6)),('A',(32,10),4,4,True),('L',(32,16)),('L',(32,28)),('A',(28,32),4,4,True),('L',(16,32)),('L',(10,32)),('A',(6,28),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        path('rear',(32,16),[('L',(38,16)),('A',(42,20),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(20,42)),('A',(16,38),4,4,True),('L',(16,32))]);join('front','rear')
