'A treasure chest has a rounded rectangular body and a domed upper section divided by two upright bands. A horizontal lid seam dips into a rounded central latch on the front.\nPlan: Domed lid, straight lower chest and central rounded latch in lid seam.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '855c5015-a00a-468a-b341-851605beee55'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/loot box treasure chest reward 1_855c5015-a00a-468a-b341-851605beee55.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'closed-treasure-chest-with-rounded-latch'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rewards'
    categories = ('rewards', 'primitive', 'primitives')
    aliases = ()
    keywords = ('closed', 'treasure', 'chest', 'with', 'rounded', 'latch')

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

        path('chest',(4,24),[('L',(4,16)),('A',(12,8),8,8,True),('L',(36,8)),('A',(44,16),8,8,True),('L',(44,24)),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,24))],True)
        path('seam',(4,24),[('L',(20,24)),('L',(20,28)),('A',(28,28),4,4,False),('L',(28,24)),('L',(44,24))]);join('seam','chest')
