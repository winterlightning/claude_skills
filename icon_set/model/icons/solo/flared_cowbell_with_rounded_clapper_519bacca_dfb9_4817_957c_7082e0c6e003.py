'A cowbell widens downward from a narrow rounded shoulder into a broad mouth. A short rounded loop projects above, and a rounded clapper hangs centrally beneath the lower edge.\nPlan: Flared bell with top loop and semicircular clapper; connected endpoints.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '519bacca-dfb9-4817-957c-7082e0c6e003'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/cowbell_519bacca-dfb9-4817-957c-7082e0c6e003.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'flared-cowbell-with-rounded-clapper'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('flared', 'cowbell', 'with', 'rounded', 'clapper')

    # Repair: Square loop and clapper openings to retain exact 8-unit interior height.
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

        path('bell',(18,12),[('L',(30,12)),('L',(40,36)),('L',(28,36)),('L',(20,36)),('L',(8,36)),('L',(18,12))],True)
        path('loop',(18,12),[('L',(18,4)),('L',(30,4)),('L',(30,12))]);join('loop','bell')
        path('clapper',(20,36),[('L',(20,44)),('L',(28,44)),('L',(28,36))]);join('clapper','bell')
