"""Close quote (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2921ecef-6779-4e0d-9ac0-683c2ff1cada'
SOURCE_PATH = 'icons-json/interface-essential/close quote_2921ecef-6779-4e0d-9ac0-683c2ff1cada.json'
AUTHOR = 'json_to_solo'

class CloseQuoteInterfaceEssential(Solo48):
    icon_id = 'close-quote-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('close', 'quote', 'interface-essential')

    def build(self):
        self.add_line('e0', (44, 22), (44, 10))
        self.add_line('e1', (42, 8), (36, 8))
        self.add_line('e2', (21, 22), (21, 10))
        self.add_line('e3', (19, 8), (12, 8))
        self.add_bezier('e4', (29, 40), ((29.118, 40), (29.7, 39.992), (29.818, 39.992)), ((31.3, 39.992), (32.9, 39.512), (34.218, 38.922)), ((39.8, 36.421), (42.591, 30.855), (43.564, 25.448)), ((43.682, 24.766), (43.755, 24.076), (43.845, 23.394)), ((43.864, 23.225), (44, 23.015), (44, 22.863)), ((44, 22.686), (44, 22.152), (44, 22)))
        self.add_bezier('e5', (44, 10), ((44, 9.916), (44, 9.516), (43.991, 9.432)), ((43.991, 8.556), (42.655, 8.236), (42, 8)))
        self.add_bezier('e6', (36, 8), ((35.927, 8.008), (35.664, 8.008), (35.591, 8.017)), ((34.582, 8.017), (33.427, 8.488), (32.555, 8.918)), ((28.045, 11.149), (25.836, 16.387), (27.691, 20.834)), ((28.982, 23.924), (32.082, 26.072), (35.618, 26.484)), ((36.582, 26.594), (38.027, 27.008), (39, 27)))
        self.add_bezier('e7', (6, 40), ((6.118, 40), (6.064, 39.992), (6.182, 39.992)), ((7.482, 39.992), (8.873, 39.613), (10.082, 39.208)), ((16.055, 37.213), (19.3, 31.579), (20.591, 26.114)), ((20.827, 25.086), (21, 22.985), (21, 22)))
        self.add_bezier('e8', (21, 10), ((21, 8.981), (19.909, 8.328), (19, 8)))
        self.add_bezier('e9', (12, 8), ((11.927, 8.008), (12.027, 8.008), (11.955, 8.017)), ((7.855, 8.017), (4.009, 13.305), (4.009, 16.8)), ((4.009, 16.883), (4, 16.958), (4, 17.04)), ((4, 17.042), (4, 17.043), (4, 17.044)), ((4, 17.364), (4.009, 17.693), (4.009, 18.013)), ((4.009, 21.667), (7.109, 25.347), (10.918, 26.265)), ((12.236, 26.577), (13.645, 27.017), (15, 27)))
        self.add_contour('c0', 'e4', 'e0', 'e5', 'e1', 'e6')
        self.add_contour('c1', 'e7', 'e2', 'e8', 'e3', 'e9')
