"""Rejected pie became a plain half-disc and lost the connected rising zigzag. Restore an open circular pie with a radial sector and a continuous growth arrow.
Symbol plan: Lucide chart-pie original and atomic geometry: radial sector, circular outline; original connected growth line.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f82a9a59-0712-48ad-b67b-ef47e7c946ad'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pie-chart-growth-content/20260929T112503Z-thuan-mac/reference/pie line graph_f82a9a59-0712-48ad-b67b-ef47e7c946ad.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'pie-chart-growth-content'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('pie', 'chart', 'growth', 'content')

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

        path('chart',(32,16),[('C',(20,8),(30,10),(26,8)),('A',(4,24),16,16,False),('A',(20,40),16,16,False),('L',(28,32)),('L',(34,36)),('L',(44,20))])
        poly('sector',(20,8),(20,24),(32,16));join('sector','chart')
        poly('arrow',(36,20),(44,20),(44,28));join('arrow','chart')
