'A rounded square outer frame surrounds a smaller rectangular shelving opening. Two horizontal dividers cross the inner opening to create three stacked empty shelves, with a broad margin around the shelving unit.\nPlan: Three shelf openings in rounded outer frame; omit redundant inner frame margin.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30ab66d4-98e1-405f-9c76-67b42a0c39d9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/rack_30ab66d4-98e1-405f-9c76-67b42a0c39d9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'framed-three-shelf-rack'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('framed', 'three', 'shelf', 'rack')

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

        path('frame',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,18)),('L',(42,30)),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,30)),('L',(6,18)),('L',(6,10)),('A',(10,6),4,4,True)],True)
        for y in (18,30):
         line(f'shelf-{y}',(6,y),(42,y));join(f'shelf-{y}','frame')
