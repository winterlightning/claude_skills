"""Segmented Hand Grenade. Oval body, top cap and segmentation; external lever omitted for clear spacing.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4defab66-f891-589d-9113-250444b98543'
SOURCE_PATH = 'pictographic-primitives/war/bomb grenade_4defab66-f891-589d-9113-250444b98543.svg'
AUTHOR = 'gpt-6'

class SegmentedHandGrenade(Solo48):
    icon_id = 'segmented-hand-grenade'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('grenade', 'explosive', 'lever', 'cap', 'weapon', 'segment')

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

        P('neck',(18,12),(18,6),(30,6),(30,12))
        A('shoulder-r',(30,12),(40,24),10,12)
        A('lower-r',(40,24),(24,42),16,20)
        A('lower-l',(24,42),(8,24),16,20)
        A('shoulder-l',(8,24),(18,12),10,12)
        self.add_contour('body','shoulder-r','lower-r','lower-l','shoulder-l');J('neck','body')
        L('seam',(8,24),(40,24));J('seam','body')
        L('lower-seam',(24,24),(24,42));J('lower-seam','body');J('lower-seam','seam')
