"""4g (text) (other), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac8587c1-0df5-4aea-b48e-de1aeb5f9c83'
SOURCE_PATH = 'icons-json/other/4g (text)_ac8587c1-0df5-4aea-b48e-de1aeb5f9c83.json'
AUTHOR = 'json_to_solo'

class Icon4gTextOther(Solo48):
    icon_id = 'icon-4g-text-other'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('4g', 'text', 'other')

    def build(self):
        self.add_line('e0', (19, 33), (4, 33))
        self.add_line('e1', (4, 33), (16, 8))
        self.add_line('e2', (16, 8), (16, 40))
        self.add_line('e3', (44, 33), (44, 25))
        self.add_line('e4', (44, 25), (38, 25))
        self.add_bezier('e5', (43, 13), ((41.855, 9.8), (40.109, 8.012), (37.382, 8.012)), ((37.255, 8.012), (37.127, 8), (37.009, 8)), ((36.791, 8), (36.573, 8.025), (36.355, 8.025)), ((35.009, 8.025), (33.545, 8.529), (32.364, 9.403)), ((27.936, 12.628), (27.791, 19.532), (27.855, 25.551)), ((27.909, 30.868), (28.855, 36.468), (32.736, 38.892)), ((33.718, 39.508), (34.891, 39.975), (35.973, 39.975)), ((36.118, 39.988), (36.264, 39.988), (36.409, 40)), ((36.618, 40), (36.836, 39.975), (37.045, 39.975)), ((39.664, 39.975), (42.364, 38.018), (43.509, 34.782)), ((43.709, 34.215), (43.982, 33.44), (43.982, 32.8)), ((43.991, 32.738), (43.991, 33.062), (44, 33)))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e5', 'e3', 'e4')
