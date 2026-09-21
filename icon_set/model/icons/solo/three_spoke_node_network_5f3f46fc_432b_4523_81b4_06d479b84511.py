'Three circular nodes sit at the ends of a Y-shaped connector. One node is directly above the central junction, while the other two spread diagonally toward the lower left and lower right.\nPlan: Three circular nodes on a Y connector. All branches end at exact cardinal circle endpoints.\nConstruction reference: network: explicit shared junctions and repeated nodes; original circular nodes retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f3f46fc-432b-4523-81b4-06d479b84511'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/network wired_5f3f46fc-432b-4523-81b4-06d479b84511.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-spoke-node-network'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('three', 'spoke', 'node', 'network')

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

        circle('top',24,12,6);circle('left',12,36,6);circle('right',36,36,6)
        poly('branches',(12,30),(24,24),(36,30));line('trunk',(24,18),(24,24))
        join('branches','left');join('branches','right');join('branches','trunk');join('trunk','top')
