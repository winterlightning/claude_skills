'Two rounded squares overlap diagonally, with the lower left square in front. The upper right square remains visible above and beside it, while the overlapping portion is hidden.\nPlan: Full lower-left card with occluded upper-right card.\nConstruction reference: Lucide copy original and atomic-debug: retain complete foreground and partial rear silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3b40a17-37d6-4e74-8642-ab0a30414c30'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/board game dice 2_e3b40a17-37d6-4e74-8642-ab0a30414c30.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'offset-rounded-square-pair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('offset', 'rounded', 'square', 'pair')

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

        path('front',(10,16),[('L',(16,16)),('L',(28,16)),('A',(32,20),4,4,True),('L',(32,32)),('L',(32,38)),('A',(28,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,20)),('A',(10,16),4,4,True)],True)
        path('rear',(16,16),[('L',(16,10)),('A',(20,6),4,4,True),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,28)),('A',(38,32),4,4,True),('L',(32,32))]);join('front','rear')
