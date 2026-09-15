"""Crossed Spiked Maces. Paired heads and crossed handles; reduced to two spikes per head.
Keyshape SQUARE: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '79c8a226-7026-5ab4-a2e4-203abe5e9998'
SOURCE_PATH = 'pictographic-primitives/war/antique mace double_79c8a226-7026-5ab4-a2e4-203abe5e9998.svg'
AUTHOR = 'gpt-6'

class CrossedSpikedMace(Solo48):
    icon_id = 'crossed-spiked-mace'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('mace', 'weapon', 'medieval', 'spike', 'crossed', 'combat')

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

        C('left-head',13,16,6);C('right-head',35,16,6)
        L('left-handle',(13,22),(33,42));J('left-handle','left-head')
        L('right-handle',(35,22),(15,42));J('right-handle','right-head');J('left-handle','right-handle')
        L('left-spike',(13,10),(13,6));J('left-spike','left-head')
        L('right-spike',(35,10),(35,6));J('right-spike','right-head')
        L('left-outer',(7,16),(6,16));J('left-outer','left-head')
        L('right-outer',(41,16),(42,16));J('right-outer','right-head')
