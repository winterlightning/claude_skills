"""Vote (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18b92527-4c62-4167-b94f-8857d15829a6'
SOURCE_PATH = 'icons-json/symbol/vote_18b92527-4c62-4167-b94f-8857d15829a6.json'
AUTHOR = 'json_to_solo'

class VoteSymbol(Solo48):
    icon_id = 'vote-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('vote', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 23), (15, 14))
        self.add_line('sym-e1', (15, 14), (24, 4))
        self.add_line('sym-e2', (24, 4), (33, 14))
        self.add_line('sym-e3', (33, 14), (24, 23))
        self.add_line('sym-e4', (24, 23), (11, 23))
        self.add_bezier('sym-e5', (11, 23), ((10.672, 23), (10.328, 22.936), (10, 23)))
        self.add_bezier('sym-e6', (10, 23), ((8.72, 23.255), (8, 24.555), (8, 26)))
        self.add_bezier('sym-e7', (8, 26), ((8, 26.2), (8, 26.8), (8, 27)))
        self.add_line('sym-e8', (8, 27), (8, 40))
        self.add_bezier('sym-e9', (8, 40), ((8, 40.164), (8, 40.836), (8, 41)))
        self.add_bezier('sym-e10', (8, 41), ((8, 42.845), (9.257, 44), (11, 44)))
        self.add_bezier('sym-e11', (11, 44), ((11.152, 44), (10.848, 44), (11, 44)))
        self.add_line('sym-e12', (11, 44), (24, 44))
        self.add_line('sym-e13', (24, 44), (37, 44))
        self.add_bezier('sym-e14', (37, 44), ((37.152, 44), (36.848, 44), (37, 44)))
        self.add_bezier('sym-e15', (37, 44), ((38.743, 44), (40, 42.845), (40, 41)))
        self.add_bezier('sym-e16', (40, 41), ((40, 40.836), (40, 40.164), (40, 40)))
        self.add_line('sym-e17', (40, 40), (40, 27))
        self.add_bezier('sym-e18', (40, 27), ((40, 26.8), (40, 26.2), (40, 26)))
        self.add_bezier('sym-e19', (40, 26), ((40, 24.555), (39.28, 23.255), (38, 23)))
        self.add_bezier('sym-e20', (38, 23), ((37.672, 22.936), (37.328, 23), (37, 23)))
        self.add_line('sym-e21', (37, 23), (24, 23))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
