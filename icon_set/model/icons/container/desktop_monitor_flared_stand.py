"""A desktop monitor with a centered, smoothly flared pedestal.

SQUARE fits screen and stand: ink (0,0)-(64,64), centerline (2,2)-(62,62).
Reference: supplied failed SVG; Lucide monitor original and atomic-debug informed
rounded screen corners and a centered stand. Mirrored curves retain the flare;
the pinched rolled foot lip was removed, leaving deliberate corners at the foot.

Hosting (compose.py): plus valid; heart, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (desktop-monitor-flared-stand SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'desktop-monitor-flared-stand'
SOURCE_PATH = 'icon_set/dist/failed/container64/desktop-monitor-flared-stand.svg'
AUTHOR = 'claude-opus-5-5'


class DesktopMonitorFlaredStand(Container64):
    icon_id = 'desktop-monitor-flared-stand'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('desktop', 'monitor', 'flared', 'stand')

    def build(self) -> None:
        self.add_line('screen-0', (12, 6), (52, 6))
        self.add_arc('screen-1', (52, 6), (58, 12), radius_x=6)
        self.add_line('screen-2', (58, 12), (58, 38))
        self.add_arc('screen-3', (58, 38), (52, 44), radius_x=6)
        self.add_line('screen-4-right', (52, 44), (36, 44))
        self.add_line('screen-4-middle', (36, 44), (28, 44))
        self.add_line('screen-4-left', (28, 44), (12, 44))
        self.add_arc('screen-5', (12, 44), (6, 38), radius_x=6)
        self.add_line('screen-6', (6, 38), (6, 12))
        self.add_arc('screen-7', (6, 12), (12, 6), radius_x=6)
        self.add_bezier('stand-left', (28, 44), ((28, 48.8), (25, 52), (20, 58)))
        self.add_line('foot', (20, 58), (44, 58))
        self.add_bezier('stand-right', (44, 58), ((39, 52), (36, 48.8), (36, 44)))
        self.add_contour('screen', 'screen-0', 'screen-1', 'screen-2', 'screen-3', 'screen-4-right', 'screen-4-middle', 'screen-4-left', 'screen-5', 'screen-6', 'screen-7', closed=True)
        self.add_contour('stand', 'stand-left', 'foot', 'stand-right')
        self.relate('connect', 'stand', 'screen')
