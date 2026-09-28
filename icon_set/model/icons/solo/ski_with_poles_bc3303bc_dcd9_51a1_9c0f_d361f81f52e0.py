"""Ski with Poles, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='bc3303bc-dcd9-51a1-9c0f-d361f81f52e0'
SOURCE_PATH='pictographic-primitives/sports/skiing skiis_bc3303bc-dcd9-51a1-9c0f-d361f81f52e0.svg'
AUTHOR='gpt-6'

class SkiWithPoles(Solo48):
    icon_id='ski-with-poles'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('ski', 'pole', 'snow', 'winter', 'equipment', 'skiing')
    def build(self) -> None:
        # VRECT_L centerline extremes (8, 4, 40, 44) from current SOLO48 contract.
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
        arc('ski-tip',(20,8),(28,8),4)
        poly('ski-body',(28,8),(28,44),(20,44),(20,8))
        self.add_contour('ski','ski-tip','ski-body-1','ski-body-2','ski-body-3',closed=True)
        for x in (8,2*axis-8):
            self.add_polyline(f'pole-{x}',(x,4),(x,36),(x,44))
            self.add_line(f'basket-{x}',(x,36),(x+3 if x<axis else x-3,36))
            self.relate('connect',f'pole-{x}',f'basket-{x}')
