"""Virtual coin crypto waves (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be021017-186f-4ca6-9f9e-837185cd059f'
SOURCE_PATH = 'pictographic-primitives/design/virtual coin crypto waves_be021017-186f-4ca6-9f9e-837185cd059f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class VirtualCoinCryptoWaves(Solo48):
    icon_id = 'virtual-coin-crypto-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'waves', 'design')

    def build(self):
        self.add_arc('sym-e2', (24, 6), (22, 7), radius_x=3, sweep=False)
        self.add_line('sym-e3', (22, 7), (7, 22))
        self.add_arc('sym-e4', (7, 22), (6, 24), radius_x=4, sweep=False)
        self.add_arc('sym-e9', (6, 24), (7, 26), radius_x=4, sweep=False)
        self.add_line('sym-e10', (7, 26), (22, 41))
        self.add_arc('sym-e11', (22, 41), (24, 42), radius_x=3, sweep=False)
        self.add_arc('sym-e16', (24, 42), (26, 41), radius_x=3, sweep=False)
        self.add_line('sym-e17', (26, 41), (41, 26))
        self.add_arc('sym-e18', (41, 26), (42, 24), radius_x=3, sweep=False)
        self.add_arc('sym-e23', (42, 24), (41, 22), radius_x=3, sweep=False)
        self.add_line('sym-e24', (41, 22), (26, 7))
        self.add_arc('sym-e25', (26, 7), (24, 6), radius_x=4, sweep=False)
        self.add_contour('sym-c0', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
