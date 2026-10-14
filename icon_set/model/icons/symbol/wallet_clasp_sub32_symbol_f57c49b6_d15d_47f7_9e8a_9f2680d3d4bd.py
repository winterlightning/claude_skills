"""Independent 32px profile of wallet-clasp.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd'
SOURCE_PATH = 'pictographic-primitives/symbol/wallet_f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd', 'pictographic-primitives/symbol/wallet_f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wallet-clasp',)
SOLO_SOURCE_ICON_IDS = ('wallet-clasp',)
REFERENCE_EXPORT_SHA256 = 'b4723a46cd93b18bf5fb5fcf0dad6e9c2d424c06fcc22e72c7947aefc9339692'

class DrawingContainerSymbol(Sub32):
    icon_id = 'wallet-clasp-sub32-symbol'
    related_origin_icon_id = 'wallet-clasp-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/wallet-clasp-sub32'
    counterpart_icon_id = 'wallet-clasp-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Wallet: rounded body with a clasp tab on the right.
        self.add_line('w-1', (6, 4), (26, 4))
        self.add_arc('w-2', (26, 4), (30, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('w-3', (30, 8), (30, 24))
        self.add_arc('w-4', (30, 24), (26, 28), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('w-5', (26, 28), (6, 28))
        self.add_arc('w-6', (6, 28), (2, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('w-7', (2, 24), (2, 8))
        self.add_arc('w-8', (2, 8), (6, 4), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('wallet', 'w-1', 'w-2', 'w-3', 'w-4', 'w-5', 'w-6', 'w-7', 'w-8', closed=True)
        self.add_line('tab-1', (30, 12), (22, 12))
        self.add_arc('tab-2', (22, 12), (22, 20), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('tab-3', (22, 20), (30, 20))
        self.add_contour('tab', 'tab-1', 'tab-2', 'tab-3')
        self.relate('connect', 'wallet', 'tab')
