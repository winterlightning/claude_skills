"""Pickup with Mounted Gun. Truck, large wheels and bed-mounted gun retained; cab window omitted.
Keyshape HRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e3b136d0-7476-497f-837e-8e3e75f2ae8f'
SOURCE_PATH = 'pictographic-primitives/war/van machine gun_e3b136d0-7476-497f-837e-8e3e75f2ae8f.svg'
AUTHOR = 'gpt-6'

class PickupWithMountedGun(Solo48):
    icon_id = 'pickup-with-mounted-gun'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('pickup', 'truck', 'gun', 'mounted', 'military', 'vehicle')

    def build(self):

        def L(n,a,b): self.add_line(n,a,b)
        def P(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def A(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def C(n,x,y,r):
            A(n+'a',(x-r,y),(x+r,y),r)
            A(n+'b',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'a',n+'b',closed=True)
        def J(a,b): self.relate('connect',a,b)
        def R(n,x,y,w,h,r=4):
            L(n+'t',(x+r,y),(x+w-r,y))
            A(n+'tr',(x+w-r,y),(x+w,y+r),r)
            L(n+'r',(x+w,y+r),(x+w,y+h-r))
            A(n+'br',(x+w,y+h-r),(x+w-r,y+h),r)
            L(n+'b',(x+w-r,y+h),(x+r,y+h))
            A(n+'bl',(x+r,y+h),(x,y+h-r),r)
            L(n+'l',(x,y+h-r),(x,y+r))
            A(n+'tl',(x,y+r),(x+r,y),r)
            self.add_contour(n,*[n+s for s in ('t','tr','r','br','b','bl','l','tl')],closed=True)

        C('rear-wheel',12,34,6);C('front-wheel',36,34,6)
        P('body',(6,34),(6,34),(6,24),(23,24),(23,18),(32,18),(39,24),(42,24),(42,34),(42,34));J('body','rear-wheel');J('body','front-wheel')
        L('underbody',(18,34),(30,34));J('underbody','rear-wheel');J('underbody','front-wheel')
        P('gun',(8,8),(21,8),(21,16),(8,16),closed=True)
        L('mount',(14,16),(14,24));J('mount','gun');J('mount','body')
        L('barrel',(21,12),(40,12));J('barrel','gun')
