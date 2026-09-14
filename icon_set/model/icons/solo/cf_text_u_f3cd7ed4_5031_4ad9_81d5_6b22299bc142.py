"""Cf (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3cd7ed4-5031-4ad9-81d5-6b22299bc142'
SOURCE_PATH = 'icons-json/symbol/cf (text u)_f3cd7ed4-5031-4ad9-81d5-6b22299bc142.json'
AUTHOR = 'json_to_solo'

class CfTextU(Solo48):
    icon_id = 'cf-text-u'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cf', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 9), (8, 21))
        self.add_line('e1', (34, 8), (34, 27))
        self.add_line('e2', (31, 11), (40, 11))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_bezier('e4', (21, 8), ((19.79, 5.982), (17.74, 4.009), (15.05, 4.009)), ((14.89, 4.009), (14.73, 4), (14.57, 4)), ((14.49, 4), (14.41, 4), (14.33, 4.009)), ((11.38, 4.009), (8, 6.382), (8, 9.236)), ((8, 9.309), (8, 8.927), (8, 9)))
        self.add_bezier('e5', (8, 21), ((8, 24.718), (12.73, 27.209), (16.31, 26.509)), ((18.51, 26.082), (19.95, 24.727), (21, 23)))
        self.add_bezier('e6', (40, 4), ((39.99, 4), (39.99, 4), (39.98, 4)), ((39.98, 4.118), (39.73, 4), (39.6, 4)), ((38.75, 4), (37.89, 4), (37.04, 4)), ((35.55, 4), (34, 6.745), (34, 8)))
        self.add_contour('c0', 'e4', 'e0', 'e5')
        self.add_contour('c1', 'e6', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
