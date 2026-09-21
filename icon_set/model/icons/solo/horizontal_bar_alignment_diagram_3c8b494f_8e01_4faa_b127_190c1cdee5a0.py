'A wide rectangular bar sits above a separate long horizontal line. A short vertical stroke appears below their shared center, with generous gaps separating all three elements in the open diagram.\nPlan: Wide rectangular bar, long separate guide and short center tick.\nConstruction reference: Lucide align-vertical-justify-center original and atomic-debug: independent bars and center guide.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3c8b494f-8e01-4faa-b127-190c1cdee5a0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/objects align bottom_3c8b494f-8e01-4faa-b127-190c1cdee5a0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-bar-alignment-diagram'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('horizontal', 'bar', 'alignment', 'diagram')

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

        poly('bar',(4,8),(44,8),(44,16),(4,16),(4,8))
        line('guide',(4,28),(44,28));line('tick',(24,36),(24,40))
