"""The rejected USB mouse had a short inverted-U cable and a blocklike plug. Restore a large looping cable around the rounded mouse and an angled USB connector.
Symbol plan: Lucide mouse rounded capsule and scroll mark; original looping USB cable.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'edeebc99-5db6-408a-828d-f317f5d07c5b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wired-usb-mouse/20260929T124732Z-thuan-mac/reference/keyboard usb_edeebc99-5db6-408a-828d-f317f5d07c5b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'wired-usb-mouse'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('wired', 'usb', 'mouse')

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

        box('mouse',21,18,39,42,9)
        line('wheel',(30,26),(30,30))
        path('cable',(30,18),[('L',(30,14)),('C',(18,6),(30,6),(24,6)),('C',(6,22),(8,6),(6,12)),('C',(14,42),(6,32),(8,40))])
        poly('plug',(14,42),(22,38),(18,30),(10,34),closed=True);join('plug','cable')
