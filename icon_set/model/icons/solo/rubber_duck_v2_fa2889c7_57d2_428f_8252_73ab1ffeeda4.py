# Variant of rubber-duck; parent file remains unchanged.
"""Left-facing bath duck with a curved lower bill. HRECT_L bounds (2,8)-(46,40). Lucide bird informs the coherent circular head and body contour. The head and tail are deliberately asymmetric; the original eye-free reduction is retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fa2889c7-57d2-428f-8252-73ab1ffeeda4'
SOURCE_PATH = 'pictographic-primitives/babies/toy yellow duck_fa2889c7-57d2-428f-8252-73ab1ffeeda4.svg'
AUTHOR = 'gpt-6'

class RubberDuckVariant2(Solo48):
    icon_id = 'rubber-duck-v2'
    variant_of = 'rubber-duck'
    variant_label = 'Rounded curved bill'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/baby'
    aliases = ()
    keywords = ('rubber', 'duck', 'baby', 'nursery', 'toy')

    def build(self) -> None:
        self.add_arc('head-top', (10, 18), (20, 8), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('head-back', (20, 8), (30, 18), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('neck', (30, 18), (26, 26), radius_x=10, radius_y=10, sweep=True)
        self.add_line('back', (26, 26), (38, 27))
        self.add_arc('tail-rise', (38, 27), (46, 23), radius_x=10, radius_y=10, sweep=False)
        self.add_contour('upper', 'head-top', 'head-back', 'neck', 'back', 'tail-rise', closed=False)
        self.add_line('tail', (46, 23), (46, 26))
        self.add_arc('body-right', (46, 26), (32, 40), radius_x=14, radius_y=14, sweep=True)
        self.add_line('belly', (32, 40), (22, 40))
        self.add_arc('body-left', (22, 40), (10, 28), radius_x=12, radius_y=12, sweep=True)
        self.add_line('throat', (10, 28), (13, 24))
        self.add_arc('bill-1', (13, 24), (2, 18), radius_x=11, radius_y=6)
        self.add_line('bill-3', (2, 18), (10, 18))
        self.add_contour('lower', 'tail', 'body-right', 'belly', 'body-left', 'throat', 'bill-1', 'bill-3', closed=False)
        self.relate('connect', 'upper', 'lower')
