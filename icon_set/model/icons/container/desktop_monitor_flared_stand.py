"""A desktop monitor with a centered, smoothly flared pedestal.

SQUARE fits screen and stand: ink (0,0)-(64,64), centerline (2,2)-(62,62).
Reference: supplied failed SVG; Lucide monitor original and atomic-debug informed
rounded screen corners and a centered stand. Mirrored curves retain the flare;
the pinched rolled foot lip was removed, leaving deliberate corners at the foot.

Hosting (compose.py): plus valid; heart, check blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'desktop-monitor-flared-stand'
SOURCE_PATH = 'icon_set/dist/failed/container64/desktop-monitor-flared-stand.svg'
AUTHOR = 'gpt-6'


class DesktopMonitorFlaredStand(Container64):
    icon_id = 'desktop-monitor-flared-stand'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('desktop', 'monitor', 'flared', 'stand')

    def build(self) -> None:
        self.add_line('screen-0', (8, 2), (56, 2))
        self.add_arc('screen-1', (56, 2), (62, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_line('screen-2', (62, 8), (62, 40))
        self.add_arc('screen-3', (62, 40), (56, 46), radius_x=6, radius_y=6, sweep=True)
        self.add_line('screen-4-right', (56, 46), (38, 46))
        self.add_line('screen-4-middle', (38, 46), (26, 46))
        self.add_line('screen-4-left', (26, 46), (8, 46))
        self.add_arc('screen-5', (8, 46), (2, 40), radius_x=6, radius_y=6, sweep=True)
        self.add_line('screen-6', (2, 40), (2, 8))
        self.add_arc('screen-7', (2, 8), (8, 2), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('screen', 'screen-0', 'screen-1', 'screen-2', 'screen-3', 'screen-4-right', 'screen-4-middle', 'screen-4-left', 'screen-5', 'screen-6', 'screen-7', closed=True)
        # Mirrored flared pedestal: shared neck and foot widths avoid a pinched lip.
        axis, neck_half, foot_half, neck_y, foot_y = 32, 6, 14, 46, 62
        self.add_bezier('stand-left', (axis - neck_half, neck_y),
                        ((axis - neck_half, 52), (axis - 9, 56), (axis - foot_half, foot_y)))
        self.add_line('foot', (axis - foot_half, foot_y), (axis + foot_half, foot_y))
        self.add_bezier('stand-right', (axis + foot_half, foot_y),
                        ((axis + 9, 56), (axis + neck_half, 52), (axis + neck_half, neck_y)))
        self.add_contour('stand', 'stand-left', 'foot', 'stand-right')
        self.relate('connect', 'stand', 'screen')
