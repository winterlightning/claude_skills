"""The rejected headset used small top and bottom semicircles and a sharp central notch. Restore a broad head strap, a wide visor and a rounded nose opening.
Symbol plan: Original headset; mirrored visor corners and rounded symmetric nose notch.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd16bbdd4-caba-5737-9a5d-49dbef78c13a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vr-headset-front-view/20260929T122443Z-thuan-mac/reference/meta quest pro_d16bbdd4-caba-5737-9a5d-49dbef78c13a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'vr-headset-front-view'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('vr', 'headset', 'front', 'view')

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

        path('visor',(10,18),[('L',(38,18)),('A',(44,24),6,6,True),('L',(44,29)),('A',(38,35),6,6,True),('L',(32,35)),('C',(24,30),(28,35),(29,30)),('C',(16,35),(19,30),(20,35)),('L',(10,35)),('A',(4,29),6,6,True),('L',(4,24)),('A',(10,18),6,6,True)],True)
        path('strap',(8,18),[('C',(24,8),(9,9),(16,8)),('C',(40,18),(32,8),(39,9))]);join('strap','visor')
        path('lower',(12,35),[('C',(24,40),(14,40),(19,40)),('C',(36,35),(29,40),(34,40))]);join('lower','visor')
