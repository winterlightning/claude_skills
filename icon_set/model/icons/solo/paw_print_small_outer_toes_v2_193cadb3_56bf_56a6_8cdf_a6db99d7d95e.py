# Variant of paw-print-small-outer-toes; parent file remains unchanged.
'Paw print with enlarged oval toes and rounded mirrored central pad. Lucide paw-print informs coherent round lobes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '193cadb3-56bf-56a6-8cdf-a6db99d7d95e'
SOURCE_PATH = 'pictographic-primitives/animals/animal print_193cadb3-56bf-56a6-8cdf-a6db99d7d95e.svg'
AUTHOR = 'gpt-6'

class PawPrintSmallOuterToesVariant2(Solo48):
    icon_id = 'paw-print-small-outer-toes-v2'
    variant_of = 'paw-print-small-outer-toes'
    variant_label = 'Larger oval toes and smooth pad'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('paw', 'print', 'track', 'footprint', 'animal', 'pet', 'dog', 'cat', 'wildlife')

    def build(self) -> None:
        # SQUARE centerline extremes (2,2)-(46,46). Mirrored toe pairs.
        self.add_arc('outer-left-top', (2,25), (12,25), radius_x=5, radius_y=6)
        self.add_arc('outer-left-bottom', (12,25), (2,25), radius_x=5, radius_y=6)
        self.add_contour('outer-left', 'outer-left-top','outer-left-bottom', closed=True)
        self.add_arc('inner-left-top', (10,8), (20,8), radius_x=5, radius_y=6)
        self.add_arc('inner-left-bottom', (20,8), (10,8), radius_x=5, radius_y=6)
        self.add_contour('inner-left', 'inner-left-top','inner-left-bottom', closed=True)
        self.add_arc('inner-right-top', (28,8), (38,8), radius_x=5, radius_y=6)
        self.add_arc('inner-right-bottom', (38,8), (28,8), radius_x=5, radius_y=6)
        self.add_contour('inner-right', 'inner-right-top','inner-right-bottom', closed=True)
        self.add_arc('outer-right-top', (36,25), (46,25), radius_x=5, radius_y=6)
        self.add_arc('outer-right-bottom', (46,25), (36,25), radius_x=5, radius_y=6)
        self.add_contour('outer-right', 'outer-right-top','outer-right-bottom', closed=True)
        self.add_arc('pad-crown', (15,38), (33,38), radius_x=9, radius_y=11)
        self.add_arc('pad-right-lobe', (33,38), (28,46), radius_x=5, radius_y=8)
        self.add_arc('pad-notch-right', (28,46), (24,44), radius_x=6, sweep=False)
        self.add_arc('pad-notch-left', (24,44), (20,46), radius_x=6, sweep=False)
        self.add_arc('pad-left-lobe', (20,46), (15,38), radius_x=5, radius_y=8)
        self.add_contour('pad', 'pad-crown','pad-right-lobe','pad-notch-right','pad-notch-left','pad-left-lobe', closed=True)
