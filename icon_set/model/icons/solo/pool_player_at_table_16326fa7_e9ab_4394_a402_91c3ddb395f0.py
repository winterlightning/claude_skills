"""Pool player at table, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='16326fa7-e9ab-4394-a402-91c3ddb395f0'
SOURCE_PATH='pictographic-primitives/sports/pool player table_16326fa7-e9ab-4394-a402-91c3ddb395f0.svg'
AUTHOR='gpt-6'

class PoolPlayerAtTable(Solo48):
    icon_id='pool-player-at-table'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    aliases=()
    keywords=('pool', 'player', 'at', 'table')
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
        circle('head',15,9,3)
        self.add_polyline('body',(6,32),(6,23),(15,21),(22,29),(30,24))
        self.add_line('torso',(15,21),(15,32))
        self.relate('connect','body','torso')
        self.add_polyline('legs',(9,42),(15,32),(21,42))
        self.relate('connect','torso','legs')
        self.add_line('cue',(30,24),(34,6))
        self.add_line('cue-lower',(26,42),(30,24))
        self.add_contour('cue-stick','cue-lower','cue')
        self.relate('connect','body','cue-stick')
        self.relate('connect','cue-stick','table-top')
        self.add_line('table-top',(28,33),(42,33))
        self.add_line('table-leg',(38,33),(42,42))
        self.relate('connect','table-top','table-leg')
