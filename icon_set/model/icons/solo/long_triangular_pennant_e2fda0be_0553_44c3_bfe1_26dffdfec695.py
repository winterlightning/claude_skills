'A long triangular pennant extends right from a thin vertical pole. Its straight upper and lower edges meet at a sharp outer point, while the pole projects above and below the attached flag.\nPlan: Long triangular pennant attaches to upright pole at explicit endpoints.\nConstruction reference: Lucide flag-triangle-right original and atomic-debug: shared triangle/pole.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2fda0be-0553-44c3-bfe1-26dffdfec695'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pennant_e2fda0be-0553-44c3-bfe1-26dffdfec695.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-triangular-pennant'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('long', 'triangular', 'pennant')

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

        poly('pole',(4,8),(4,16),(4,32),(4,40))
        poly('flag',(4,16),(44,24),(4,32));join('flag','pole')
