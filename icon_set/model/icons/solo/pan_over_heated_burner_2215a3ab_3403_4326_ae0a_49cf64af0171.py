"""Frying Pan on Stove Burner."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2215a3ab-3403-4326-ae0a-49cf64af0171'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/stove induction pan_2215a3ab-3403-4326-ae0a-49cf64af0171.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pan-over-heated-burner'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('pan', 'stove', 'burner', 'heat', 'cooking', 'kitchen', 'skillet')

    def build(self):
        # Plan: Side-view frying pan over burner and three heat marks. Lucide cooking-pot coherent rim and shallow vessel. Five heat marks reduced to three, long handle retained. Envelope (4,8)-(44,40).
        self.add_polyline('rim',(4,8),(16,8),(44,8))
        self.add_bezier('pan',(16,8),((16,12),(16,14),(16,16)),((16,20),(20,20),(24,20)),((28,20),(32,20),(36,20)),((44,20),(44,16),(44,8)))
        self.relate('connect','pan','rim')
        for x in (20,30,40):self.add_line(f'heat-{x}',(x,29),(x,31))
        self.add_line('burner',(16,40),(44,40))
