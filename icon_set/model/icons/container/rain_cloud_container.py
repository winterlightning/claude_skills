"""A cloud enclosure above three diagonal rain strokes. Simplified side lobes retain the cloud enclosure; the extra right shoulder bulge is omitted.

Keyshape HRECT_XL; visible bounds (0, 4, 64, 60); centerline extremes (2, 6)-(62, 58).
Construction reference: Lucide cloud-rain: lobed canopy and detached rain strokes, original and atomic-debug inspected.
Reference identity retained; minor export irregularities simplified.
Hosting measured with compose.py: plus passes, heart passes, check passes.

Batch 10 Hosting measured with compose.py: plus: pass; heart: pass; check: pass.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (rain-cloud-container HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): the shape caps it below 24, now it takes a 20 symbol with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class RainCloudContainer(Container64):
    icon_id = 'rain-cloud-container'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('cloud-with-falling-rain', 'rainy-weather-cloud')
    keywords = ('rain', 'cloud', 'container')

    def build(self) -> None:
        # SQUARE (was HRECT_L): a full cloud 6..58 x 6..46 with three short drops below (52..58), so the cloud holds
        # a symbol of 20 with a 4 px gap (was 12.5).
        self.add_bezier('cloud-left', (16, 46), ((9, 46), (6, 41), (6, 35)), ((6, 29), (10, 25), (15, 24)))
        self.add_bezier('cloud-crown', (15, 24), ((16, 13), (23, 6), (33, 6)), ((42, 6), (49, 13), (50, 22)))
        self.add_bezier('cloud-right', (50, 22), ((55, 23), (58, 29), (58, 35)), ((58, 41), (54, 46), (48, 46)))
        self.add_line('base', (48, 46), (16, 46))
        self.add_line('rain0', (20, 52), (17, 58))
        self.add_line('rain1', (34, 52), (31, 58))
        self.add_line('rain2', (48, 52), (45, 58))
        self.add_contour('cloud', 'cloud-left', 'cloud-crown', 'cloud-right', 'base', closed=True)
