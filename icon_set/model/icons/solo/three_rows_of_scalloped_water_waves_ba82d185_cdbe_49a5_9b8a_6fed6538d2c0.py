'Three parallel rows of shallow scalloped waves stretch horizontally across the image. Each row repeats three rounded troughs with pointed crests between them, and the pattern remains separate from any shoreline.\nPlan: Three equal rows each repeat three scalloped troughs. Shared horizontal series and row spacing.\nConstruction reference: No useful exact Lucide match; source-specific construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba82d185-cdbe-49a5-9b8a-6fed6538d2c0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shallows_ba82d185-cdbe-49a5-9b8a-6fed6538d2c0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-rows-of-scalloped-water-waves'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'rows', 'of', 'scalloped', 'water', 'waves')

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

        for j,y in enumerate((10,22,34)):
         path(f'wave-{j}',(4,y),[('A',(17,y),7,4,False),('A',(31,y),7,4,False),('A',(44,y),7,4,False)])
