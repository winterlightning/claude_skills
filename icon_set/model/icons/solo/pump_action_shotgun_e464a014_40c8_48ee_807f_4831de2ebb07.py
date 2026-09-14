"""Pump-Action Shotgun. Long barrel, angled grip and separate pump fore-end; small trigger guard omitted.
Keyshape SQUARE: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e464a014-40c8-48ee-807f-4831de2ebb07'
SOURCE_PATH = 'pictographic-primitives/war/shotgun_e464a014-40c8-48ee-807f-4831de2ebb07.svg'
AUTHOR = 'gpt-6'

class PumpActionShotgun(Solo48):
    icon_id = 'pump-action-shotgun'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('shotgun', 'pump', 'barrel', 'grip', 'trigger', 'weapon')

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

        P('gun',(10,42),(6,30),(12,23),(38,6),(42,12),(16,30),(18,38),(10,42))
        P('pump',(23,25),(28,30),(36,25),(34,17));J('pump','gun')
