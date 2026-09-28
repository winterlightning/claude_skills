'A round yarn toy with an interior winding and two broad curved feather tips.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: shell: round toy construction; source-specific feather silhouettes.\nOmissions: Fine thread lines and motion marks omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='70726b69-9e7a-4233-b7d0-b7ed337efc12'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__yarn-ball-toy-feathers/20260924T163721Z-thuan-mac/reference/cat yarn toy_70726b69-9e7a-4233-b7d0-b7ed337efc12.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='yarn-ball-toy-feathers'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('yarn', 'ball', 'toy', 'feathers')
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

        circle('ball',18,30,12)
        line('winding',(6,30),(30,30));join('winding','ball')
        path('feathers',(18,18),[('C',(18,6),(24,14),(22,10)),('C',(30,20),(26,6),(34,12)),('C',(42,10),(36,20),(41,15)),('C',(30,30),(42,26),(38,30))]);join('feathers','ball')
