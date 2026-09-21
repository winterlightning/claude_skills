'Two rounded square outlines overlap diagonally, with the upper one shifted left. Short gaps interrupt several edges around the shared center, while the outer portions remain broad and clearly separated.\nPlan: Interrupted overlapping outlines retain asymmetric gaps and central elbow.\nConstruction reference: No useful direct Lucide match; rebuilt from inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be8dae84-5405-4802-81b7-35e3f6f8f7f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pathfinder outline_be8dae84-5405-4802-81b7-35e3f6f8f7f4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'interrupted-overlapping-square-outlines'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('interrupted', 'overlapping', 'square', 'outlines')

    # Repair: Widen the intentional interruption gaps while preserving the central elbow.
    # Repair: Give the final intentional top interruption9 units of centerline clearance.
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

        path('upper',(10,6),[('L',(26,6)),('A',(30,10),4,4,True),('L',(30,18)),('L',(22,18)),('A',(16,24),6,6,False),('L',(16,28)),('L',(10,28)),('A',(6,24),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        path('lower',(39,18),[('A',(42,21),3,3,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(22,42)),('A',(18,38),4,4,True)])
        poly('elbow',(27,30),(30,30),(30,27))
