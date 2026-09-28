'A pickup beneath a row of three compact pine silhouettes, with a clear cab, bed and two wheels.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: truck and trees: straight vehicle structure and repeated tree definitions.\nOmissions: Tree branch tiers simplified to single triangular canopies.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6dfa119a-7ff9-4daf-b2d5-bc196f42deb1'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__pickup-beneath-three-pines/20260924T163721Z-thuan-mac/reference/car truck woods_6dfa119a-7ff9-4daf-b2d5-bc196f42deb1.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='pickup-beneath-three-pines'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('pickup', 'beneath', 'three', 'pines')
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

        for i,x in enumerate((12,24,36)):
         poly(f'pine-{i}',(x-6,14),(x,6),(x+6,14),(x-6,14))
         if i:join(f'pine-{i-1}',f'pine-{i}')
        poly('truck',(6,38),(6,30),(14,30),(18,22),(26,22),(26,30),(42,30),(42,38),(38,38))
        line('floor',(14,38),(30,38))
        for x in (10,34):
         path(f'wheel-{x}',(x+4,38),[('A',(x-4,38),4,4,True)])
        join('truck','wheel-10');join('truck','wheel-34');join('floor','wheel-10');join('floor','wheel-34')
