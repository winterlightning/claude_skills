"""Skateboard, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='9b469e31-62e5-51b7-b9fc-b6d7f9f5b55b'
SOURCE_PATH='pictographic-primitives/sports/skateboard_9b469e31-62e5-51b7-b9fc-b6d7f9f5b55b.svg'
AUTHOR='gpt-6'

class Skateboard(Solo48):
    icon_id='skateboard'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    aliases=()
    keywords=('skateboard', 'skating', 'board', 'wheel', 'equipment', 'sport')
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
        arc('nose-left',(4,8),(14,18),10,sweep=False)
        self.add_line('deck',(14,18),(34,18))
        arc('nose-right',(34,18),(44,8),10,sweep=False)
        self.add_contour('board','nose-left','deck','nose-right')
        for x in (14,2*axis-14):circle(f'wheel-{x}',x,35,5)
