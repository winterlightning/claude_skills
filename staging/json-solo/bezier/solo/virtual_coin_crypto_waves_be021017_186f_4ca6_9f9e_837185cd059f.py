"""Virtual coin crypto waves (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be021017-186f-4ca6-9f9e-837185cd059f'
SOURCE_PATH = 'icons-json/design/virtual coin crypto waves_be021017-186f-4ca6-9f9e-837185cd059f.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoWavesDesign(Solo48):
    icon_id = 'virtual-coin-crypto-waves-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'waves', 'design')

    def build(self):
        self.add_bezier('sym-e0', (24, 6), ((23.976, 6), (24.025, 6), (24, 6)))
        self.add_bezier('sym-e1', (24, 6), ((23.918, 6), (24.082, 6), (24, 6)))
        self.add_bezier('sym-e2', (24, 6), ((23.288, 6), (22.515, 6.485), (22, 7)))
        self.add_line('sym-e3', (22, 7), (7, 22))
        self.add_bezier('sym-e4', (7, 22), ((6.517, 22.483), (6, 23.329), (6, 24)))
        self.add_bezier('sym-e5', (6, 24), ((6, 24.074), (6, 23.926), (6, 24)))
        self.add_bezier('sym-e6', (6, 24), ((6, 24.014), (6, 23.986), (6, 24)))
        self.add_bezier('sym-e7', (6, 24), ((6, 24.014), (6, 23.986), (6, 24)))
        self.add_bezier('sym-e8', (6, 24), ((6, 24.074), (6, 23.926), (6, 24)))
        self.add_bezier('sym-e9', (6, 24), ((6, 24.671), (6.517, 25.517), (7, 26)))
        self.add_line('sym-e10', (7, 26), (22, 41))
        self.add_bezier('sym-e11', (22, 41), ((22.515, 41.515), (23.288, 42), (24, 42)))
        self.add_bezier('sym-e12', (24, 42), ((24.082, 42), (23.918, 42), (24, 42)))
        self.add_bezier('sym-e13', (24, 42), ((24.025, 42), (23.976, 42), (24, 42)))
        self.add_bezier('sym-e14', (24, 42), ((24.024, 42), (23.975, 42), (24, 42)))
        self.add_bezier('sym-e15', (24, 42), ((24.082, 42), (23.918, 42), (24, 42)))
        self.add_bezier('sym-e16', (24, 42), ((24.712, 42), (25.485, 41.515), (26, 41)))
        self.add_line('sym-e17', (26, 41), (41, 26))
        self.add_bezier('sym-e18', (41, 26), ((41.483, 25.517), (42, 24.671), (42, 24)))
        self.add_bezier('sym-e19', (42, 24), ((42, 23.926), (42, 24.074), (42, 24)))
        self.add_bezier('sym-e20', (42, 24), ((42, 23.986), (42, 24.014), (42, 24)))
        self.add_bezier('sym-e21', (42, 24), ((42, 23.986), (42, 24.014), (42, 24)))
        self.add_bezier('sym-e22', (42, 24), ((42, 23.926), (42, 24.074), (42, 24)))
        self.add_bezier('sym-e23', (42, 24), ((42, 23.329), (41.483, 22.483), (41, 22)))
        self.add_line('sym-e24', (41, 22), (26, 7))
        self.add_bezier('sym-e25', (26, 7), ((25.485, 6.485), (24.712, 6), (24, 6)))
        self.add_bezier('sym-e26', (24, 6), ((23.918, 6), (24.082, 6), (24, 6)))
        self.add_bezier('sym-e27', (24, 6), ((23.975, 6), (24.024, 6), (24, 6)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', closed=True)
