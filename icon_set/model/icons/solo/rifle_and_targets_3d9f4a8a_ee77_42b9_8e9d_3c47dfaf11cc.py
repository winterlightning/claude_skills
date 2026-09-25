"""Rifle and Targets, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='3d9f4a8a-ee77-42b9-8e9d-3c47dfaf11cc'
SOURCE_PATH='pictographic-primitives/sports/shooting rifle target_3d9f4a8a-ee77-42b9-8e9d-3c47dfaf11cc.svg'
AUTHOR='gpt-6'

class RifleAndTargets(Solo48):
    icon_id='rifle-and-targets'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    aliases=()
    keywords=('rifle', 'target', 'shooting', 'equipment', 'sport', 'bullseye')
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
        circle('target-left',12,12,5)
        circle('target-right',36,36,5)
        self.add_polyline('rifle-stock',(6,36),(12,42),(23,31),(23,26),(18,24),closed=True)
        self.add_line('barrel',(23,26),(42,6))
        self.relate('connect','barrel','rifle-stock')
