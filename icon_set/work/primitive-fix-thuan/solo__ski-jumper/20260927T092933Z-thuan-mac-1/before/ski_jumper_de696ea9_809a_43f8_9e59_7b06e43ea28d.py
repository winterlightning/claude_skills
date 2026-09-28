"""Ski Jumper, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='de696ea9-809a-43f8-9e59-7b06e43ea28d'
SOURCE_PATH='pictographic-primitives/sports/ski jumping_de696ea9-809a-43f8-9e59-7b06e43ea28d.svg'
AUTHOR='gpt-6'

class SkiJumper(Solo48):
    icon_id='ski-jumper'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('ski', 'jump', 'skier', 'winter', 'athlete', 'flight')
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
        circle('head',36,9,3)
        self.add_polyline('body',(26,17),(15,29),(10,41))
        self.add_polyline('ski',(6,42),(10,41),(36,32))
        arc('ski-tip',(36,32),(42,26),6,sweep=False)
        self.relate('connect','body','ski')
        self.relate('connect','ski','ski-tip')
