'A tall tree with a lobed crown stands to the left of a simple park bench. The bench has a rectangular backrest above a narrow seat, with short supporting legs beneath it.\nPlan: Separate tree and park bench form natural scene; broad tree crown and simple seat.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b71c4ae-653e-46c7-bc4a-d22b626e2b7d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/park_7b71c4ae-653e-46c7-bc4a-d22b626e2b7d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'park-bench-beside-tree'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('park', 'bench', 'beside', 'tree')

    # Repair: Widen bench back to read as a bench instead of a chair; simplify tree to a round crown with certified diagonal clearance.
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

        circle('crown',14,14,8)
        line('trunk',(14,22),(14,42));join('trunk','crown')
        poly('bench',(26,26),(42,26),(42,34),(26,34),(26,26))
        line('leg1',(26,34),(26,42));line('leg2',(42,34),(42,42));join('bench','leg1');join('bench','leg2')
