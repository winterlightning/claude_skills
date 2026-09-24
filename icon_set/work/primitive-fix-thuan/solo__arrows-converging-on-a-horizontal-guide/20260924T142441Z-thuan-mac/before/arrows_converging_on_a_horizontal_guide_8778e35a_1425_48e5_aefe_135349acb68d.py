'A downward arrow above and an upward arrow below point toward the same horizontal guide. Their vertical shafts share a centerline, creating a balanced top-and-bottom arrangement.\nPlan: Two opposed arrows on a shared vertical axis with separate horizontal guide.\nConstruction reference: Lucide arrow-up original and atomic-debug: symmetric shared arrowhead/shaft junctions.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8778e35a-1425-48e5-aefe-135349acb68d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/align text middle_8778e35a-1425-48e5-aefe-135349acb68d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arrows-converging-on-a-horizontal-guide'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('arrows', 'converging', 'on', 'a', 'horizontal', 'guide')

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

        line('guide',(6,24),(42,24));line('top',(24,6),(24,16));poly('down',(16,8),(24,16),(32,8));join('top','down')
        line('bottom',(24,32),(24,42));poly('up',(16,40),(24,32),(32,40));join('bottom','up')
