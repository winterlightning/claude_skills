from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c2a64d8a-ca70-53b9-b450-150287c2bfc6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__boxer-avatar/20260925T034659Z-thuan-mac/reference/boxer_c2a64d8a-ca70-53b9-b450-150287c2bfc6.svg'
AUTHOR = 'gpt-6'
# Plan: Boxer portrait with broad shoulders and headguard framing the face; omit facial microdetails.
# Construction reference: human_ref/user.svg broad shoulders and circular jaw; headguard retained from original.
# Envelope: VRECT_L; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = 'boxer-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('boxer', 'avatar')
    def build(self):
        self.add_arc('helmet',(10,18),(38,18),radius_x=14)
        self.add_polyline('left-pad',(10,18),(10,24),(18,24),(18,18))
        self.add_polyline('right-pad',(38,18),(38,24),(30,24),(30,18))
        self.relate('connect','helmet','left-pad')
        self.relate('connect','helmet','right-pad')
        self.add_arc('jaw',(18,18),(30,18),radius_x=6,sweep=False)
        self.relate('connect','jaw','left-pad')
        self.relate('connect','jaw','right-pad')
        self.add_arc('shoulder',(8,44),(40,44),radius_x=16,radius_y=12)

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
