from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '807318c5-21cc-453f-a7fa-a1c902d1a221'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bitcoin-with-adjust/20260925T034659Z-thuan-mac/reference/bitcoin with adjust_807318c5-21cc-453f-a7fa-a1c902d1a221.svg'
AUTHOR = 'gpt-6'
# Plan: Recognizable Bitcoin B with two top and bottom currency ticks; omit adjustment controls to prioritize reviewer request for bitcoin.
# Construction reference: Lucide bitcoin double currency ticks and two bowls.
# Envelope: VRECT_M; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = 'bitcoin-with-adjust'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bitcoin', 'with', 'adjust')
    def build(self):
        self.add_polyline('spine',(14,12),(14,24),(14,36))
        self.add_line('top',(10,12),(32,12))
        self.add_arc('upper',(32,12),(32,24),radius_x=6)
        self.add_line('mid',(14,24),(32,24))
        self.add_arc('lower',(32,24),(32,36),radius_x=6)
        self.add_line('bottom',(32,36),(10,36))
        for a,b in [('spine','top'),('spine','mid'),('spine','bottom'),('top','upper'),('upper','mid'),('upper','lower'),('mid','lower'),('lower','bottom')]:
            self.relate('connect',a,b)
        for x in (18,26):
            self.add_line(f'top-tick-{x}',(x,4),(x,12))
            self.add_line(f'bottom-tick-{x}',(x,36),(x,44))
            self.relate('connect',f'top-tick-{x}','top')
            self.relate('connect',f'bottom-tick-{x}','bottom')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=4):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
