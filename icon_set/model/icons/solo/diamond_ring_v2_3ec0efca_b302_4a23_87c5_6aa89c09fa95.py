# Variant of diamond-ring; parent file remains unchanged.
"""Ring band topped by a gemstone. Lucide diamond informs deliberate gem corners. Tiny facet lines omitted; gem and band share their structural upper boundary.

SOLO48 VRECT_L, live visible envelope (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3ec0efca-b302-4a23-87c5-6aa89c09fa95'
SOURCE_PATH = 'pictographic-primitives/symbol/ring 1_3ec0efca-b302-4a23-87c5-6aa89c09fa95.svg'
AUTHOR = 'gpt-6'

class DiamondRingVariant2(Solo48):
    icon_id = 'diamond-ring-v2'
    variant_of = 'diamond-ring'
    variant_label = 'Design rules: exact bounds and open spacing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('ring', 'diamond', 'engagement', 'wedding', 'jewelry', 'proposal', 'gem', 'marriage')

    def build(self):
        # Lucide gem: deliberate facet corners; band uses exact cardinal ellipse and circle junctions, mirrored about x=24.
        self.add_polyline('gem', (16, 16), (12, 8), (18, 4), (30, 4), (36, 8), (32, 16), closed=False)
        self.add_arc('band-top-right', (32, 16), (40, 28), radius_x=8, radius_y=12, sweep=True)
        self.add_arc('band-bottom-right', (40, 28), (24, 44), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('band-bottom-left', (24, 44), (8, 28), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('band-top-left', (8, 28), (16, 16), radius_x=8, radius_y=12, sweep=True)
        self.add_contour('outline', 'gem-1', 'gem-2', 'gem-3', 'gem-4', 'gem-5', 'band-top-right', 'band-bottom-right', 'band-bottom-left', 'band-top-left', closed=True)
        self.add_arc('crown', (16, 16), (32, 16), radius_x=8, radius_y=4, sweep=True)
        self.relate("connect", 'outline', 'crown')
