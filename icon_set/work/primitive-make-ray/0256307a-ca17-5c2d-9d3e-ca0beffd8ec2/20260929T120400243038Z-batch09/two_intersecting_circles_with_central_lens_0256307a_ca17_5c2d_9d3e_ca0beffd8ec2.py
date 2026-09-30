"""Intersecting circles: rejected circles are tall ovals. Restore rounder overlapping circles and clear central lens. Rebuild equal rounder lobes and a wide central lens, meeting at two shared intersection nodes.
Symbol plan: Two matched circle-like contours. Round outer quarter arcs and smooth cubic intersection spans preserve horizontal Venn layout on the integer grid.
Keyshape HRECT_M: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0256307a-ca17-5c2d-9d3e-ca0beffd8ec2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-intersecting-circles-with-central-lens/20260929T115456Z-thuan-mac/reference/boolean or_0256307a-ca17-5c2d-9d3e-ca0beffd8ec2.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'two-intersecting-circles-with-central-lens'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('two', 'intersecting', 'circles', 'with', 'central', 'lens')

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

        for side in [-1,1]:
         p=lambda x,y:(24+side*x,y)
         path(f'outer-{side}',p(0,12),[('C',p(6,10),p(2,10),p(4,10)),('A',p(20,24),14,14,side>0),('A',p(6,38),14,14,side>0),('C',p(0,36),p(4,38),p(2,38))])
         path(f'inner-{side}',p(0,12),[('C',p(8,24),p(5,15),p(8,19)),('C',p(0,36),p(8,29),p(5,33))])
        for a,b in [('outer--1','outer-1'),('inner--1','inner-1'),('outer--1','inner--1'),('outer--1','inner-1'),('outer-1','inner--1'),('outer-1','inner-1')]:join(a,b)
