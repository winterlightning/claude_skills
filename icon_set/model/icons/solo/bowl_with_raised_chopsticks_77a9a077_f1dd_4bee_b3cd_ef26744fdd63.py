"""Bowl with Chopsticks."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77a9a077-f1dd-4bee-b3cd-ef26744fdd63'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/soup_77a9a077-f1dd-4bee-b3cd-ef26744fdd63.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bowl-with-raised-chopsticks'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('bowl', 'chopsticks', 'dining', 'meal', 'utensil', 'food', 'kitchen')

    def build(self):
        # Plan: Deep round bowl and splayed raised sticks. Lucide soup elliptical rim, open rear rim to preserve spacing. Deliberate right lean. Envelope (6,6)-(42,42).
        self.add_arc('bowl',(42,24),(6,24),radius_x=18)
        self.add_bezier('rim',(6,24),((12,29),(36,29),(42,24)))
        self.add_bezier('rear-l',(6,24),((6,20),(11,18),(14,18)))
        self.add_bezier('rear-r',(32,20),((36,18),(42,20),(42,24)))
        self.add_line('stick-l',(23,18),(30,6));self.add_line('stick-r',(32,20),(42,8))
        for a,b in (('bowl','rim'),('rear-l','rim'),('rear-r','rim'),('rear-l','bowl'),('rear-r','bowl'),('stick-r','rear-r')):self.relate('connect',a,b)
