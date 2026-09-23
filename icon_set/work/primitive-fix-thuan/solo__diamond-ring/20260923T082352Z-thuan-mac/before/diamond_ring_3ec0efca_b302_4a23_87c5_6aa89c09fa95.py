"""Ring band topped by a gemstone. Lucide diamond informs deliberate gem corners. Tiny facet lines omitted; gem and band share their structural upper boundary.

SOLO48 VRECT_L, live visible envelope (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3ec0efca-b302-4a23-87c5-6aa89c09fa95'
SOURCE_PATH = 'pictographic-primitives/symbol/ring 1_3ec0efca-b302-4a23-87c5-6aa89c09fa95.svg'
AUTHOR = 'gpt-6'

class DiamondRing(Solo48):
    icon_id = 'diamond-ring'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('ring', 'diamond', 'engagement', 'wedding', 'jewelry', 'proposal', 'gem', 'marriage')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        points = [(16, 16), (14, 8), (18, 4), (30, 4), (34, 8), (32, 16)]
        for i, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line('gem-' + str(i), a, b)
        self.add_arc('band-right-top', (32, 16), (40, 28), radius_x=8, radius_y=12)
        self.add_arc('band-bottom-right', (40, 28), (24, 44), radius_x=16)
        self.add_arc('band-bottom-left', (24, 44), (8, 28), radius_x=16)
        self.add_arc('band-left-top', (8, 28), (16, 16), radius_x=8, radius_y=12)
        self.add_contour('outline', *['gem-' + str(i) for i in range(1, 6)], 'band-right-top', 'band-bottom-right', 'band-bottom-left', 'band-left-top', closed=True)
        self.add_arc('band-crown', (16, 16), (32, 16), radius_x=8, radius_y=4)
        self.relate('connect', 'outline', 'band-crown')
