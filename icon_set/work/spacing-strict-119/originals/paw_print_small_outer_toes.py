'Paw print: paired round toe pads and broad lower pad rebalance the open gaps within SQUARE.'
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
        self.add_arc('left-outer-top', (6,27), (12,27), radius_x=3, radius_y=4)
        self.add_arc('left-outer-bottom', (12,27), (6,27), radius_x=3, radius_y=4)
        self.add_contour('left-outer', 'left-outer-top', 'left-outer-bottom', closed=True)

        self.add_arc('left-inner-top', (12,11), (20,11), radius_x=4, radius_y=5)
        self.add_arc('left-inner-bottom', (20,11), (12,11), radius_x=4, radius_y=5)
        self.add_contour('left-inner', 'left-inner-top', 'left-inner-bottom', closed=True)

        self.add_arc('right-inner-top', (28,11), (36,11), radius_x=4, radius_y=5)
        self.add_arc('right-inner-bottom', (36,11), (28,11), radius_x=4, radius_y=5)
        self.add_contour('right-inner', 'right-inner-top', 'right-inner-bottom', closed=True)

        self.add_arc('right-outer-top', (36,27), (42,27), radius_x=3, radius_y=4)
        self.add_arc('right-outer-bottom', (42,27), (36,27), radius_x=3, radius_y=4)
        self.add_contour('right-outer', 'right-outer-top', 'right-outer-bottom', closed=True)

        self.add_arc('pad-top',(17, 37),(31, 37),radius_x=7,radius_y=5)
        self.add_arc('pad-bottom',(31, 37),(17, 37),radius_x=7,radius_y=5)
        self.add_contour('pad', 'pad-top', 'pad-bottom', closed=True)
