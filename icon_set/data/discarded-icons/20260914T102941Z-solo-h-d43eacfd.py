"""H (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd43eacfd-b338-4b75-a892-35bf7092ad5f'
SOURCE_PATH = 'icons-json/typeface/h_d43eacfd-b338-4b75-a892-35bf7092ad5f.json'
AUTHOR = 'json_to_solo'

class HD43eacfd(Solo48):
    icon_id = 'h-d43eacfd'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('h', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (8, 44))
        self.add_bezier('e1', (8, 24), ((8, 23.982), (8.032, 23.973), (8.032, 23.955)), ((8.032, 23.273), (9.984, 21.745), (10.688, 21.245)), ((15.008, 18.155), (22.688, 17.127), (29.248, 18.236)), ((37.424, 19.627), (39.968, 24.782), (39.968, 29.145)), ((39.968, 29.445), (40, 29.755), (40, 30.064)), ((40, 33.636), (39.984, 37.2), (40, 40.773)), ((40, 41.709), (40, 42.636), (40, 43.573)), ((40, 43.709), (39.76, 43.991), (40, 43.991)), ((40, 44), (40, 44), (40, 44)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.relate('connect', 'c1', 'c0')
