"""Fish Shaped Pastry Taiyaki."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f8a79412-2951-4699-9934-43d0710ff866'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/desert fish shaped grilled bun taiyaki_f8a79412-2951-4699-9934-43d0710ff866.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'taiyaki-fish-pastry'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('taiyaki', 'fish', 'pastry', 'japanese', 'dessert', 'bun', 'food')

    def build(self):
        # Plan: Fish-shaped taiyaki with rounded tail, eye and one gill. Lucide fish coherent silhouette. Two decorative curves reduced to one. Left-facing envelope (4,10)-(44,38).
        self.add_bezier('fish',(4,24),((4,16),(11,10),(20,10)),((25,10),(29,13),(32,16)),((38,10),(44,11),(44,18)),((44,22),(44,26),(44,30)),((44,37),(38,38),(32,32)),((29,35),(25,38),(20,38)),((11,38),(4,32),(4,24)))
        self.add_contour('pastry','fish',closed=True)
        self.add_dot('eye',(14,24))
        self.add_bezier('gill',(24,21),((27,23),(27,25),(24,27)))
