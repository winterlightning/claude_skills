"""Fencing Foil, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='86ebe00d-869c-51ce-ae7e-d1f92e7d5482'
SOURCE_PATH='pictographic-primitives/sports/sword fencing_86ebe00d-869c-51ce-ae7e-d1f92e7d5482.svg'
AUTHOR='gpt-6'

class FencingFoil(Solo48):
    icon_id='fencing-foil'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    aliases=()
    keywords=('fencing', 'foil', 'sword', 'blade', 'guard', 'equipment')
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
        def wave(n,y):
            for i,x in enumerate((6,18,30)):
                arc(f'{n}-{i}',(x,y),(x+12,y),6,2,sweep=i%2==0)
            self.add_contour(n,*[f'{n}-{i}' for i in range(3)])
        axis=24
        def mirror(p):return (2*axis-p[0],p[1])
        self.add_line('handle',(6,42),(18,30))
        self.add_line('blade',(18,20),(42,6))
        arc('guard-a',(8,30),(18,20),10)
        arc('guard-b',(18,20),(28,30),10)
        poly('guard-edge',(28,30),(18,30),(8,30))
        self.add_contour('guard','guard-a','guard-b','guard-edge-1','guard-edge-2',closed=True)
        self.relate('connect','handle','guard')
        self.relate('connect','blade','guard')
