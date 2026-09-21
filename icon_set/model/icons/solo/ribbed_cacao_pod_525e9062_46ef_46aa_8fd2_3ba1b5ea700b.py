'A long cacao pod has pointed ends and broad curved sides. Two internal ribs bow outward from top to bottom, while a short curved stem rises above the upper tip.\nPlan: Pointed cacao pod with one central rib and curved short stem; symmetric pod.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '525e9062-46ef-46aa-8fd2-3ba1b5ea700b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/cacao_525e9062-46ef-46aa-8fd2-3ba1b5ea700b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ribbed-cacao-pod'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('ribbed', 'cacao', 'pod')

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

        path('pod',(24,12),[('C',(40,28),(32,16),(40,20)),('C',(24,44),(40,36),(32,40)),('C',(8,28),(16,40),(8,36)),('C',(24,12),(8,20),(16,16))],True)
        line('rib',(24,12),(24,44));join('rib','pod')
        path('stem',(24,12),[('A',(32,4),8,8,True)]);join('stem','pod')
