"""Rising Bar Chart with Trend Arrow.

Symbol plan: Three rising chart bars on one baseline below an angular upward trend arrow. Reduce outlined narrow bars to clean solid strokes.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: No useful exact Lucide subject match; reconstruct the supplied silhouette with coherent lines and arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2277b58f-cc3b-46a1-8520-dbd319e88f7f'
SOURCE_PATH = 'pictographic-primitives/business/performance increase_2277b58f-cc3b-46a1-8520-dbd319e88f7f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rising-bar-chart-with-trend-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('chart', 'graph', 'data', 'analytics', 'trend', 'statistics', 'finance', 'comparison')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        path('base',(6,42),(8,42),(24,42),(40,42),(42,42))
        for j,(x,y) in enumerate(((8,34),(24,30),(40,26))):
            line('bar-'+str(j),(x,42),(x,y));connect('bar-'+str(j),'base')
        path('trend',(6,22),(18,14),(28,18),(42,6))
        path('arrow',(30,6),(42,6),(42,18));connect('trend','arrow')
