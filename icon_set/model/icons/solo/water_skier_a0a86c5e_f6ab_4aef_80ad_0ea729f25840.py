"""Water Skier, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='a0a86c5e-f6ab-4aef-80ad-0ea729f25840'
SOURCE_PATH='pictographic-primitives/sports/skating_a0a86c5e-f6ab-4aef-80ad-0ea729f25840.svg'
AUTHOR='gpt-6'

class WaterSkier(Solo48):
    icon_id='water-skier'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('water', 'skier', 'skiing', 'rider', 'glide', 'sport')
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
        circle('head',18,11,3)
        self.add_polyline('body',(15,23),(14,31),(22,28),(24,34))
        self.add_polyline('arm',(6,27),(15,23),(30,21),(44,21))
        self.relate('connect','arm','body')
        arc('ski-left',(4,34),(24,34),10,6,sweep=False)
        arc('ski-right',(24,34),(44,34),10,6,sweep=False)
        self.add_contour('ski','ski-left','ski-right')
        self.relate('connect','ski','body')
