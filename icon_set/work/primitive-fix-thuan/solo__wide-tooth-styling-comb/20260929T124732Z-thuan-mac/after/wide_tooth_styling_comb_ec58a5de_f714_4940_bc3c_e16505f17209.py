"""The rejected comb looked like an E with squared spine corners. Restore a rounded vertical spine and evenly spaced teeth with consistent lengths.
Symbol plan: Original styling comb; one rounded spine and an evenly spaced tooth series.
Keyshape VRECT_M: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ec58a5de-f714-4940-bc3c-e16505f17209'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wide-tooth-styling-comb/20260929T124732Z-thuan-mac/reference/comb_ec58a5de-f714-4940-bc3c-e16505f17209.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'wide-tooth-styling-comb'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('wide', 'tooth', 'styling', 'comb')

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

        path('spine',(38,4),[('L',(14,4)),('A',(10,8),4,4,False),('L',(10,40)),('A',(14,44),4,4,False),('L',(38,44))])
        for i,y in enumerate((14,24,34)):
         line(f'tooth-{i}',(10,y),(38,y));join(f'tooth-{i}','spine')
