"""Megaphone (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6916faa-9a8d-4d21-9406-4e2f3510d5f0'
SOURCE_PATH = 'icons-json/interface-essential/megaphone_b6916faa-9a8d-4d21-9406-4e2f3510d5f0.json'
AUTHOR = 'json_to_solo'

class Megaphone(Solo48):
    icon_id = 'megaphone'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('megaphone', 'interface-essential')

    def build(self):
        self.add_line('e0', (18, 32), (22, 32))
        self.add_line('e1', (44, 33), (35, 8))
        self.add_line('e2', (35, 8), (31, 11))
        self.add_line('e3', (15, 21), (7, 24))
        self.add_line('e4', (12, 33), (18, 32))
        self.add_line('e5', (18, 32), (15, 21))
        self.add_line('e6', (18, 32), (23, 40))
        self.add_bezier('e7', (22, 32), ((29.282, 30.653), (36.909, 31.484), (44, 33)))
        self.add_bezier('e8', (31, 11), ((26.745, 14.941), (20.736, 19.232), (15, 21)))
        self.add_bezier('e9', (7, 24), ((5.545, 24.446), (4.009, 26.198), (4.009, 27.604)), ((4.009, 27.712), (4, 27.812), (4, 27.919)), ((4, 27.921), (4, 27.922), (4, 27.924)), ((4, 28.168), (4.018, 28.413), (4.018, 28.657)), ((4.018, 31.04), (6.527, 33.002), (8.927, 33.364)), ((9.927, 33.516), (11, 33.152), (12, 33)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e2', 'e8', 'e3', 'e9', 'e4')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e6')
        self.relate('connect', 'c1', 'c0')
