"""Matched curved blade shoulders join long straight runs with near-matching tangents. Continuous visible blade portions replace floating fragments; Lucide swords informed clean foreground occlusion."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0ef35f0a-e6c2-5cd6-861a-50bf28d6a460'
SOURCE_PATH = 'pictographic-primitives/war/pirate sword_0ef35f0a-e6c2-5cd6-861a-50bf28d6a460.svg'
AUTHOR = 'gpt-6'

class CrossedCutlass(Solo48):
    icon_id = 'crossed-cutlass'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('crossed', 'cutlass')

    def build(self):

        def L(n,a,b): self.add_line(n,a,b)
        def P(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def A(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def J(a,b): self.relate('connect',a,b)
        def C(n,x,y,r):
            A(n+'-upper',(x-r,y),(x+r,y),r)
            A(n+'-lower',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'-upper',n+'-lower',closed=True)

        L('front-outer-low',(30,38),(24,32))
        L('front-outer-high',(24,32),(16,24))
        A('front-curve',(16,24),(6,6),36)
        L('front-tip',(6,6),(16,8))
        L('front-inner-high',(16,8),(24,16))
        L('front-inner-mid',(24,16),(32,24))
        L('front-inner-low',(32,24),(38,30))
        self.add_contour('front-blade','front-outer-low','front-outer-high','front-curve','front-tip','front-inner-high','front-inner-mid','front-inner-low')
        L('rear-inner',(24,16),(32,8))
        L('rear-point',(32,8),(42,6))
        A('rear-curve',(42,6),(32,24),36)
        self.add_contour('rear-tip','rear-inner','rear-point','rear-curve');J('rear-tip','front-blade')

        P('front-guard',(28,40),(30,38),(34,34),(38,30),(40,28));J('front-guard','front-blade')
        L('front-grip',(34,34),(42,42));J('front-grip','front-guard')
        L('rear-left-edge',(16,24),(8,32));J('rear-left-edge','front-blade')
        L('rear-right-edge',(24,32),(16,40));J('rear-right-edge','front-blade')
        P('rear-guard',(6,30),(8,32),(12,36),(16,40),(18,42));J('rear-guard','rear-left-edge');J('rear-guard','rear-right-edge')
        L('rear-grip',(12,36),(6,42));J('rear-grip','rear-guard')
