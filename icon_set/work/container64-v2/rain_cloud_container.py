"""A cloud enclosure above three diagonal rain strokes. Simplified side lobes retain the cloud enclosure; the extra right shoulder bulge is omitted.

Keyshape HRECT_XL; visible bounds (0, 4, 64, 60); centerline extremes (2, 6)-(62, 58).
Construction reference: Lucide cloud-rain: lobed canopy and detached rain strokes, original and atomic-debug inspected.
Reference identity retained; minor export irregularities simplified.
Hosting measured with compose.py: plus passes, heart passes, check passes.

Batch 10 Hosting measured with compose.py: plus: pass; heart: pass; check: pass.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (rain-cloud-container HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class RainCloudContainer(Container64):
    icon_id = 'rain-cloud-container'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('cloud-with-falling-rain', 'rainy-weather-cloud')
    keywords = ('rain', 'cloud', 'container')

    def build(self) -> None:
        self.add_arc('left-a', (15, 25), (4, 33), radius_x=11, radius_y=9, sweep=False)
        self.add_arc('left-b', (4, 33), (14, 40), radius_x=10, radius_y=8, sweep=False)
        self.add_line('base', (14, 40), (52, 40))
        self.add_arc('right', (52, 40), (60, 32), radius_x=8, sweep=False)
        self.add_arc('shoulder', (60, 32), (45, 25), radius_x=15, radius_y=7, sweep=False)
        self.add_arc('crown', (45, 25), (15, 25), radius_x=15, sweep=False)
        self.add_line('rain0', (24, 47), (16, 54))
        self.add_line('rain1', (38, 47), (30, 54))
        self.add_line('rain2', (52, 47), (44, 54))
        self.add_contour('cloud', 'left-a', 'left-b', 'base', 'right', 'shoulder', 'crown', closed=True)
