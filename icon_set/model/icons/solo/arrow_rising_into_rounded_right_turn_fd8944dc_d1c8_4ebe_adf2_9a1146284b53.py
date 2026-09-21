'A long vertical shaft rises from the lower left into a smooth rounded elbow. Its upper horizontal run extends right and ends in a small open arrowhead with two diagonal arms.\nPlan: Up shaft turns right through a quarter-circle elbow.\nConstruction reference: Lucide corner-up-right original and atomic-debug: tangent round elbow and shared arrowhead endpoint.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd8944dc-d1c8-4ebe-adf2-9a1146284b53'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/diagram fall rise steady_fd8944dc-d1c8-4ebe-adf2-9a1146284b53.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arrow-rising-into-rounded-right-turn'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('arrow', 'rising', 'into', 'rounded', 'right', 'turn')

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

        path('shaft',(6,42),[('L',(6,26)),('A',(18,14),12,12,True),('L',(42,14))])
        poly('head',(34,6),(42,14),(34,22));join('shaft','head')
