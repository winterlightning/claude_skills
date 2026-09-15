"""Irregular Stone with Crack.

Symbol plan: Asymmetric broad stone polygon with a crack attached at one edge. Retain deliberate geological corners.
HRECT_L centerline extremes (4,8)-(44,40); envelope follows the subject's proportions.
Construction reference: No useful Lucide subject match; basic coherent arcs and straight runs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'fa848293-9c2c-5921-89bd-d869e2bd6293'
SOURCE_PATH = 'pictographic-primitives/construction/material stone_fa848293-9c2c-5921-89bd-d869e2bd6293.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'irregular-stone-with-crack'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('irregular', 'stone', 'with', 'crack')

    def build(self) -> None:

        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        path('stone',(4,24),(12,12),(28,8),(44,18),(44,30),(32,40),(12,36),(4,24),closed=True)
        path('crack',(4,24),(16,24),(22,30))
        connect('stone','crack')
