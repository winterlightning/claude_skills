"""Bipod Mortar. Diagonal tube and splayed bipod; sight nub omitted.
Keyshape SQUARE: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ee17620e-81ef-4b79-88d8-0ce13c726c44'
SOURCE_PATH = 'pictographic-primitives/war/die cast_ee17620e-81ef-4b79-88d8-0ce13c726c44.svg'
AUTHOR = 'gpt-6'

class BipodMortar(Solo48):
    icon_id = 'bipod-mortar'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('mortar', 'bipod', 'tube', 'artillery', 'baseplate', 'weapon')

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

        P('tube',(11,32),(34,6),(42,14),(19,40),(11,32))
        P('foot',(6,42),(19,42),(19,40));J('foot','tube')
        P('legs',(24,34),(28,42),(24,34),(40,42));J('legs','tube')
