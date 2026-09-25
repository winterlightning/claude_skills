"""Fork and Knife Utensils."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56745c4d-820e-4bdb-9aa5-f3fbd6b451ab'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/fork and spoon_56745c4d-820e-4bdb-9aa5-f3fbd6b451ab.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-fork-and-pointed-knife'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('fork', 'knife', 'cutlery', 'dining', 'utensil', 'meal', 'kitchen')

    def build(self):
        # Plan: Upright three-tine fork beside pointed knife. Lucide utensils common baseline and open tine bowl. Narrow grips reduced to strokes. Envelope (6,6)-(42,42).
        self.add_line('tine-l',(6,6),(6,18))
        self.add_bezier('fork-bowl',(6,18),((6,23),(10,26),(14,26)),((18,26),(22,23),(22,18)))
        self.add_line('tine-r',(22,18),(22,6))
        self.add_contour('fork','tine-l','fork-bowl','tine-r')
        self.add_polyline('fork-shaft',(14,6),(14,26),(14,42));self.relate('connect','fork-shaft','fork')

        self.add_polyline('knife-spine',(34,6),(34,28),(34,42))
        self.add_bezier('blade',(34,6),((38,14),(42,21),(42,25)),((42,28),(38,28),(34,28)))
        self.relate('connect','blade','knife-spine')
