"""Cao dai (religion), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a804c88-15f7-4476-b406-236f03484b85'
SOURCE_PATH = 'icons-json/religion/cao dai_1a804c88-15f7-4476-b406-236f03484b85.json'
AUTHOR = 'json_to_solo'

class CaoDai(Solo48):
    icon_id = 'cao-dai'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'religion'
    aliases = ()
    keywords = ('cao', 'dai', 'religion')

    def build(self):
        self.add_line('sym-e0', (44, 40), (24, 8))
        self.add_line('sym-e1', (24, 8), (4, 40))
        self.add_line('sym-e2', (4, 40), (44, 40))
        self.add_line('sym-e3', (24, 27), (24, 27))
        self.add_arc('sym-e4', (24, 21), (31, 23), radius_x=14)
        self.add_arc('sym-e5', (31, 23), (34, 26), radius_x=12, sweep=False)
        self.add_line('sym-e6', (34, 26), (35, 27))
        self.add_line('sym-e8', (35, 27), (35, 28))
        self.add_line('sym-e9', (35, 28), (31, 32))
        self.add_line('sym-e10', (31, 32), (24, 34))
        self.add_line('sym-e11', (24, 34), (17, 32))
        self.add_arc('sym-e12', (17, 32), (13, 28), radius_x=15)
        self.add_line('sym-e13', (13, 28), (13, 27))
        self.add_line('sym-e15', (13, 27), (14, 26))
        self.add_arc('sym-e16', (14, 26), (17, 23), radius_x=12)
        self.add_arc('sym-e17', (17, 23), (24, 21), radius_x=14)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', closed=True)
        self.add_contour('sym-c1', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
