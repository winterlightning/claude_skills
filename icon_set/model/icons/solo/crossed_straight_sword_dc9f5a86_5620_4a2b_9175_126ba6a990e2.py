"""Two consistent blade widths and aligned grips. Rear edges stop exactly at the front blade; Lucide swords informed the occlusion and perpendicular guards."""
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
    category = 'war'
    aliases = ()
    keywords = ('crossed', 'straight', 'sword')

    def build(self):

        def L(n,a,b): self.add_line(n,a,b)
        def P(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def A(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def J(a,b): self.relate('connect',a,b)
        def C(n,x,y,r):
            A(n+'-upper',(x-r,y),(x+r,y),r)
            A(n+'-lower',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'-upper',n+'-lower',closed=True)

        P('front-blade',(30,38),(24,32),(16,24),(8,16),(6,6),(16,8),(24,16),(32,24),(38,30))
        P('rear-tip',(24,16),(32,8),(42,6),(40,16),(32,24));J('rear-tip','front-blade')

        P('front-guard',(28,40),(30,38),(34,34),(38,30),(40,28));J('front-guard','front-blade')
        L('front-grip',(34,34),(42,42));J('front-grip','front-guard')
        L('rear-left-edge',(16,24),(8,32));J('rear-left-edge','front-blade')
        L('rear-right-edge',(24,32),(16,40));J('rear-right-edge','front-blade')
        P('rear-guard',(6,30),(8,32),(12,36),(16,40),(18,42));J('rear-guard','rear-left-edge');J('rear-guard','rear-right-edge')
        L('rear-grip',(12,36),(6,42));J('rear-grip','rear-guard')
