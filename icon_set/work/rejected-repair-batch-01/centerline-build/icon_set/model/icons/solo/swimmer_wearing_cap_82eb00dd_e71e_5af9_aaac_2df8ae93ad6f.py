"""Swimmer Wearing Cap, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='82eb00dd-e71e-5af9-aaac-2df8ae93ad6f'
SOURCE_PATH='pictographic-primitives/sports/swimming cap_82eb00dd-e71e-5af9-aaac-2df8ae93ad6f.svg'
AUTHOR='gpt-6'

class SwimmerWearingCap(Solo48):
    icon_id='swimmer-wearing-cap'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('swimming', 'cap', 'swimmer', 'head', 'face', 'sport')
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
        arc('cap',(6,20),(42,20),18,14)
        arc('face',(42,20),(6,20),18,22)
        self.add_contour('head','cap','face',closed=True)
        self.add_line('cap-edge',(6,20),(42,20))
        self.relate('connect','head','cap-edge')
        arc('smile',(20,29),(28,29),4,sweep=False)
