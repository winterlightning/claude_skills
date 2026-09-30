"""The rejected winged lion had a blocky single wing, a plain rounded head and squared limbs. Restore a swept wing, a scalloped mane and a rounded muzzle with stepping feet.
Symbol plan: Original winged lion; swept wing and rounded head; fine mane scallops and distant legs reduced.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd518e467-fc65-46ea-a989-a754cb583565'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__winged-lion-in-profile/20260929T124732Z-thuan-mac/reference/winged lion_d518e467-fc65-46ea-a989-a754cb583565.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'winged-lion-in-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('winged', 'lion', 'in', 'profile')

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

        path('lion',(10,28),[('L',(6,36)),('L',(10,40)),('L',(18,40)),('L',(16,34)),('L',(28,34)),('L',(34,40)),('L',(44,40)),('L',(38,32)),('C',(44,24),(42,32),(44,29)),('C',(38,16),(44,19),(43,16)),('C',(30,24),(30,16),(30,18)),('L',(22,24)),('L',(22,16)),('C',(4,8),(22,11),(13,11)),('C',(10,28),(5,18),(8,23))],True)
        path('tail',(10,28),[('C',(4,31),(5,26),(4,28))]);join('tail','lion')
