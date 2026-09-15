"""Baby bottle with teat shoulders extended to both body sidewalls. VRECT_M (11,6)-(37,42). Mirrored elliptical shoulders preserve the nipple and rounded body; no detail omitted. No additional useful Lucide match."""
# Variant of baby-bottle; parent file remains unchanged.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '017fdfd5-cc7b-55c1-97bd-dfe302867ff9'
SOURCE_PATH = 'pictographic-primitives/babies/baby care bottle_017fdfd5-cc7b-55c1-97bd-dfe302867ff9.svg'
AUTHOR = 'gpt-6'

class BabyBottle(Solo48):
    icon_id = 'baby-bottle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/baby-care'
    aliases = ()
    keywords = ('bottle', 'baby', 'milk', 'feeding', 'teat', 'infant', 'formula', 'nursing')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        self.add_line('body-1', (8, 18), (8, 37))
        self.add_arc('body-2', (8, 37), (18, 44), radius_x=10, radius_y=7, sweep=False)
        self.add_line('body-3', (18, 44), (30, 44))
        self.add_arc('body-4', (30, 44), (40, 37), radius_x=10, radius_y=7, sweep=False)
        self.add_line('body-5', (40, 37), (40, 18))
        self.add_line('body-6', (40, 18), (8, 18))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', closed=True)
        self.add_line('teat-1', (8, 18), (8, 12))
        self.add_arc('teat-2', (8, 12), (20, 8), radius_x=12, radius_y=4, sweep=True)
        self.add_line('teat-3', (20, 8), (20, 8))
        self.add_arc('teat-4', (20, 8), (28, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_line('teat-5', (28, 8), (28, 8))
        self.add_arc('teat-6', (28, 8), (40, 12), radius_x=12, radius_y=4, sweep=True)
        self.add_line('teat-7', (40, 12), (40, 18))
        self.add_contour('teat', 'teat-1', 'teat-2', 'teat-3', 'teat-4', 'teat-5', 'teat-6', 'teat-7', closed=False)
        self.relate('connect', 'body', 'teat')
