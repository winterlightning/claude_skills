"""The rejected watermelon was an upright bowl. Restore a diagonal slice with a thick curved rind; omit seeds to preserve clear flesh and rind at 48px.
Symbol plan: Original diagonal watermelon; symmetric quarter-turn slice and bowed rind, seeds omitted for legal separation.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8a129756-fbf5-4dcf-87f5-abd6e50e9d3f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__watermelon-wedge-rind/20260929T122443Z-thuan-mac/reference/melon_8a129756-fbf5-4dcf-87f5-abd6e50e9d3f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'watermelon-wedge-rind'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('watermelon', 'wedge', 'rind')

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

        path('wedge',(6,32),[('L',(32,6)),('C',(42,24),(39,10),(42,17)),('C',(24,42),(42,35),(35,42)),('C',(6,32),(17,42),(10,39))],True)
        path('rind',(12,26),[('C',(26,12),(25,37),(37,25))]);join('rind','wedge')
