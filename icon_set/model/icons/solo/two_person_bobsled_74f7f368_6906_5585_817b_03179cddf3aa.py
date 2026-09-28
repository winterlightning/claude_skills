"""Two-Person Bobsled, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='74f7f368-6906-5585-817b-03179cddf3aa'
SOURCE_PATH='pictographic-primitives/sports/skiing bobsled_74f7f368-6906-5585-817b-03179cddf3aa.svg'
AUTHOR='gpt-6'

class TwoPersonBobsled(Solo48):
    icon_id='two-person-bobsled'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('bobsled', 'sled', 'rider', 'snow', 'winter', 'racing')
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
        for x in (14,29):
            circle(f'head-{x}',x,10,2)
            self.add_line(f'shoulders-{x}',(x,21),(x,24))
        poly('top',(8,24),(14,24),(18,24),(25,24),(29,24),(34,24))
        arc('nose',(34,24),(34,32),10,4)
        poly('bottom',(34,32),(32,32),(14,32),(8,32))
        arc('tail',(8,32),(8,24),4)
        self.add_contour('shell',*[f'top-{i}' for i in range(1,6)],'nose',*[f'bottom-{i}' for i in range(1,4)],'tail',closed=True)
        for x in (14,29):self.relate('connect',f'shoulders-{x}','shell')
        for x in (14,32):
            self.add_line(f'mount-{x}',(x,32),(x,40))
            self.relate('connect',f'mount-{x}','shell')
        self.add_polyline('runner',(4,40),(14,40),(32,40),(40,40))
        arc('tip',(40,40),(44,36),4,sweep=False)
        self.relate('connect','runner','tip')
        for x in (14,32):self.relate('connect',f'mount-{x}','runner')
