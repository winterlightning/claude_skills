'A winners podium consists of three adjoining rectangular platforms. The central block rises highest, the right block is intermediate, and the left block is lowest, all meeting on a common baseline.\nPlan: Three adjoining podium platforms with center highest, right intermediate, left lowest. Shared baseline nodes and partition edges.\nConstruction reference: No useful exact Lucide match; source-specific construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c8e9f19-5d7e-4cc6-a3c7-9648b020f8c3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/podium_0c8e9f19-5d7e-4cc6-a3c7-9648b020f8c3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-level-winners-podium'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('three', 'level', 'winners', 'podium')

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

        poly('outline',(4,38),(4,26),(17,26),(17,10),(31,10),(31,22),(44,22),(44,38),(31,38),(17,38),(4,38))
        line('left-wall',(17,26),(17,38));line('right-wall',(31,22),(31,38));join('outline','left-wall');join('outline','right-wall')
