"""Maze with Upward Exit Path.

Symbol plan: Square maze walls with open entrance; one rising route with arrow at exit. Preserve directional asymmetry and drop dense branches.
SQUARE centerline extremes (6,6)-(42,42); envelope follows the subject's proportions.
Construction reference: No useful exact Lucide maze match; coherent orthogonal paths and shared route/arrow tip.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'ddb96ee7-aaa5-56e2-b813-eb8ea6f175ab'
SOURCE_PATH = 'pictographic-primitives/business/maze strategy_ddb96ee7-aaa5-56e2-b813-eb8ea6f175ab.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'maze-with-upward-exit-path'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('maze', 'with', 'upward', 'exit', 'path')

    def build(self) -> None:

        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        path('wall-left',(10,6),(6,6),(6,22),(6,42),(16,42))
        path('wall-right',(36,6),(42,6),(42,42),(34,42))
        path('route',(24,42),(24,30),(32,30),(32,22),(24,22),(24,6))
        path('arrow',(16,14),(24,6),(32,14))
        connect('route','arrow')
        path('branch',(6,22),(14,22),(14,32))
        connect('wall-left','branch')
