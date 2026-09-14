"""Long low receiver, short front sight, separate angled grip and wider magazine. Small trigger detail omitted; source proportions restore the automatic-rifle reading."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '835277d4-590e-5008-a9cb-07213ea668e9'
SOURCE_PATH = 'pictographic-primitives/war/modern weapon machine gun_835277d4-590e-5008-a9cb-07213ea668e9.svg'
AUTHOR = 'gpt-6'

class AutomaticRifleV2(Solo48):
    icon_id = 'automatic-rifle-v2'
    variant_of = 'automatic-rifle'
    variant_label = 'Clearer construction and spacing'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('automatic', 'rifle')

    def build(self):

        def L(n,a,b): self.add_line(n,a,b)
        def P(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def A(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def J(a,b): self.relate('connect',a,b)
        def C(n,x,y,r):
            A(n+'-upper',(x-r,y),(x+r,y),r)
            A(n+'-lower',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'-upper',n+'-lower',closed=True)

        P('receiver',(6,16),(14,16),(18,12),(38,12),(38,18),(38,24),(32,24),(23,24),(14,24),(6,30),closed=True)
        L('barrel',(38,18),(42,18));J('barrel','receiver')
        L('front-sight',(38,12),(38,8));J('front-sight','receiver')
        P('magazine',(23,24),(25,40),(34,40),(32,24));J('magazine','receiver')
        L('pistol-grip',(14,24),(8,40));J('pistol-grip','receiver')
