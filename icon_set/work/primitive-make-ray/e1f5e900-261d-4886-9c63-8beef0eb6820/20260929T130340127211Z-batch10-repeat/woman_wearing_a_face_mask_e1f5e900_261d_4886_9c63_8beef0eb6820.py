"""The rejected masked woman had a hanging central bar. Restore long side hair around a complete round face with a horizontal mask edge and curved lower mask.
Symbol plan: human_ref/user.svg circular head; original long hair and lower-face mask. Fine swept fringe omitted to preserve the face and mask openings.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e1f5e900-261d-4886-9c63-8beef0eb6820'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-wearing-a-face-mask/20260929T124732Z-thuan-mac/reference/air purifier 5_e1f5e900-261d-4886-9c63-8beef0eb6820.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'woman-wearing-a-face-mask'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('woman', 'wearing', 'a', 'face', 'mask')

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

        path('hair',(6,42),[('L',(6,24)),('A',(42,24),18,18,True),('L',(42,42))])
        circle('face',24,24,9)
        line('mask-edge',(15,24),(33,24));join('mask-edge','face')
