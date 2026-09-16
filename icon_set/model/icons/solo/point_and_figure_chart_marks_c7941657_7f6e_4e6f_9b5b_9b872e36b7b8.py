"""Point-and-Figure Chart Marks.

Symbol plan: Four identical X marks flank two stacked open circles. Shared repeat dimensions preserve the staggered chart arrangement.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: Lucide chart-no-axes-combined informs uniform chart-series construction; source supplies point-and-figure symbols.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'c7941657-7f6e-4e6f-9b5b-9b872e36b7b8'
SOURCE_PATH = 'pictographic-primitives/business/point figure chart_c7941657-7f6e-4e6f-9b5b-9b872e36b7b8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'point-and-figure-chart-marks'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('point and figure', 'chart', 'graph', 'data', 'analytics', 'trend', 'statistics', 'finance', 'comparison')

    def build(self) -> None:

        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j in range(4): arc(n+str(j),pts[j],pts[j+1],r)
            join(n,*(n+str(j) for j in range(4)),closed=True)

        for j,(x,y) in enumerate(((10,10),(38,10),(10,29),(38,29))):
            path('cross-a-'+str(j),(x-4,y-4),(x,y),(x+4,y+4))
            path('cross-b-'+str(j),(x-4,y+4),(x,y),(x+4,y-4));connect('cross-a-'+str(j),'cross-b-'+str(j))
        for j,y in enumerate((20,39)):circle('circle-'+str(j),24,y,3)
