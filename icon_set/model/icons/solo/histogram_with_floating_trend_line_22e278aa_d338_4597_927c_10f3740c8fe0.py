"""Histogram with Floating Trend Line.

Symbol plan: Left chart axis and two columns share a baseline; a detached trend line falls into a valley then rises.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: Lucide chart-no-axes-combined: separate data columns and connected trend segments.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '22e278aa-d338-4597-927c-10f3740c8fe0'
SOURCE_PATH = 'pictographic-primitives/business/photo histogram_22e278aa-d338-4597-927c-10f3740c8fe0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'histogram-with-floating-trend-line'
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

        path('axes',(6,6),(6,42),(20,42),(34,42),(42,42))
        for j,(x,y) in enumerate(((20,26),(34,32))):
            line('bar-'+str(j),(x,42),(x,y));connect('bar-'+str(j),'axes')
        path('trend',(14,12),(22,6),(32,18),(42,8))
