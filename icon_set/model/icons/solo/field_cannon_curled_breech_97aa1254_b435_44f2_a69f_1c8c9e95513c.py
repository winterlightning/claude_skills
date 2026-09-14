"""A coherent curled breech and wider barrel replace the pinched overlap. The wheel is smaller, with a 9-unit hub clearance. The source supplies the subject; no useful exact Lucide cannon match exists."""
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
    keywords = ('field', 'cannon', 'curled', 'breech')

    def build(self):

        def L(n,a,b): self.add_line(n,a,b)
        def P(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def A(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def J(a,b): self.relate('connect',a,b)
        def C(n,x,y,r):
            A(n+'-upper',(x-r,y),(x+r,y),r)
            A(n+'-lower',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'-upper',n+'-lower',closed=True)

        A('wheel-ul',(13,31),(22,22),9)
        A('wheel-ur',(22,22),(31,31),9)
        A('wheel-lr',(31,31),(22,40),9)
        A('wheel-ll',(22,40),(13,31),9)
        self.add_contour('wheel','wheel-ul','wheel-ur','wheel-lr','wheel-ll',closed=True)
        self.add_dot('hub',(22,31))
        A('breech',(13,31),(13,13),9)
        L('upper-barrel',(13,13),(40,8))
        L('muzzle',(40,8),(44,18))
        L('lower-barrel',(44,18),(22,22))
        self.add_contour('barrel','breech','upper-barrel','muzzle','lower-barrel')
        J('barrel','wheel')
        L('trail',(13,31),(6,38));J('trail','wheel');J('trail','barrel')
