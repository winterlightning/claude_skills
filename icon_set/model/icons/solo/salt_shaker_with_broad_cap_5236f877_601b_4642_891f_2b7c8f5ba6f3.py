'A plain salt shaker has a tapered body that widens toward a rounded base. A broad rounded cap rests above its narrow shoulders, with a thin seam between the lid and body.\nPlan: Rounded broad cap with tapered shaker body.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5236f877-601b-4642-891f-2b7c8f5ba6f3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/salt_5236f877-601b-4642-891f-2b7c8f5ba6f3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'salt-shaker-with-broad-cap'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('salt', 'shaker', 'with', 'broad', 'cap')

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

        path('cap',(16,4),[('L',(32,4)),('A',(36,8),4,4,True),('L',(36,14)),('L',(12,14)),('L',(12,8)),('A',(16,4),4,4,True)],True)
        path('body',(12,14),[('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(36,14))]);join('cap','body')
