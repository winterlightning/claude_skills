"""Fresh Lettuce Salad Bowl."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d37911e-43a8-420e-8739-1a7629d69da3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/salad_3d37911e-43a8-420e-8739-1a7629d69da3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'leafy-salad-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('salad', 'lettuce', 'bowl', 'leaf', 'vegetable', 'meal', 'food')

    def build(self):
        # Plan: Scalloped lettuce leaves above a shallow bowl. Lucide salad rim and leaf overlap. Fine veins omitted; uneven leaf heights retained. Envelope (6,6)-(42,42).
        self.add_polyline('rim',(6,28),(30,28),(42,28))
        self.add_bezier('bowl',(42,28),((42,37),(34,42),(24,42)),((14,42),(6,37),(6,28)))
        self.relate('connect','bowl','rim')
        self.add_bezier('leaves',(6,28),((6,20),(10,14),(16,18)),((13,12),(15,6),(22,6)),((28,6),(32,12),(28,18)),((32,14),(35,10),(38,12)),((42,14),(42,22),(42,28)))
        self.relate('connect','leaves','rim');self.relate('connect','leaves','bowl')
        self.add_bezier('fold',(28,18),((31,21),(32,24),(30,28)));self.relate('connect','fold','leaves');self.relate('connect','fold','rim')
