"""Rejected scientist was oversized goggles without a coat. Restore smaller round spectacles with visible lenses, circular face, broad shoulders and lab-coat collar.
Symbol plan: human_ref/user.svg circular jaw bottom28 and shoulders32 touching ink; original coat and spectacles.
Keyshape VRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c61c2ca8-17c1-4390-9206-72043bde469f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__scientist-with-round-glasses/20260929T112503Z-thuan-mac/reference/scientist_c61c2ca8-17c1-4390-9206-72043bde469f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'scientist-with-round-glasses'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('scientist', 'with', 'round', 'glasses')
    human_construction = "bust"
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

        circle('head',24,16,12)
        circle('lens-l',16,16,4);circle('lens-r',32,16,4)
        line('bridge',(20,16),(28,16));join('bridge','lens-l');join('bridge','lens-r');join('head','lens-l');join('head','lens-r')
        path('shoulders',(8,44),[('C',(12,36),(8,40),(10,38)),('A',(24,32),20,20,True),('A',(36,36),20,20,True),('C',(40,44),(38,38),(40,40))])
        join('head','shoulders')
        poly('collar',(12,36),(24,44),(36,36));join('collar','shoulders')
