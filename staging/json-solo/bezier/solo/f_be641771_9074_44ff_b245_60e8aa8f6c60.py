"""F (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be641771-9074-44ff-b245-60e8aa8f6c60'
SOURCE_PATH = 'icons-json/typeface/f_be641771-9074-44ff-b245-60e8aa8f6c60.json'
AUTHOR = 'json_to_solo'

class F(Solo48):
    icon_id = 'f'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('f', 'typeface')

    def build(self):
        self.add_line('e0', (20, 9), (20, 44))
        self.add_line('e1', (8, 18), (38, 18))
        self.add_bezier('e2', (40, 5), ((40, 5), (39.98, 4.909), (39.98, 4.9)), ((39.98, 4.818), (35.06, 4.009), (32.84, 4.009)), ((32.643, 4), (32.446, 4), (32.249, 4)), ((32.246, 4), (32.243, 4), (32.24, 4)), ((32.06, 4), (31.86, 4.009), (31.66, 4.009)), ((25.38, 4.009), (20, 6.209), (20, 9)))
        self.add_contour('c0', 'e2', 'e0')
        self.add_contour('c1', 'e1')
