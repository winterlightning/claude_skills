"""Runner in Starting Crouch, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='af50935b-1a94-494c-83f9-bc75b2269903'
SOURCE_PATH='pictographic-primitives/sports/running ready starting posture_af50935b-1a94-494c-83f9-bc75b2269903.svg'
AUTHOR='gpt-6'

class RunnerStartingCrouch(Solo48):
    icon_id='runner-starting-crouch'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('runner', 'start', 'crouch', 'sprint', 'athletics', 'running')
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
        circle('head',9,9,3)
        self.add_polyline('back',(20,18),(30,24),(42,36))
        self.add_line('arm',(20,18),(12,42))
        self.relate('connect','arm','back')
        self.add_polyline('bent-leg',(30,24),(22,34),(30,42))
        self.relate('connect','back','bent-leg')
