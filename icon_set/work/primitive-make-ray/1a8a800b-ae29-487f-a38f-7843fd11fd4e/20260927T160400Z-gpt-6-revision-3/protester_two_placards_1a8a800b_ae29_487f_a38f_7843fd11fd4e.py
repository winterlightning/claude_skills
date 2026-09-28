"""Protester Holding Two Placards. Two placards and central person retained; poles and hands combined into arm strokes.
Keyshape HRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1a8a800b-ae29-487f-a38f-7843fd11fd4e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__protester-two-placards/20260927T153803Z-thuan-mac-1/reference/protest_1a8a800b-ae29-487f-a38f-7843fd11fd4e.svg'
AUTHOR = "gpt-6"

class ProtesterTwoPlacards(Solo48):
    icon_id = 'protester-two-placards'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('protester', 'placard', 'sign', 'person', 'demonstration', 'rally')

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

        P('left-sign',(4,8),(16,8),(16,20),(4,20),closed=True)
        P('right-sign',(32,8),(44,8),(44,20),(32,20),closed=True)
        C('head',24,28,3)
        self.add_bezier('arms',(10,20),((8,30),(14,35),(16,40)));J('arms','left-sign')
        self.add_bezier('right-arm',(38,20),((40,30),(34,35),(32,40)));J('right-arm','right-sign')
        self.add_bezier('shoulders',(16,40),((19,39),(29,39),(32,40)));J('shoulders','arms');J('shoulders','right-arm')
