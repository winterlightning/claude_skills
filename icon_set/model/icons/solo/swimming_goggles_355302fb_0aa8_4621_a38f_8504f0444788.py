"""Swimming Goggles, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='355302fb-0aa8-4621-a38f-8504f0444788'
SOURCE_PATH='pictographic-primitives/sports/swimming goggles_355302fb-0aa8-4621-a38f-8504f0444788.svg'
AUTHOR='gpt-6'

class SwimmingGoggles(Solo48):
    icon_id='swimming-goggles'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('swimming', 'goggles', 'lens', 'eyewear', 'protection', 'equipment')
    def build(self) -> None:
        # CIRCLE centerline extremes (4, 4, 44, 44) from current SOLO48 contract.
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
        for n,x in [('left',12),('right',36)]:
            arc(n+'-top',(x-8,24),(x+8,24),8,6)
            arc(n+'-bottom',(x+8,24),(x-8,24),8,6)
            self.add_contour(n,n+'-top',n+'-bottom',closed=True)
        self.add_line('bridge',(20,24),(28,24))
        self.relate('connect','bridge','left')
        self.relate('connect','bridge','right')
