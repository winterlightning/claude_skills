"""The rejected unicorn had a sideways spike, square back and fused rectangular legs. Restore a single upright horn, a curved back and rounded stepped hooves; distant legs omitted for clearance.
Symbol plan: Original horse silhouette; smooth circular haunch and stepped hooves, no useful exact Lucide match.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a775341a-0e75-4ee2-9369-e05213871fd6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__walking-unicorn/20260929T122443Z-thuan-mac/reference/fantasy unicorn 1_a775341a-0e75-4ee2-9369-e05213871fd6.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'walking-unicorn'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('walking', 'unicorn')

    def build(self):

        def path(n,start,steps,closed=False):
            point=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L': self.add_line(m,point,end)
                elif kind=='A': self.add_arc(m,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,point,(args[0],args[1],end))
                point=end; members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        path('horse',(4,20),[('L',(14,16)),('C',(24,23),(18,16),(20,23)),('L',(34,23)),('A',(40,29),6,6,True),('L',(40,36)),('A',(36,40),4,4,True),('L',(32,40)),('L',(32,32)),('L',(22,32)),('L',(20,40)),('L',(10,40)),('L',(14,29)),('L',(17,25)),('L',(4,27)),('L',(4,20))],True)
        line('horn',(14,16),(12,8));join('horn','horse')
        path('tail',(40,29),[('C',(44,37),(44,29),(44,33))]);join('tail','horse')
