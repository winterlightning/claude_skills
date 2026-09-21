'Three long upright arrows stand side by side with their open arrowheads aligned near the top. Their straight shafts extend downward independently, with equal spacing and no surrounding frame or baseline.\nPlan: Three equal upward arrows, shared 10-unit horizontal pitch.\nConstruction reference: arrow-right: open arrowhead construction re-authored upward.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3866e2d7-1784-4e90-8b61-948baafcadea'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/sliders up_3866e2d7-1784-4e90-8b61-948baafcadea.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-parallel-upward-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('three', 'parallel', 'upward', 'arrows')

    # Repair: Compact upward arrowheads allow three distinct shafts at 12-unit pitch.
    # Repair: Expanded horizontal pitch keeps all three upward arrowheads open.
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

        for j,x in enumerate((8,24,40)):
         poly(f'head-{j}',(x-4,14),(x,8),(x+4,14))
         line(f'shaft-{j}',(x,8),(x,40));join(f'head-{j}',f'shaft-{j}')
