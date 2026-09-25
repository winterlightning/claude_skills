"""Fried Shrimp Tempura."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '16f4051e-4e10-5f14-b1b6-8d6038274f05'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/deep fied pawn shrimp tempura_16f4051e-4e10-5f14-b1b6-8d6038274f05.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-shrimp-tempura'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('tempura', 'shrimp', 'prawn', 'fried', 'tail', 'seafood', 'food')

    def build(self):
        # Plan: Curved shrimp tempura with scalloped coating and pointed fan tail. Lucide shrimp broad curling silhouette. Fine batter bumps reduced. Envelope (8,4)-(40,44).
        self.add_polyline('tail',(16,18),(10,4),(22,10),(26,4),(28,12),(38,8),(28,18))
        self.add_bezier('body',(28,18),((31,21),(29,24),(26,25)),((30,27),(30,29),(30,32)),((34,30),(40,30),(40,36)),((40,42),(34,44),(30,42)),((28,44),(24,44),(22,44)),((18,44),(16,43),(16,42)),((10,44),(8,40),(10,36)),((8,34),(8,32),(8,30)),((8,27),(10,26),(12,25)),((9,20),(12,18),(16,18)))
        self.relate('connect','body','tail')
