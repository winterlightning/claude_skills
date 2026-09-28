'A horizontal toothbrush has a raised rectangular bristle block and a gently bent handle. A large curled dollop of toothpaste floats directly above the bristles, separated by a small gap.\nPlan: Paste teardrop above two broad bristle lines and bent brush spine. Box 4,8–44,40.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30a98a8e-4d69-4039-8e6c-32e3fbfdabff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/brush toothpaste 1_30a98a8e-4d69-4039-8e6c-32e3fbfdabff.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'toothbrush-beneath-curl-of-paste'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('toothbrush', 'beneath', 'curl', 'of', 'paste')

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

        path('paste',(20,8),[('C',(28,16),(16,16),(24,14)),('A',(28,24),4,4,True),('L',(12,24)),('C',(20,8),(2,24),(4,12))],True)
        poly('brush',(4,40),(28,40),(36,32),(44,32))
        line('bristle-left',(4,32),(4,40));line('bristle-right',(20,32),(20,40));join('brush','bristle-left');join('brush','bristle-right')
