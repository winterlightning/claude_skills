'Two rounded squares overlap diagonally, with one above and left of the other. Their continuous outlines cross through the shared central area, leaving the outer corners clearly visible on opposite sides.\nPlan: Two complete rounded squares with shared crossing nodes.\nConstruction reference: Lucide copy original and atomic-debug: matched corner radii.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42e59e00-4768-4843-87fb-93b40487dbc8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/object ungroup_42e59e00-4768-4843-87fb-93b40487dbc8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'offset-rounded-squares'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('offset', 'rounded', 'squares')

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

        path('upper',(10,6),[('L',(26,6)),('A',(30,10),4,4,True),('L',(30,18)),('L',(30,26)),('A',(26,30),4,4,True),('L',(18,30)),('L',(10,30)),('A',(6,26),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        path('lower',(22,18),[('L',(30,18)),('L',(38,18)),('A',(42,22),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(22,42)),('A',(18,38),4,4,True),('L',(18,30)),('L',(18,22)),('A',(22,18),4,4,True)],True);join('upper','lower')
