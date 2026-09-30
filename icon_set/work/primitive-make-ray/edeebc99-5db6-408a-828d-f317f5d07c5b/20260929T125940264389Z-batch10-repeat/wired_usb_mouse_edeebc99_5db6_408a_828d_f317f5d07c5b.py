"""The rejected USB mouse had a short square cable bend and blocklike plug. Restore a rounded mouse and a broad looping cable ending in a clear USB plug.
Symbol plan: Lucide mouse capsule and scroll mark; reference large looping cord retained.
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

        box('mouse',24,20,42,42,9)
        line('wheel',(33,29),(33,32))
        path('cable',(33,20),[('L',(33,14)),('C',(20,6),(33,6),(27,6)),('C',(6,20),(10,6),(6,12)),('L',(6,26))]);join('cable','mouse')
        poly('plug',(6,26),(14,26),(14,40),(6,40),closed=True);join('plug','cable')
