"A right pointing triangle sits at the open left side of a large circular arc. Its point projects toward the circle's interior, with clear gaps between the two outlines.\nPlan: Open circular arc with entering right-pointed triangle; intentional open gap.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6494d88a-d0fd-4a63-afbc-cb5428c5b917'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/blinklist logo_6494d88a-d0fd-4a63-afbc-cb5428c5b917.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'triangle-entering-open-circle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('triangle', 'entering', 'open', 'circle')

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

        path('circle',(16,12),[('C',(28,8),(20,8),(24,8)),('A',(44,24),16,16,True),('A',(28,40),16,16,True),('C',(16,36),(24,40),(20,40))])
        poly('triangle',(4,16),(16,24),(4,32),(4,16))
