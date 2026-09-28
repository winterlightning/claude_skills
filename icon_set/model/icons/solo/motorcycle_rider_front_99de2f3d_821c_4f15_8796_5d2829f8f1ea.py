"""Motorcycle rider front, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='99de2f3d-821c-4f15-8796-5d2829f8f1ea'
SOURCE_PATH='pictographic-primitives/sports/racing_99de2f3d-821c-4f15-8796-5d2829f8f1ea.svg'
AUTHOR='gpt-6'

class MotorcycleRiderFront(Solo48):
    icon_id='motorcycle-rider-front'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('motorcycle', 'rider', 'front')
    def build(self) -> None:
        # VRECT_L centerline extremes (8, 4, 40, 44).
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def arc(n,a,b,r,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line(f'{n}-{i}',a,b)
        circle('head',24,8,4)
        self.add_polyline('shoulders',(8,29),(13,21),(24,21),(35,21),(40,29))
        self.add_polyline('left-grip',(8,29),(10,34),(10,44))
        self.add_polyline('right-grip',(40,29),(38,34),(38,44))
        self.relate('connect','shoulders','left-grip')
        self.relate('connect','shoulders','right-grip')
        self.add_polyline('wheel',(20,44),(20,33),(28,33),(28,44),closed=True)
