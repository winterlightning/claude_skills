"""Treadmill, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='e0a53706-08a2-42be-aca8-be485e413c8c'
SOURCE_PATH='pictographic-primitives/sports/sport treadmill_e0a53706-08a2-42be-aca8-be485e413c8c.svg'
AUTHOR='gpt-6'

class Treadmill(Solo48):
    icon_id='treadmill'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    aliases=()
    keywords=('treadmill', 'running', 'fitness', 'exercise', 'machine', 'equipment')
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
        poly('top',(10,28),(32,28),(38,28))
        arc('right-a',(38,28),(44,34),6)
        arc('right-b',(44,34),(38,40),6)
        self.add_line('bottom',(38,40),(10,40))
        arc('left',(10,40),(10,28),6)
        self.add_contour('base','top-1','top-2','right-a','right-b','bottom','left',closed=True)
        self.add_polyline('console',(20,12),(28,12),(38,12),(42,8))
        self.add_line('inner-post',(28,12),(32,28))
        self.add_line('outer-post',(38,12),(44,34))
        for n in ['inner-post','outer-post']:
            self.relate('connect',n,'base')
            self.relate('connect',n,'console')
