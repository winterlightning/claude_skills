"""Lit Explosive Stick. Single stick with short fuse and two sparks; chamfers omitted.
Keyshape SQUARE: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '735864fd-220a-4d0d-93f7-c07a27f9fa47'
SOURCE_PATH = 'pictographic-primitives/war/explosive_735864fd-220a-4d0d-93f7-c07a27f9fa47.svg'
AUTHOR = 'gpt-6'

class LitExplosiveStick(Solo48):
    icon_id = 'lit-explosive-stick'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('explosive', 'dynamite', 'fuse', 'spark', 'stick', 'fire')

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

        P('stick',(6,34),(26,14),(34,22),(14,42),closed=True)
        L('fuse',(30,18),(35,13));J('fuse','stick')
        L('spark-top',(35,6),(35,13));J('spark-top','fuse')
        L('spark-right',(35,13),(42,13));J('spark-right','fuse');J('spark-right','spark-top')
