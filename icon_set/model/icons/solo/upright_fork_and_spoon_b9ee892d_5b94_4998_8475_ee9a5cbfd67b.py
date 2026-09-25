"""Fork and Spoon Utensils."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9ee892d-5b94-4998-8475-ee9a5cbfd67b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/restaurant fork spoon_b9ee892d-5b94-4998-8475-ee9a5cbfd67b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-fork-and-spoon'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('fork', 'spoon', 'cutlery', 'utensil', 'dining', 'meal', 'tableware')

    def build(self):
        # Plan: Upright fork and oval spoon. Lucide utensils matched heights, three tines and clear separation. Narrow handles reduced to strokes. Envelope (6,6)-(42,42).
        self.add_line('tine-l',(6,6),(6,18))
        self.add_bezier('fork-bowl',(6,18),((6,23),(10,26),(14,26)),((18,26),(22,23),(22,18)))
        self.add_line('tine-r',(22,18),(22,6))
        self.add_contour('fork','tine-l','fork-bowl','tine-r')
        self.add_polyline('fork-shaft',(14,6),(14,26),(14,42));self.relate('connect','fork-shaft','fork')

        self.add_arc('spoon-r',(36,6),(36,26),radius_x=6,radius_y=10)
        self.add_arc('spoon-l',(36,26),(36,6),radius_x=6,radius_y=10)
        self.add_contour('spoon','spoon-r','spoon-l',closed=True)
        self.add_line('spoon-shaft',(36,26),(36,42));self.relate('connect','spoon-shaft','spoon')
