"""Three-Person Squad. Central rounded figure flanked by two partial torsos; overlapping outlines simplified.
Keyshape HRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '47b5d0d4-7421-51e3-82ac-4ebeeb7bce0a'
SOURCE_PATH = 'pictographic-primitives/war/symbol squad_47b5d0d4-7421-51e3-82ac-4ebeeb7bce0a.svg'
AUTHOR = 'gpt-6'

class ThreePersonSquad(Solo48):
    icon_id = 'three-person-squad'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('squad', 'group', 'people', 'team', 'military', 'person')

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

        C('middle-head',24,11,3);C('left-head',7,14,3);C('right-head',41,14,3)
        R('middle-body',18,24,12,16,4)
        P('left-body',(8,26),(5,26),(5,36),(8,36));P('right-body',(40,26),(43,26),(43,36),(40,36))
