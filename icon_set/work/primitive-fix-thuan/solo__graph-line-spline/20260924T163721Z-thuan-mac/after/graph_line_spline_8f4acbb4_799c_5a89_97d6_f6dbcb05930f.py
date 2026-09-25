'Two smooth data curves above a straight horizontal axis and beside a straight vertical axis.\nPlan: HRECT_L exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: chart-spline: coherent rising and falling cubic sections with horizontal tangents at extrema.\nOmissions: No series omitted; shallow troughs preserve spacing.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8f4acbb4-799c-5a89-97d6-f6dbcb05930f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__graph-line-spline/20260924T163721Z-thuan-mac/reference/graph line spline_8f4acbb4-799c-5a89-97d6-f6dbcb05930f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='graph-line-spline'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('graph', 'line', 'spline')
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

        poly('axes',(4,8),(4,40),(44,40))
        path('upper',(13,17),[('C',(22,8),(16,17),(16,8)),('C',(34,14),(28,8),(28,14)),('C',(44,8),(40,14),(42,12))])
        path('lower',(13,31),[('C',(22,26),(17,28),(18,26)),('C',(34,28),(28,26),(28,28)),('C',(44,21),(40,28),(42,25))])
