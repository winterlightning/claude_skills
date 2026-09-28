"""Barbed Wire Knot. Central twisted barb and horizontal wire; doubled strands and tightly overlapping loops reduced.
Keyshape HRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4b91bbc3-3d86-404a-b686-fc5f17882dac'
SOURCE_PATH = 'pictographic-primitives/war/protest barb wire_4b91bbc3-3d86-404a-b686-fc5f17882dac.svg'
AUTHOR = 'gpt-6'

class BarbedWireKnot(Solo48):
    icon_id = 'barbed-wire-knot'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('wire', 'barbed', 'barb', 'fence', 'knot', 'barrier')

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

        L('wire',(4,24),(44,24))
        P('barb-left',(10,8),(24,24),(10,40));J('barb-left','wire')
        P('barb-right',(38,8),(24,24),(38,40));J('barb-right','wire');J('barb-left','barb-right')
