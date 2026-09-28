from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '07459f9b-1db4-4f1f-aeee-4e5113b2f2f4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__briefcase-dollar/20260927T140835Z-thuan-mac-1/reference/briefcase dollar_07459f9b-1db4-4f1f-aeee-4e5113b2f2f4.svg'
AUTHOR = "gpt-6"
# Plan: Briefcase with a curved S and projecting currency ticks, avoiding tiny enclosed loops; preserve handle and recognizable dollar.
# Construction reference: No useful exact Lucide match; supplied reference subject and geometric arc construction.
# Envelope: VRECT_L; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = 'briefcase-dollar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('briefcase', 'dollar')
    def build(self):
        self.box('case',8,12,40,44,4)
        self.add_polyline('handle',(16,12),(16,4),(32,4),(32,12))
        self.relate('connect','handle','case')
        self.add_arc('s-upper',(24,23),(24,28),radius_x=5,radius_y=3,sweep=False)
        self.add_arc('s-lower',(24,28),(24,33),radius_x=5,radius_y=3)
        self.add_contour('s','s-upper','s-lower')
        self.add_line('currency-stem',(24,21),(24,35))
        self.relate('connect','s','currency-stem')

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

