"""Adding Seasoning to Bowl."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a16e312-9168-40ab-847b-d4ba0dc7b6ae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/seasoning food_3a16e312-9168-40ab-847b-d4ba0dc7b6ae.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'seasoning-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('seasoning', 'shaker', 'bowl', 'cooking', 'salt', 'sprinkle', 'food')

    def build(self):
        # Plan: Tilted shaker above a broad footed bowl; two falling seasoning marks. Lucide ice-cream-bowl for bowl construction. Deliberate diagonal action. Bounds (6,6)-(42,42).
        self.add_polyline('shaker',(28,6),(42,12),(38,20),(24,14),closed=True)
        self.add_dot('seasoning-1',(12,14))
        self.add_dot('seasoning-2',(19,22))
        self.add_line('rim',(6,30),(42,30))
        self.add_bezier('bowl-right',(42,30),((42,34),(36,38),(30,38)))
        self.add_line('foot-1',(30,38),(30,42))
        self.add_line('foot-2',(30,42),(18,42))
        self.add_line('foot-3',(18,42),(18,38))
        self.add_bezier('bowl-left',(18,38),((12,38),(6,34),(6,30)))
        self.add_contour('bowl','rim','bowl-right','foot-1','foot-2','foot-3','bowl-left',closed=True)
