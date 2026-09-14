"""Paw with four detached toe pads and scalloped main pad; centerline extremes (6,6)-(42,42). Lucide paw-print informs round toe contours; oval toes simplified to circles for native-size clarity."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a1bcec0-4f4d-5256-8275-cc56ec3fa7d1'
SOURCE_PATH = 'pictographic-primitives/animals/animal print paw_3a1bcec0-4f4d-5256-8275-cc56ec3fa7d1.svg'
AUTHOR = 'gpt-6'


class PawPrint(Solo48):
    icon_id = 'paw-print'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('paw', 'print', 'track', 'footprint', 'animal', 'pet', 'dog', 'cat', 'wildlife')

    def build(self) -> None:
        # Paw with four detached toe pads and scalloped main pad; centerline extremes (6,6)-(42,42). Lucide paw-print informs round toe contours; oval toes simplified to circles for native-size clarity.
        self.add_arc('outer-left-top', (6, 21), (8, 21), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('outer-left-bottom', (8, 21), (6, 21), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('outer-left', 'outer-left-top', 'outer-left-bottom', closed=True)
        self.add_arc('inner-left-top', (13, 6), (19, 6), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('inner-left-bottom', (19, 6), (13, 6), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('inner-left', 'inner-left-top', 'inner-left-bottom', closed=True)
        self.add_arc('inner-right-top', (29, 6), (35, 6), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('inner-right-bottom', (35, 6), (29, 6), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('inner-right', 'inner-right-top', 'inner-right-bottom', closed=True)
        self.add_arc('outer-right-top', (40, 21), (42, 21), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('outer-right-bottom', (42, 21), (40, 21), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('outer-right', 'outer-right-top', 'outer-right-bottom', closed=True)
        self.add_arc('pad-crown', (16, 31), (32, 31), radius_x=8, radius_y=7, sweep=True)
        self.add_line('pad-right-slope', (32, 31), (37, 36))
        self.add_arc('pad-right-lobe', (37, 36), (30, 42), radius_x=7, radius_y=10, sweep=True)
        self.add_arc('pad-notch-right', (30, 42), (24, 42), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('pad-notch-left', (24, 42), (18, 42), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('pad-left-lobe', (18, 42), (11, 36), radius_x=7, radius_y=10, sweep=True)
        self.add_line('pad-left-slope', (11, 36), (16, 31))
        self.add_contour('pad', 'pad-crown', 'pad-right-slope', 'pad-right-lobe', 'pad-notch-right', 'pad-notch-left', 'pad-left-lobe', 'pad-left-slope', closed=True)
