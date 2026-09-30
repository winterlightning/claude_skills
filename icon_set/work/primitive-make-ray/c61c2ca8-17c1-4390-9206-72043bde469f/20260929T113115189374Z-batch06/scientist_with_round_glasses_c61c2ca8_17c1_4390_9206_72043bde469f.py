"""Rejected scientist was a giant pair of goggles with no lab coat. Reduce head and spectacle proportions, add a clear coat collar, and keep a round jaw and touching shoulders.
Symbol plan: human_ref/user.svg: circular jaw and paired shoulders; coat collar restores scientist identity.
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
        circle('lens-l',18,16,4);circle('lens-r',30,16,4)
        line('bridge',(22,16),(26,16));line('temple-l',(12,16),(14,16));line('temple-r',(34,16),(36,16))
        for n in ['lens-l','lens-r']:join('bridge',n)
        join('temple-l','head');join('temple-l','lens-l');join('temple-r','head');join('temple-r','lens-r')
        path('shoulders',(8,44),[('A',(24,32),17,17,True),('A',(40,44),17,17,True)])
        join('head','shoulders')
        poly('collar',(16,34),(24,44),(32,34));join('collar','shoulders')
