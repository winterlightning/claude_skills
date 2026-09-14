"""Amfitheater in delphi top (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2baf247e-0126-4274-99c5-a0211405791f'
SOURCE_PATH = 'icons-json/_uncategorized_03/amfitheater in delphi top_2baf247e-0126-4274-99c5-a0211405791f.json'
AUTHOR = 'json_to_solo'

class AmfitheaterInDelphiTop(Solo48):
    icon_id = 'amfitheater-in-delphi-top'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('amfitheater', 'in', 'delphi', 'top', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (4, 39), (4, 27))
        self.add_line('e1', (44, 27), (44, 39))
        self.add_line('e2', (43, 40), (36, 40))
        self.add_line('e3', (35, 39), (35, 28))
        self.add_line('e4', (13, 28), (13, 39))
        self.add_line('e5', (12, 40), (5, 40))
        self.add_bezier('e6', (4, 27), ((4, 25.57), (4.409, 23.95), (4.818, 22.6)), ((7.273, 14.35), (14.873, 8.02), (22.855, 8.02)), ((23.034, 8.02), (23.204, 8), (23.382, 8)), ((23.385, 8), (23.388, 8), (23.391, 8)), ((23.818, 8), (24.236, 8.02), (24.664, 8.02)), ((32.555, 8.02), (40.836, 14.13), (43.155, 22.55)), ((43.536, 23.93), (43.982, 25.44), (43.982, 26.9)), ((43.991, 26.93), (43.991, 26.97), (44, 27)))
        self.add_bezier('e7', (44, 39), ((43.882, 39.18), (43.936, 39.57), (43.773, 39.73)), ((43.182, 40), (43.545, 39.61), (43, 40)))
        self.add_bezier('e8', (36, 40), ((35.882, 39.95), (35.582, 39.89), (35.464, 39.84)), ((35.236, 39.66), (35.155, 39.24), (35, 39)))
        self.add_bezier('e9', (35, 28), ((35, 26.83), (33.982, 24.47), (33.427, 23.41)), ((29.236, 15.33), (18.427, 15.72), (14.427, 23.76)), ((13.827, 24.98), (13.391, 26.35), (13.218, 27.73)), ((13.173, 27.82), (13.045, 27.91), (13, 28)))
        self.add_bezier('e10', (13, 39), ((12.836, 39.25), (12.8, 39.68), (12.555, 39.84)), ((12.427, 39.89), (12.127, 39.95), (12, 40)))
        self.add_bezier('e11', (5, 40), ((4.745, 39.8), (4, 39.46), (4, 39.01)), ((4, 39.01), (4, 39), (4, 39)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', closed=True)
