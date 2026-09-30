"""Tuxedo: rejected bow is oversized and jacket cropped into a box. Restore narrow bow and long tapered jacket/lapels. Rebalance bow to a wider, shallower form and taper the jacket sides.
Symbol plan: Shared center axis and mirrored bow/lapels; no useful exact Lucide match.
Keyshape VRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f9451716-545e-4b2d-baaa-edadd03ed515'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tuxedo-bow-tie/20260929T115456Z-thuan-mac/reference/tuxedo_f9451716-545e-4b2d-baaa-edadd03ed515.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'tuxedo-bow-tie'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('tuxedo', 'bow', 'tie')

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

        poly('bow-left',(8,4),(24,10),(8,16),closed=True)
        poly('bow-right',(40,4),(24,10),(40,16),closed=True);join('bow-left','bow-right')
        poly('lapels',(8,16),(24,36),(40,16));join('lapels','bow-left');join('lapels','bow-right')
        path('jacket',(8,16),[('L',(8,24)),('L',(13,44)),('L',(35,44)),('L',(40,24)),('L',(40,16))]);join('jacket','bow-left');join('jacket','bow-right');join('jacket','lapels')
        line('seam',(24,36),(24,44));join('seam','jacket');join('seam','lapels')
