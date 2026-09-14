"""Symbol medical (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2218007-b6c4-5c1b-9355-0c9d6d72fb5c'
SOURCE_PATH = 'icons-json/protection/symbol medical_c2218007-b6c4-5c1b-9355-0c9d6d72fb5c.json'
AUTHOR = 'json_to_solo'

class SymbolMedicalProtection(Solo48):
    icon_id = 'symbol-medical-protection'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('symbol', 'medical', 'protection')

    def build(self):
        self.add_line('e0', (30, 18), (30, 8))
        self.add_line('e1', (27, 6), (21, 6))
        self.add_line('e2', (18, 8), (18, 18))
        self.add_line('e3', (18, 18), (8, 18))
        self.add_line('e4', (6, 19), (6, 28))
        self.add_line('e5', (9, 30), (18, 30))
        self.add_line('e6', (18, 30), (18, 39))
        self.add_line('e7', (19, 42), (26, 42))
        self.add_line('e8', (30, 41), (30, 30))
        self.add_line('e9', (30, 30), (40, 30))
        self.add_line('e10', (42, 28), (42, 20))
        self.add_line('e11', (40, 18), (30, 18))
        self.add_bezier('e12', (30, 8), ((30, 6.985), (28.934, 6.008), (28.001, 6.008)), ((27.854, 6.008), (27.698, 6), (27.551, 6)), ((27.461, 6), (27.09, 6), (27, 6)))
        self.add_bezier('e13', (21, 6), ((20.681, 6), (20.081, 6.016), (19.762, 6.016)), ((18.813, 6.016), (18, 7.043), (18, 8)))
        self.add_bezier('e14', (8, 18), ((7.059, 18), (6.573, 18.386), (6, 19)))
        self.add_bezier('e15', (6, 28), ((6, 28.082), (6, 28.255), (6, 28.336)), ((6, 30.243), (7.797, 30), (9, 30)))
        self.add_bezier('e16', (18, 39), ((18, 39.941), (17.635, 40.92), (18.273, 41.746)), ((18.363, 41.828), (18.445, 41.918), (18.535, 42)), ((18.723, 42), (18.812, 42), (19, 42)))
        self.add_bezier('e17', (26, 42), ((26.712, 42), (27.878, 41.992), (28.59, 41.992)), ((29.089, 41.992), (29.673, 41.319), (30, 41)))
        self.add_bezier('e18', (40, 30), ((40.925, 30), (42, 29.686), (42, 28.598)), ((42, 28.426), (42, 28.172), (42, 28)))
        self.add_bezier('e19', (42, 20), ((42, 19.877), (42, 19.672), (41.992, 19.549)), ((41.992, 18.207), (40.884, 18), (40, 18)))
        self.add_contour('c0', 'e0', 'e12', 'e1', 'e13', 'e2', 'e3', 'e14', 'e4', 'e15', 'e5', 'e6', 'e16', 'e7', 'e17', 'e8', 'e9', 'e18', 'e10', 'e19', 'e11', closed=True)
