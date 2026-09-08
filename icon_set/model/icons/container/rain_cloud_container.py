"""A cloud enclosure above three diagonal rain strokes. Simplified side lobes retain the cloud enclosure; the extra right shoulder bulge is omitted.

Keyshape HRECT_XL; visible bounds (0, 4, 64, 60); centerline extremes (2, 6)-(62, 58).
Construction reference: Lucide cloud-rain: lobed canopy and detached rain strokes, original and atomic-debug inspected.
Reference identity retained; minor export irregularities simplified.
Hosting measured with compose.py: plus passes, heart passes, check passes.

Batch 10 Hosting measured with compose.py: plus: pass; heart: pass; check: pass.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class RainCloudContainer(Container64):
    icon_id = 'rain-cloud-container'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('cloud-with-falling-rain', 'rainy-weather-cloud')
    keywords = ('rain', 'cloud', 'container')

    def build(self) -> None:
        self.add_arc('left', (14, 22), (14, 42), radius_x=12, radius_y=10, sweep=False, large_arc=False)
        self.add_line('base', (14, 42), (52, 42))
        self.add_arc('right', (52, 42), (62, 32), radius_x=10, radius_y=10, sweep=False, large_arc=False)
        self.add_arc('shoulder', (62, 32), (46, 22), radius_x=16, radius_y=10, sweep=False, large_arc=False)
        self.add_arc('crown', (46, 22), (14, 22), radius_x=16, radius_y=16, sweep=False, large_arc=False)
        self.add_contour('cloud', 'left', 'base', 'right', 'shoulder', 'crown', closed=True)
        self.add_line('rain0', (24, 50), (16, 58))
        self.add_line('rain1', (38, 50), (30, 58))
        self.add_line('rain2', (52, 50), (44, 58))
