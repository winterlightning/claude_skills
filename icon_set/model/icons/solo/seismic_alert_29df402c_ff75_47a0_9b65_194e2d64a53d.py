"""A tall tapered exclamation mark with a separate circular dot stands between two opposing curved vibration strokes. The arcs flank the punctuation symmetrically and remain open above and below.

Simplified tapered punctuation to a heavy straight stem; retained paired vibration arcs.
Construction reference: No useful exact local match; mirrored elliptical side arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '29df402c-ff75-47a0-9b65-194e2d64a53d'
SOURCE_PATH = 'pictographic-primitives/weather/earthquake alert_29df402c-ff75-47a0-9b65-194e2d64a53d.svg'
AUTHOR = 'gpt-6'

class SeismicAlert(Solo48):
    icon_id = 'seismic-alert'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    categories = ("weather", "primitives")
    aliases = ()
    keywords = ('seismic', 'alert', 'earthquake', 'warning', 'vibration', 'alarm')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_line('stem', (24, 8), (24, 25))
        self.add_arc('dot-top', (21, 37), (27, 37), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('dot-bottom', (27, 37), (21, 37), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('dot', 'dot-top', 'dot-bottom', closed=True)
        self.add_arc('left', (10, 8), (10, 40), radius_x=6, radius_y=16, sweep=False, large_arc=False)
        self.add_arc('right', (38, 8), (38, 40), radius_x=6, radius_y=16, sweep=True, large_arc=False)
