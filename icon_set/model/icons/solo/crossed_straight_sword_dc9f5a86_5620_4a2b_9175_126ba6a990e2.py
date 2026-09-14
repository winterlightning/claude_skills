"""Crossed Straight Swords. Lucide swords informs one blade passing in front; stepped occlusion replaces a crowded crossing.
Keyshape SQUARE: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dc9f5a86-5620-4a2b-9175-126ba6a990e2'
SOURCE_PATH = 'pictographic-primitives/war/sword fight_dc9f5a86-5620-4a2b-9175-126ba6a990e2.svg'
AUTHOR = 'gpt-6'

class CrossedStraightSword(Solo48):
    icon_id = 'crossed-straight-sword'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('sword', 'crossed', 'blade', 'hilt', 'duel', 'weapon')

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

        P('first',(6,6),(17,9),(34,30),(26,38),(9,17),closed=True)
        P('second-upper',(24,19),(34,9),(42,6),(39,17),(29,26));J('second-upper','first')
        L('second-lower',(19,28),(6,42));J('second-lower','first')
        L('guard',(24,40),(40,24));J('guard','first')
        L('grip',(30,34),(38,42));J('grip','first');J('grip','guard')
