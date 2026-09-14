"""Folding package (health), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9af2bc7d-2f9e-491c-8b50-ab4286375de7'
SOURCE_PATH = 'icons-json/health/folding package_9af2bc7d-2f9e-491c-8b50-ab4286375de7.json'
AUTHOR = 'json_to_solo'

class FoldingPackageHealth(Solo48):
    icon_id = 'folding-package-health'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('folding', 'package', 'health')

    def build(self):
        self.add_line('sym-e0', (24, 42), (18, 42))
        self.add_bezier('sym-e1', (18, 42), ((16.953, 41.575), (17.458, 41.023), (17, 40)))
        self.add_line('sym-e2', (17, 40), (17, 31))
        self.add_line('sym-e3', (17, 31), (8, 31))
        self.add_bezier('sym-e4', (8, 31), ((7.002, 30.534), (6.475, 30.99), (6, 30)))
        self.add_line('sym-e5', (6, 30), (6, 18))
        self.add_bezier('sym-e6', (6, 18), ((6.458, 17.018), (6.961, 17.466), (8, 17)))
        self.add_line('sym-e7', (8, 17), (17, 17))
        self.add_line('sym-e8', (17, 17), (17, 8))
        self.add_bezier('sym-e9', (17, 8), ((17.286, 7.313), (17.084, 6), (18, 6)))
        self.add_line('sym-e10', (18, 6), (24, 6))
        self.add_line('sym-e11', (24, 6), (30, 6))
        self.add_bezier('sym-e12', (30, 6), ((30.916, 6), (30.714, 7.313), (31, 8)))
        self.add_line('sym-e13', (31, 8), (31, 17))
        self.add_line('sym-e14', (31, 17), (40, 17))
        self.add_bezier('sym-e15', (40, 17), ((41.039, 17.466), (41.542, 17.018), (42, 18)))
        self.add_line('sym-e16', (42, 18), (42, 30))
        self.add_bezier('sym-e17', (42, 30), ((41.525, 30.99), (40.998, 30.534), (40, 31)))
        self.add_line('sym-e18', (40, 31), (31, 31))
        self.add_line('sym-e19', (31, 31), (31, 40))
        self.add_bezier('sym-e20', (31, 40), ((30.542, 41.023), (31.047, 41.575), (30, 42)))
        self.add_line('sym-e21', (30, 42), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
