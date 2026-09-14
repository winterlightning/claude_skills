"""Field Cannon with Curled Breech. Upward barrel, round wheel and curled breech; wheel occludes lower barrel.
Keyshape HRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '97aa1254-b435-44f2-a69f-1c8c9e95513c'
SOURCE_PATH = 'pictographic-primitives/war/cannon_97aa1254-b435-44f2-a69f-1c8c9e95513c.svg'
AUTHOR = 'gpt-6'

class FieldCannonCurledBreech(Solo48):
    icon_id = 'field-cannon-curled-breech'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('cannon', 'artillery', 'wheel', 'barrel', 'carriage', 'weapon')

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

        C('wheel',24,30,10);self.add_dot('hub',(24,30))
        P('barrel',(16,24),(10,20),(40,8),(42,18),(32,24));J('barrel','wheel')
        L('trail',(16,36),(6,40));J('trail','wheel')
        A('breech',(10,20),(6,26),6,s=False);J('breech','barrel')
