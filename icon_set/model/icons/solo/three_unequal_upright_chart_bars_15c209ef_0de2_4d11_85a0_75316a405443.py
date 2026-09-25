'Three separate rectangular bars share a lower baseline and rise to different heights. The center bar is tallest, the right bar is intermediate, and the left bar is shortest.\nPlan: Three bars with distinct heights, shared visual baseline and8-unit horizontal gaps.\nConstruction reference: Lucide chart-no-axes-column original and atomic-debug: three ordered bar heights.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '15c209ef-0de2-4d11-85a0-75316a405443'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/logo logo_15c209ef-0de2-4d11-85a0-75316a405443.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-unequal-upright-chart-bars'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('three', 'unequal', 'upright', 'chart', 'bars')

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

        for name,x,top in [('left',4,24),('middle',20,8),('right',36,16)]:poly(name,(x,40),(x,top),(x+8,top),(x+8,40),(x,40))
