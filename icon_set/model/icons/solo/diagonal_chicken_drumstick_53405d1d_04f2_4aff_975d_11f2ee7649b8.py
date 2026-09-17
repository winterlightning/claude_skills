"""Chicken Drumstick."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53405d1d-04f2-4aff-975d-11f2ee7649b8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/drumsticks_53405d1d-04f2-4aff-975d-11f2ee7649b8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-chicken-drumstick'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('chicken', 'drumstick', 'meat', 'bone', 'poultry', 'food', 'leg')

    def build(self):
        # Plan: Meat oval with short diagonal bone and two round end lobes. Lucide drumstick construction. Intentional diagonal asymmetry. Envelope (6,6)-(42,42).
        self.add_bezier('meat',(16,24),((16,18),(23,6),(32,6)),((39,6),(42,10),(42,16)),((42,24),(30,32),(24,30)),((21,30),(17,28),(16,24)))
        self.add_contour('chicken','meat',closed=True)
        self.add_line('neck-l',(16,24),(10,30))
        self.add_bezier('bone',(10,30),((6,28),(6,30),(6,33)),((6,37),(10,38),(12,36)),((10,40),(12,42),(15,42)),((19,42),(20,38),(18,36)))
        self.add_line('neck-r',(18,36),(24,30))
        self.relate('connect','neck-l','chicken');self.relate('connect','neck-l','bone');self.relate('connect','neck-r','bone');self.relate('connect','neck-r','chicken')
