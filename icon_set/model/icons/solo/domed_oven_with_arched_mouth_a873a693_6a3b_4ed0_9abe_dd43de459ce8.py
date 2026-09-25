'A broad domed oven rises from a low rectangular plinth, with straight lower sides beneath its rounded roof. A smaller arched opening sits centrally at the base of the dome.\nPlan: Domed oven and broad arched mouth share flat base; plinth simplified into base.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a873a693-6a3b-4ed0-9abe-dd43de459ce8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/apse_a873a693-6a3b-4ed0-9abe-dd43de459ce8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'domed-oven-with-arched-mouth'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('domed', 'oven', 'with', 'arched', 'mouth')

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

        path('oven',(6,42),[('L',(6,24)),('A',(42,24),18,18,True),('L',(42,42)),('L',(32,42)),('L',(16,42)),('L',(6,42))],True)
        path('mouth',(16,42),[('L',(16,34)),('A',(32,34),8,8,True),('L',(32,42))]);join('mouth','oven')
