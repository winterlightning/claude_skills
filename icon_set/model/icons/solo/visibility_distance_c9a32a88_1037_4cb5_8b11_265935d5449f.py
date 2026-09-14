"""A left-pointing outlined triangle sits beside a horizontal trail of three separated dashes. The numeral 100 appears beneath the trail, aligned under its right-hand portion.

Placed the 100 legend across the lower row and reduced the trail to one dash; retained the numeric meaning.
Construction reference: No useful exact local match; geometric triangle and single-line digits.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c9a32a88-1037-4cb5-8b11-265935d5449f'
SOURCE_PATH = 'pictographic-primitives/weather/visibility_c9a32a88-1037-4cb5-8b11-265935d5449f.svg'
AUTHOR = 'gpt-6'

class VisibilityDistance(Solo48):
    icon_id = 'visibility-distance'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('visibility', 'distance', 'marker', 'measurement', 'sight', 'weather')

    def build(self) -> None:
        """Opening repair: Widened the right zero into a true circle, keeping the 100 legend legible."""
        self.add_polyline('marker', (6, 20), (18, 8), (18, 24), closed=True)
        self.add_line('trail', (28, 14), (42, 14))
        self.add_line('one', (6, 32), (6, 40))
        self.add_arc('zero-left-top', (16, 36), (24, 36), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('zero-left-bottom', (24, 36), (16, 36), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('zero-left', 'zero-left-top', 'zero-left-bottom', closed=True)
        self.add_arc('zero-right-top', (34, 36), (42, 36), sweep=True, large_arc=False, radius_x=4, radius_y=4)
        self.add_arc('zero-right-bottom', (42, 36), (34, 36), sweep=True, large_arc=False, radius_x=4, radius_y=4)
        self.add_contour('zero-right', 'zero-right-top', 'zero-right-bottom', closed=True)
