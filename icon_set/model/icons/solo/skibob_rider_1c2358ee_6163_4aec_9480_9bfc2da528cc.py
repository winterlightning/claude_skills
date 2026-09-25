"""Skibob Rider, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1c2358ee-6163-4aec-9480-9bfc2da528cc'
SOURCE_PATH='pictographic-primitives/sports/skibob_1c2358ee-6163-4aec-9480-9bfc2da528cc.svg'
AUTHOR='gpt-6'

class SkibobRider(Solo48):
    icon_id='skibob-rider'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    aliases=()
    keywords=('skibob', 'ski', 'bike', 'rider', 'snow', 'winter')
    def build(self) -> None:
        # SQUARE centerline extremes (6, 6, 42, 42) from current SOLO48 contract.
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
        circle('head',24,9,3)
        self.add_polyline('rider',(19,19),(13,27),(22,30),(26,39))
        self.add_polyline('arms',(19,19),(27,24),(34,21))
        self.relate('connect','rider','arms')
        self.add_polyline('steering',(34,21),(37,30),(40,42))
        self.relate('connect','arms','steering')
        self.add_polyline('seat',(6,23),(6,27),(13,27))
        self.add_line('seat-post',(13,27),(10,42))
        self.relate('connect','seat','seat-post')
        self.relate('connect','rider','seat')
        self.relate('connect','rider','seat-post')
        self.add_polyline('rear-ski',(6,42),(10,42),(18,42))
        self.relate('connect','seat-post','rear-ski')
        self.add_polyline('front-ski',(29,42),(40,42),(42,38))
        self.relate('connect','steering','front-ski')
