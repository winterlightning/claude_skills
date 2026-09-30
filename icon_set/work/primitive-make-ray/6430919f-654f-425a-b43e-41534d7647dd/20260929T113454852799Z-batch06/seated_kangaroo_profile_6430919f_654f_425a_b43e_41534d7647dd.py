"""Rejected kangaroo had a block-shaped head and absent long ears. Restore an upright rounded ear, tapered muzzle, round haunch and long raised tail. Tiny eye and forepaw omitted for spacing.
Symbol plan: No useful exact Lucide match; original reference and geometric curves.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6430919f-654f-425a-b43e-41534d7647dd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-kangaroo-profile/20260929T112503Z-thuan-mac/reference/gowalla logo 1_6430919f-654f-425a-b43e-41534d7647dd.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'seated-kangaroo-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('seated', 'kangaroo', 'profile')

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

        path('outline',(6,20),[('L',(14,12)),('L',(14,10)),('A',(22,10),4,4,True),('L',(22,16)),('C',(32,30),(29,19),(31,24)),('C',(42,28),(36,33),(40,30)),('C',(28,40),(41,37),(35,40)),('L',(28,42)),('L',(12,42)),('A',(12,34),4,4,True),('L',(20,34)),('C',(14,24),(12,33),(12,29)),('L',(6,20))],True)
