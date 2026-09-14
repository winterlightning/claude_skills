"""Cao dai (religion), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a804c88-15f7-4476-b406-236f03484b85'
SOURCE_PATH = 'icons-json/religion/cao dai_1a804c88-15f7-4476-b406-236f03484b85.json'
AUTHOR = 'json_to_solo'

class CaoDaiReligion(Solo48):
    icon_id = 'cao-dai-religion'
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
        self.add_bezier('sym-e4', (24, 21), ((26.35, 21), (28.902, 21.748), (31, 23)))
        self.add_bezier('sym-e5', (31, 23), ((32.409, 23.842), (33.027, 24.737), (34, 26)))
        self.add_bezier('sym-e6', (34, 26), ((34.162, 26.217), (35, 26.808), (35, 27)))
        self.add_bezier('sym-e7', (35, 27), ((35, 27.001), (35, 26.999), (35, 27)))
        self.add_bezier('sym-e8', (35, 27), ((34.855, 27.185), (35.145, 27.815), (35, 28)))
        self.add_bezier('sym-e9', (35, 28), ((33.936, 29.432), (32.573, 31.032), (31, 32)))
        self.add_bezier('sym-e10', (31, 32), ((28.834, 33.325), (26.331, 34), (24, 34)))
        self.add_bezier('sym-e11', (24, 34), ((21.669, 34), (19.166, 33.325), (17, 32)))
        self.add_bezier('sym-e12', (17, 32), ((15.427, 31.032), (14.064, 29.432), (13, 28)))
        self.add_bezier('sym-e13', (13, 28), ((12.855, 27.815), (13.145, 27.185), (13, 27)))
        self.add_bezier('sym-e14', (13, 27), ((13, 26.999), (13, 27.001), (13, 27)))
        self.add_bezier('sym-e15', (13, 27), ((13, 26.808), (13.838, 26.217), (14, 26)))
        self.add_bezier('sym-e16', (14, 26), ((14.973, 24.737), (15.591, 23.842), (17, 23)))
        self.add_bezier('sym-e17', (17, 23), ((19.098, 21.748), (21.65, 21), (24, 21)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', closed=True)
        self.add_contour('sym-c1', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
