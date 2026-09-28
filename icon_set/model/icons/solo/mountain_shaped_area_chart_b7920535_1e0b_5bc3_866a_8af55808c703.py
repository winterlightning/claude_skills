"""Mountain-Shaped Area Chart.

Symbol plan: Area chart with two unequal peaks and visible left axis; remove no essential features.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: No useful exact Lucide subject match; reconstruct the supplied silhouette with coherent lines and arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b7920535-1e0b-5bc3-866a-8af55808c703'
SOURCE_PATH = 'pictographic-primitives/business/mountain_b7920535-1e0b-5bc3-866a-8af55808c703.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mountain-shaped-area-chart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('area chart', 'chart', 'graph', 'data', 'analytics', 'trend', 'statistics', 'finance', 'comparison')

    def build(self) -> None:

        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        path('axes',(4,8),(4,40),(44,40))
        path('area',(4,40),(16,24),(24,30),(32,12),(44,32),(44,40))
        connect('axes','area')
