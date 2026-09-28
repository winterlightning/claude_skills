"""Sandbag Bunker with Flag. Bunker roof, flag and two sandbags; narrow firing slit removed.
Keyshape HRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a11b34be-4873-45b5-a0d7-6d6445847347'
SOURCE_PATH = 'pictographic-primitives/war/sand bag_a11b34be-4873-45b5-a0d7-6d6445847347.svg'
AUTHOR = 'gpt-6'

class SandbagBunkerWithFlag(Solo48):
    icon_id = 'sandbag-bunker-with-flag'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('bunker', 'sandbag', 'flag', 'fortification', 'shelter', 'military')

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

        P('flag',(24,20),(24,8),(37,8))
        A('roof-l',(9,30),(19,20),10)
        L('roof',(19,20),(29,20));A('roof-r',(29,20),(39,30),10)
        self.add_contour('bunker','roof-l','roof','roof-r');J('flag','bunker')
        R('bag-left',4,30,15,10,5);R('bag-right',29,30,15,10,5)
        J('bag-left','bunker');J('bag-right','bunker')
