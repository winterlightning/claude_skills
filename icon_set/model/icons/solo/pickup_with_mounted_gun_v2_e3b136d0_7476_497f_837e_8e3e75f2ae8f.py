"""Square layout adds vertical room between mounted gun and cab. Smaller matched wheels, clear bed and a 10-unit gun-to-roof gap; Lucide truck informed wheel/chassis construction. No tiny window is added."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e3b136d0-7476-497f-837e-8e3e75f2ae8f'
SOURCE_PATH = 'pictographic-primitives/war/van machine gun_e3b136d0-7476-497f-837e-8e3e75f2ae8f.svg'
AUTHOR = 'gpt-6'

class PickupWithMountedGunV2(Solo48):
    icon_id = 'pickup-with-mounted-gun-v2'
    variant_of = 'pickup-with-mounted-gun'
    variant_label = 'Clearer construction and spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('pickup', 'with', 'mounted', 'gun')

    def build(self):

        def L(n,a,b): self.add_line(n,a,b)
        def P(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def A(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def J(a,b): self.relate('connect',a,b)
        def C(n,x,y,r):
            A(n+'-upper',(x-r,y),(x+r,y),r)
            A(n+'-lower',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'-upper',n+'-lower',closed=True)

        C('rear-wheel',12,38,4);C('front-wheel',36,38,4)
        P('body',(8,38),(6,32),(6,24),(11,24),(24,24),(24,16),(33,16),(42,27),(42,32),(40,38))
        J('body','rear-wheel');J('body','front-wheel')
        L('chassis',(16,38),(32,38));J('chassis','rear-wheel');J('chassis','front-wheel')
        P('gun',(6,6),(16,6),(16,14),(11,14),(6,14),closed=True)
        L('barrel',(16,6),(42,6));J('barrel','gun')
        L('mount',(11,14),(11,24));J('mount','gun');J('mount','body')
