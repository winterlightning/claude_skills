"""Pool table with cue, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='8c179a92-08df-431d-82cd-16de168d722b'
SOURCE_PATH='pictographic-primitives/sports/pool table_8c179a92-08df-431d-82cd-16de168d722b.svg'
AUTHOR='gpt-6'

class PoolTableWithCue(Solo48):
    icon_id='pool-table-with-cue'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('pool', 'table', 'with', 'cue')
    def build(self) -> None:
        # HRECT_L centerline extremes (4, 8, 44, 40).
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def arc(n,a,b,r,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line(f'{n}-{i}',a,b)
        self.add_polyline('table',(4,8),(44,8),(44,34),(4,34),closed=True)
        self.add_line('cue-upper',(25,21),(38,34))
        self.add_line('cue-lower',(38,34),(44,40))
        self.add_contour('cue','cue-upper','cue-lower')
        self.relate('connect','cue','table')
