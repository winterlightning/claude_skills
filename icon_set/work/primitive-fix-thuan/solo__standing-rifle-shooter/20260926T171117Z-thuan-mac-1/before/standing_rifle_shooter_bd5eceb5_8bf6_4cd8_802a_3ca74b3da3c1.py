"""Standing Rifle Shooter. Bent-knee shooter and horizontal rifle; limbs use clear single strokes.
Keyshape SQUARE: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bd5eceb5-8bf6-4cd8-802a-3ca74b3da3c1'
SOURCE_PATH = 'pictographic-primitives/war/sport esport fps counterstrike_bd5eceb5-8bf6-4cd8-802a-3ca74b3da3c1.svg'
AUTHOR = 'gpt-6'

class StandingRifleShooter(Solo48):
    icon_id = 'standing-rifle-shooter'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('shooter', 'rifle', 'person', 'aim', 'stance', 'soldier')

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

        C('head',17,9,3)
        P('body',(19,20),(16,29),(10,42),(6,42))
        P('legs',(16,29),(26,35),(28,42),(34,42));J('legs','body')
        P('arms',(19,20),(28,23),(33,16));J('arms','body')
        L('rifle',(28,16),(42,16));J('rifle','arms')
