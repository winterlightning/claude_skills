"""Prone Sled Rider, independently authored on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3dbd2a29-fec9-4e7a-83e9-5c9475ef9583'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__prone-sled-rider/20260927T153803Z-thuan-mac-1/reference/skiing chest slide_3dbd2a29-fec9-4e7a-83e9-5c9475ef9583.svg'
AUTHOR='gpt-6'

class ProneSledRider(Solo48):
    icon_id='prone-sled-rider'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('sled', 'skeleton', 'prone', 'rider', 'snow', 'winter')
    def build(self) -> None:
        # HRECT_L centerline extremes (4, 8, 44, 40) from current SOLO48 contract.
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def arc(n,a,b,r,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line(f'{n}-{i}',a,b)
        axis=24
        def mirror(p):return (2*axis-p[0],p[1])
        circle('head',40,20,3)
        self.add_polyline('rider',(8,8),(16,19),(28,24),(30,36))
        self.add_polyline('rider-lower',(8,18),(22,28),(30,36))
        self.relate('connect','rider','rider-lower')
        self.relate('connect','rider-lower','sled')
        self.relate('connect','rider','sled')
        self.add_polyline('sled',(4,25),(18,31),(30,36),(44,40))
