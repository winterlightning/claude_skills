"""Pool player aiming, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='bcaab976-a053-4420-bd38-48bdf4e984d6'
SOURCE_PATH='pictographic-primitives/sports/pool player_bcaab976-a053-4420-bd38-48bdf4e984d6.svg'
AUTHOR='gpt-6'

class PoolPlayerAiming(Solo48):
    icon_id='pool-player-aiming'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    aliases=()
    keywords=('pool', 'player', 'aiming')
    def build(self) -> None:
        # SQUARE centerline extremes (6, 6, 42, 42).
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def arc(n,a,b,r,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line(f'{n}-{i}',a,b)
        circle('head',28,9,3)
        self.add_polyline('arm',(6,26),(15,21),(33,25),(36,34))
        self.add_polyline('cue',(6,34),(17,34),(36,34),(42,34))
        self.relate('connect','arm','cue')
        self.add_line('torso',(15,21),(17,34))
        self.relate('connect','arm','torso')
        self.relate('connect','torso','cue')
        self.add_polyline('legs',(12,42),(17,34),(25,42))
        self.relate('connect','torso','legs')
        self.relate('connect','cue','legs')
