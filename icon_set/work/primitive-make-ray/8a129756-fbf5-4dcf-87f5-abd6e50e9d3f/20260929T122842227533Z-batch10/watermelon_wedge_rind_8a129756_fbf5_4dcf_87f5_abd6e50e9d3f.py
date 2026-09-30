"""The rejected watermelon was an upright bowl with one seed. Restore the diagonal cut edge, curved rind and separated seeds in the flesh.
Symbol plan: Original diagonal melon wedge; smooth curved rind, simplified seed detail.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8a129756-fbf5-4dcf-87f5-abd6e50e9d3f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__watermelon-wedge-rind/20260929T122443Z-thuan-mac/reference/melon_8a129756-fbf5-4dcf-87f5-abd6e50e9d3f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'watermelon-wedge-rind'
    keyshape = Keyshape.HRECT_L
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

        path('wedge',(4,30),[('L',(36,8)),('C',(44,22),(42,12),(44,17)),('C',(25,40),(44,34),(36,40)),('C',(4,30),(16,40),(8,37))],True)
        path('rind',(11,25),[('C',(34,13),(22,42),(43,29))]);join('rind','wedge')
        self.add_dot('seed',(24,22))
