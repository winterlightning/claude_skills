"""Fresh Ginger Root."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4142ec14-6a10-572f-93eb-dcbc8856121a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/ginger_4142ec14-6a10-572f-93eb-dcbc8856121a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'branching-ginger-root'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('ginger', 'root', 'rhizome', 'spice', 'knob', 'ingredient', 'food')

    def build(self):
        # Plan: Asymmetric ginger rhizome with three thick rounded offshoots. No useful exact Lucide match; coherent cubic silhouette, no surface marks. Envelope (8,4)-(40,44).
        self.add_bezier('root',(20,14),((20,10),(17,4),(24,4)),((30,4),(28,10),(29,13)),((30,18),(28,23),(30,27)),((33,30),(35,24),(38,27)),((40,28),(40,30),(40,32)),((40,37),(32,38),(30,40)),((27,44),(20,44),(18,44)),((12,44),(16,38),(12,35)),((8,33),(8,31),(8,28)),((8,23),(14,27),(17,28)),((18,23),(14,21),(11,18)),((6,15),(8,9),(12,9)),((17,9),(17,13),(20,14)))
        self.add_contour('ginger','root',closed=True)
