'Left-facing hen with small split crest, curved breast, lifted tail and two straight legs.\nPlan: HRECT_L exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: bird: continuous body silhouette with a pointed tail and simple feet.\nOmissions: Fine feather details and eye omitted; crest and two feet retained.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='5ee8a983-7ca0-48b0-a3c8-3fbe81bd8f23'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__left-facing-hen-with-split-crest/20260924T162030Z-thuan-mac/reference/chicken animal_5ee8a983-7ca0-48b0-a3c8-3fbe81bd8f23.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='left-facing-hen-with-split-crest'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('left', 'facing', 'hen', 'with', 'split', 'crest')
    def build(self):

        def path(name,start,commands,closed=False):
            point=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,point,end)
                elif kind=='A': self.add_arc(member,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,point,(args[0],args[1],end))
                point=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('hen',(8,16),[('L',(4,19)),('L',(8,22)),('L',(8,25)),('C',(18,32),(8,30),(12,32)),('L',(20,32)),('L',(32,32)),('C',(42,24),(38,32),(42,29)),('L',(44,13)),('L',(34,21)),('C',(23,22),(30,23),(26,24)),('C',(20,11),(20,20),(20,16)),('A',(14,11),3,3,False),('A',(8,11),3,3,False),('L',(8,16))],True)
        for x in (20,32):
         poly(f'leg-{x}',(x,32),(x-2,40),(x-4,40));join(f'leg-{x}','hen')
