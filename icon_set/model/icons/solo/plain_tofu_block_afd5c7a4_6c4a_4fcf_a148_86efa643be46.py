'A plain block of tofu appears in perspective with a broad sloping top and two visible sides. Slightly rounded lower corners soften the otherwise cuboid silhouette.\nPlan: Plain tofu block in perspective; coherent cuboid outline with three shared interior edges. Preserve source asymmetric top face.\nConstruction reference: cuboid: shared three-face junction with no doubled edges.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'afd5c7a4-6c4a-4fcf-a148-86efa643be46'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/beancurd_afd5c7a4-6c4a-4fcf-a148-86efa643be46.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plain-tofu-block'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('plain', 'tofu', 'block')

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

        poly('outline',(4,18),(18,8),(44,14),(44,32),(30,40),(4,34),(4,18))
        poly('top-front',(4,18),(30,24),(44,14));line('front-edge',(30,24),(30,40));join('outline','top-front');join('outline','front-edge');join('top-front','front-edge')
