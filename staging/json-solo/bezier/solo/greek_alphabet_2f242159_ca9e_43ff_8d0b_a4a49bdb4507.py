"""Greek alphabet (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f242159-ca9e-43ff-8d0b-a4a49bdb4507'
SOURCE_PATH = 'icons-json/interface-essential/greek alphabet_2f242159-ca9e-43ff-8d0b-a4a49bdb4507.json'
AUTHOR = 'json_to_solo'

class GreekAlphabetInterfaceEssential(Solo48):
    icon_id = 'greek-alphabet-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('greek', 'alphabet', 'interface-essential')

    def build(self):
        self.add_bezier('sym-e0', (24, 6), ((24.134, 6), (23.868, 6), (24, 6)))
        self.add_bezier('sym-e1', (24, 6), ((26.086, 6), (29.135, 6.1), (31, 7)))
        self.add_bezier('sym-e2', (31, 7), ((37.275, 10.013), (40, 16.429), (40, 23)))
        self.add_bezier('sym-e3', (40, 23), ((40, 24.422), (40.333, 25.557), (40, 27)))
        self.add_bezier('sym-e4', (40, 27), ((39.002, 31.336), (35.805, 35.709), (32, 38)))
        self.add_bezier('sym-e5', (32, 38), ((30.953, 38.63), (30.121, 39.525), (29, 40)))
        self.add_line('sym-e6', (29, 40), (29, 42))
        self.add_line('sym-e7', (29, 42), (42, 42))
        self.add_bezier('sym-e8', (24, 6), ((23.866, 6), (24.132, 6), (24, 6)))
        self.add_bezier('sym-e9', (24, 6), ((21.914, 6), (18.865, 6.1), (17, 7)))
        self.add_bezier('sym-e10', (17, 7), ((10.725, 10.013), (8, 16.429), (8, 23)))
        self.add_bezier('sym-e11', (8, 23), ((8, 24.422), (7.667, 25.557), (8, 27)))
        self.add_bezier('sym-e12', (8, 27), ((8.998, 31.336), (12.195, 35.709), (16, 38)))
        self.add_bezier('sym-e13', (16, 38), ((17.047, 38.63), (17.879, 39.525), (19, 40)))
        self.add_line('sym-e14', (19, 40), (19, 42))
        self.add_line('sym-e15', (19, 42), (6, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c1', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.relate('connect', 'sym-c0', 'sym-c1')
