"""Rising Bar Chart with Trend Arrow.

Symbol plan: Three ascending solid chart bars on a baseline, under a zigzag trend arrow; omit narrow hollow bars.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: Lucide chart-no-axes-combined original and atomic-debug: simple bar strokes and a connected angular trend.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '9c0e8e6a-07ed-4a64-88dc-0ddbe6c0c63c'
SOURCE_PATH = 'pictographic-primitives/business/performance increase_9c0e8e6a-07ed-4a64-88dc-0ddbe6c0c63c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rising-bar-chart-with-zigzag-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('chart', 'graph', 'data', 'analytics', 'trend', 'statistics', 'finance', 'comparison')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        path('base',(6,42),(10,42),(24,42),(38,42),(42,42))
        for j,(x,y) in enumerate(((10,34),(24,30),(38,26))):
            line('bar-'+str(j),(x,42),(x,y));connect('bar-'+str(j),'base')
        path('trend',(6,22),(18,14),(28,18),(42,6))
        path('arrow',(30,6),(42,6),(42,18));connect('trend','arrow')
