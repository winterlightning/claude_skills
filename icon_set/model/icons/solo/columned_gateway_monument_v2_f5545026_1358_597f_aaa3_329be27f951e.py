# Variant of columned-gateway-monument; parent file remains unchanged.
"""A columned gateway with a raised cross and rebalanced upper tiers. SQUARE preserves the full monument; cross-to-attic clearance increased."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f5545026-1358-597f-aaa3-329be27f951e'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/brandenburg gate berlin_f5545026-1358-597f-aaa3-329be27f951e.svg'
AUTHOR = 'gpt-6'

class LandmarkVariant2(Solo48):
    icon_id = 'columned-gateway-monument-v2'
    variant_of = 'columned-gateway-monument'
    variant_label = 'More clearance below cross'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('gate', 'gateway', 'monument', 'brandenburg', 'berlin', 'landmark', 'arch', 'columns', 'architecture')

    def build(self):
        self.add_polyline('outline', (2, 24), (14, 24), (34, 24), (46, 24), (46, 46), (36, 46), (36, 32), (12, 32), (12, 46), (2, 46), closed=True)
        self.add_polyline('attic', (14, 24), (14, 16), (24, 16), (34, 16), (34, 24))
        self.relate('connect', 'attic', 'outline')
        self.add_polyline('mast', (24, 2), (24, 5), (24, 16))
        self.add_polyline('cross', (19, 5), (24, 5), (29, 5))
        self.relate('connect', 'mast', 'cross')
        self.relate('connect', 'mast', 'attic')
        self.add_line('lintel-left', (2, 32), (12, 32))
        self.add_line('lintel-right', (36, 32), (46, 32))
        self.relate('connect', 'lintel-left', 'outline')
        self.relate('connect', 'lintel-right', 'outline')
