"""The rejected headset used small circular strap loops and a sharp V nose. Restore a wide visor with a rounded nose arch and a broader head strap.
Symbol plan: Original headset; symmetric rounded visor and broad head outline.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd16bbdd4-caba-5737-9a5d-49dbef78c13a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vr-headset-front-view/20260929T122443Z-thuan-mac/reference/meta quest pro_d16bbdd4-caba-5737-9a5d-49dbef78c13a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'vr-headset-front-view'
    keyshape = Keyshape.SQUARE
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

        path('visor',(12,16),[('L',(36,16)),('A',(42,22),6,6,True),('L',(42,28)),('A',(36,34),6,6,True),('L',(32,34)),('C',(24,25),(28,34),(28,25)),('C',(16,34),(20,25),(20,34)),('L',(12,34)),('A',(6,28),6,6,True),('L',(6,22)),('A',(12,16),6,6,True)],True)
        path('strap',(10,16),[('C',(24,6),(10,9),(16,6)),('C',(38,16),(32,6),(38,9))]);join('strap','visor')
        path('lower',(12,34),[('C',(24,42),(12,40),(18,42)),('C',(36,34),(30,42),(36,40))]);join('lower','visor')
