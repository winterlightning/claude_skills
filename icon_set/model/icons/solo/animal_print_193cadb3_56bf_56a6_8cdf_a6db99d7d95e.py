"""Paw with four detached toe pads and scalloped main pad; centerline extremes (2,2)-(46,46). Lucide paw-print informs round toe contours; oval toes simplified to circles for native-size clarity."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '193cadb3-56bf-56a6-8cdf-a6db99d7d95e'
SOURCE_PATH = 'pictographic-primitives/animals/animal print_193cadb3-56bf-56a6-8cdf-a6db99d7d95e.svg'
AUTHOR = 'gpt-6'


class PawPrintSmallOuterToes(Solo48):
    icon_id = 'paw-print-small-outer-toes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('paw', 'print', 'track', 'footprint', 'animal', 'pet', 'dog', 'cat', 'wildlife')

    def build(self) -> None:
        # Paw with four detached toe pads and scalloped main pad; centerline extremes (2,2)-(46,46). Lucide paw-print informs round toe contours; oval toes simplified to circles for native-size clarity.
        self.add_arc('outer-left-top', (2, 22), (8, 22), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('outer-left-bottom', (8, 22), (2, 22), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('outer-left', 'outer-left-top', 'outer-left-bottom', closed=True)
        self.add_arc('inner-left-top', (10, 7), (20, 7), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('inner-left-bottom', (20, 7), (10, 7), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('inner-left', 'inner-left-top', 'inner-left-bottom', closed=True)
        self.add_arc('inner-right-top', (28, 7), (38, 7), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('inner-right-bottom', (38, 7), (28, 7), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('inner-right', 'inner-right-top', 'inner-right-bottom', closed=True)
        self.add_arc('outer-right-top', (40, 22), (46, 22), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('outer-right-bottom', (46, 22), (40, 22), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('outer-right', 'outer-right-top', 'outer-right-bottom', closed=True)
        self.add_arc('pad-crown', (16, 31), (32, 31), radius_x=8, radius_y=7, sweep=True)
        self.add_line('pad-right-slope', (32, 31), (37, 36))
        self.add_arc('pad-right-lobe', (37, 36), (30, 46), radius_x=7, radius_y=10, sweep=True)
        self.add_arc('pad-notch-right', (30, 46), (24, 43), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('pad-notch-left', (24, 43), (18, 46), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('pad-left-lobe', (18, 46), (11, 36), radius_x=7, radius_y=10, sweep=True)
        self.add_line('pad-left-slope', (11, 36), (16, 31))
        self.add_contour('pad', 'pad-crown', 'pad-right-slope', 'pad-right-lobe', 'pad-notch-right', 'pad-notch-left', 'pad-left-lobe', 'pad-left-slope', closed=True)
