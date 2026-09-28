'A broad outlined arrow points upward from a long vertical shaft. Two diagonal arms form its head, with rounded outer tips and a smoothly curved upper point.\nPlan: Broad outlined upward arrow with rounded joins and full shaft.\nConstruction reference: Lucide arrow-up original and atomic-debug: symmetry and common apex; source outlined shaft retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '93ee4635-bd23-4a56-af66-aa96bc94feb9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/caret up_93ee4635-bd23-4a56-af66-aa96bc94feb9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arrow-up-rounded-outline'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('arrow', 'up', 'rounded', 'outline')

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

        poly('arrow',(6,22),(24,6),(42,22),(34,28),(28,22),(28,42),(20,42),(20,22),(14,28),(6,22))
