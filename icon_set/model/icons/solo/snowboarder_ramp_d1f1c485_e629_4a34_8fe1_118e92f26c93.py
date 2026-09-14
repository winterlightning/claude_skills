"""Snowboarder over Ramp, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d1f1c485-e629-4a34-8fe1-118e92f26c93'
SOURCE_PATH='pictographic-primitives/sports/snowskating_d1f1c485-e629-4a34-8fe1-118e92f26c93.svg'
AUTHOR='gpt-6'

class SnowboarderRamp(Solo48):
    icon_id='snowboarder-ramp'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('snowboard', 'ramp', 'board', 'snow', 'winter', 'athlete')
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
        circle('head',14,9,3)
        self.add_polyline('arms',(8,23),(20,19),(34,6))
        self.add_polyline('body',(20,19),(19,24),(28,26),(29,31))
        self.relate('connect','body','arms')
        self.add_line('leg',(19,24),(14,31))
        self.relate('connect','body','leg')
        self.add_polyline('board',(10,31),(14,31),(29,31),(37,26))
        self.relate('connect','board','body')
        self.relate('connect','board','leg')
        self.add_line('ramp',(6,42),(34,40))
        arc('ramp-tip',(34,40),(42,42),8,2)
        self.relate('connect','ramp','ramp-tip')
