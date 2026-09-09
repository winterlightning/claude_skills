# Variant of paw-print; parent file remains unchanged.
'Paw print with enlarged circular toes and rounded mirrored central pad. Lucide paw-print informs coherent round lobes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3a1bcec0-4f4d-5256-8275-cc56ec3fa7d1'
SOURCE_PATH = 'pictographic-primitives/animals/animal print paw_3a1bcec0-4f4d-5256-8275-cc56ec3fa7d1.svg'
AUTHOR = 'gpt-6'

class PawPrintVariant2(Solo48):
    icon_id = 'paw-print-v2'
    variant_of = 'paw-print'
    variant_label = 'Larger circular toes and smooth pad'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('paw', 'print', 'track', 'footprint', 'animal', 'pet', 'dog', 'cat', 'wildlife')

    def build(self) -> None:
        # SQUARE centerline extremes (2,2)-(46,46). Mirrored toe pairs.
        self.add_arc('outer-left-top', (2,23), (12,23), radius_x=5, radius_y=5)
        self.add_arc('outer-left-bottom', (12,23), (2,23), radius_x=5, radius_y=5)
        self.add_contour('outer-left', 'outer-left-top','outer-left-bottom', closed=True)
        self.add_arc('inner-left-top', (10,7), (20,7), radius_x=5, radius_y=5)
        self.add_arc('inner-left-bottom', (20,7), (10,7), radius_x=5, radius_y=5)
        self.add_contour('inner-left', 'inner-left-top','inner-left-bottom', closed=True)
        self.add_arc('inner-right-top', (28,7), (38,7), radius_x=5, radius_y=5)
        self.add_arc('inner-right-bottom', (38,7), (28,7), radius_x=5, radius_y=5)
        self.add_contour('inner-right', 'inner-right-top','inner-right-bottom', closed=True)
        self.add_arc('outer-right-top', (36,23), (46,23), radius_x=5, radius_y=5)
        self.add_arc('outer-right-bottom', (46,23), (36,23), radius_x=5, radius_y=5)
        self.add_contour('outer-right', 'outer-right-top','outer-right-bottom', closed=True)
        self.add_arc('pad-crown', (15,37), (33,37), radius_x=9, radius_y=11)
        self.add_arc('pad-right-lobe', (33,37), (28,46), radius_x=5, radius_y=9)
        self.add_arc('pad-notch-right', (28,46), (24,44), radius_x=6, sweep=False)
        self.add_arc('pad-notch-left', (24,44), (20,46), radius_x=6, sweep=False)
        self.add_arc('pad-left-lobe', (20,46), (15,37), radius_x=5, radius_y=9)
        self.add_contour('pad', 'pad-crown','pad-right-lobe','pad-notch-right','pad-notch-left','pad-left-lobe', closed=True)
