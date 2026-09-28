'A curved path rises from a rounded square and bends toward a circular endpoint. A square node at its crest connects to a horizontal handle ending in another circle.\nPlan: Bezier curve with square crest node, square starting node and circular handles.\nConstruction reference: Lucide vector-square original and atomic-debug: explicit node endpoints and curved segment joins.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a842e565-c7cd-4f81-a804-368e82ebfcbb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bezier curve_a842e565-c7cd-4f81-a804-368e82ebfcbb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bezier-curve-with-control-handles'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bezier', 'curve', 'with', 'control', 'handles')

    # Repair: Bow the left curve away from its control handle; retain hollow6-unit round nodes and split the square nodes at actual joins.
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

        poly('start',(6,30),(12,30),(18,30),(18,42),(6,42),(6,30))
        poly('node',(22,6),(30,6),(30,10),(30,14),(22,14),(22,10),(22,6))
        circle('handle-left',9,10,3);circle('end',39,39,3)
        line('handle',(12,10),(22,10));join('handle','handle-left');join('handle','node')
        path('curve',(12,30),[('C',(22,10),(20,26),(22,18))]);join('curve','start');join('curve','node')
        path('curve-right',(30,10),[('C',(39,36),(39,10),(39,26))]);join('curve-right','node');join('curve-right','end')
