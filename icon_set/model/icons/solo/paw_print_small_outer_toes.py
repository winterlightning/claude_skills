# Review candidate; original preserved.
"""Paw print with enlarged oval toes and rounded mirrored central pad. Lucide paw-print informs coherent round lobes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '193cadb3-56bf-56a6-8cdf-a6db99d7d95e'
SOURCE_PATH = 'pictographic-primitives/animals/animal print_193cadb3-56bf-56a6-8cdf-a6db99d7d95e.svg'
AUTHOR = 'gpt-6'

class PawPrintSmallOuterToes(Solo48):
    icon_id = 'paw-print-small-outer-toes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('paw', 'print', 'track', 'footprint', 'animal', 'pet', 'dog', 'cat', 'wildlife')

    def build(self) -> None:
        """Opening repair: Rebuilt the two outer toes as open circles/ovals, preserving paired proportions and the central pad."""
        self.add_arc('outer-left-top', (6, 25), (12, 25), radius_x=3, radius_y=4)
        self.add_arc('outer-left-bottom', (12, 25), (6, 25), radius_x=3, radius_y=4)
        self.add_contour('outer-left', 'outer-left-top', 'outer-left-bottom', closed=True)
        self.add_arc('inner-left-top', (10, 8), (20, 8), radius_x=5, radius_y=6)
        self.add_arc('inner-left-bottom', (20, 8), (10, 8), radius_x=5, radius_y=6)
        self.add_contour('inner-left', 'inner-left-top', 'inner-left-bottom', closed=True)
        self.add_arc('inner-right-top', (28, 8), (38, 8), radius_x=5, radius_y=6)
        self.add_arc('inner-right-bottom', (38, 8), (28, 8), radius_x=5, radius_y=6)
        self.add_contour('inner-right', 'inner-right-top', 'inner-right-bottom', closed=True)
        self.add_arc('outer-right-top', (36, 25), (42, 25), radius_x=3, radius_y=4)
        self.add_arc('outer-right-bottom', (42, 25), (36, 25), radius_x=3, radius_y=4)
        self.add_contour('outer-right', 'outer-right-top', 'outer-right-bottom', closed=True)
        self.add_arc('pad-crown', (16, 38), (32, 38), radius_x=8, radius_y=9)
        self.add_arc('pad-right-lobe', (32, 38), (28, 42), radius_y=8, radius_x=4)
        self.add_arc('pad-notch-right', (28, 42), (24, 42), radius_x=6, sweep=False)
        self.add_arc('pad-notch-left', (24, 42), (20, 42), radius_x=6, sweep=False)
        self.add_arc('pad-left-lobe', (20, 42), (16, 38), radius_y=8, radius_x=4)
        self.add_contour('pad', 'pad-crown', 'pad-right-lobe', 'pad-notch-right', 'pad-notch-left', 'pad-left-lobe', closed=True)
