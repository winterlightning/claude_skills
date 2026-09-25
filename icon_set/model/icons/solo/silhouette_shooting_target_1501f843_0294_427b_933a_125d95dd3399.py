"""Silhouette Shooting Target, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1501f843-0294-427b-933a-125d95dd3399'
SOURCE_PATH='pictographic-primitives/sports/shooting target_1501f843-0294-427b-933a-125d95dd3399.svg'
AUTHOR='gpt-6'

class SilhouetteShootingTarget(Solo48):
    icon_id='silhouette-shooting-target'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('shooting', 'target', 'silhouette', 'bullseye', 'practice', 'sport')
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
        arc('head-left',(18,22),(24,4),10,10)
        arc('head-right',(24,4),(30,22),10,10)
        arc('shoulder-right',(30,22),(40,32),10)
        self.add_line('side-right',(40,32),(40,44))
        self.add_line('side-left',(8,44),(8,32))
        arc('shoulder-left',(8,32),(18,22),10)
        self.add_contour('silhouette','side-left','shoulder-left','head-left','head-right','shoulder-right','side-right')
        circle('bullseye',24,34,5)
