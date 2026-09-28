'Symmetric chestnut with a pointed crown, smoothly rounded shell and a broad basal patch.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: nut and droplet: coherent curved silhouette; paired lobes share an axis.\nOmissions: Small inner patch highlight omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='82d65976-9908-4544-8c19-ca1cdea52290'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__whole-chestnut-with-basal-patch/20260924T163721Z-thuan-mac/reference/chestnut_82d65976-9908-4544-8c19-ca1cdea52290.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='whole-chestnut-with-basal-patch'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('whole', 'chestnut', 'with', 'basal', 'patch')
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

        path('shell',(24,6),[('C',(42,28),(28,14),(42,15)),('C',(40,34),(42,30),(41,32)),('C',(24,42),(36,42),(30,42)),('C',(8,34),(18,42),(12,42)),('C',(6,28),(7,32),(6,30)),('C',(24,6),(6,15),(20,14))],True)
        path('patch',(8,34),[('C',(40,34),(14,23),(34,23))]);join('patch','shell')
