"""A desktop monitor on two splayed legs and a horizontal foot.

HRECT_XL: centerline extremes (2,5)-(46,43).
Lucide monitor: concentric arcs / matched tangent corners and shared-axis geometry.
Source duplicates are retained in SOURCE_REFERENCES.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c37eca99-9a58-480b-96e2-655800a1c2c8'
SOURCE_PATH = 'pictographic-primitives/computers/batch-03/desktop computer pc_c37eca99-9a58-480b-96e2-655800a1c2c8.svg'
AUTHOR = 'astra-chatgpt'
SOURCE_REFERENCES = (('c37eca99-9a58-480b-96e2-655800a1c2c8', 'pictographic-primitives/computers/batch-03/desktop computer pc_c37eca99-9a58-480b-96e2-655800a1c2c8.svg'), ('2e58e9b5-0627-5117-9f47-d771673be5ab', 'pictographic-primitives/computers/batch-03/desktop computer_2e58e9b5-0627-5117-9f47-d771673be5ab.svg'))


class DesktopMonitorBezelSplayedStand(Solo48):
    icon_id = 'desktop-monitor-bezel-splayed-stand'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('desktop', 'monitor', 'bezel', 'splayed', 'stand')

    def build(self) -> None:
        self.add_line('top', (7, 5), (41, 5))
        self.add_arc('ne', (41, 5), (46, 10), radius_x=5, radius_y=5, sweep=True)
        self.add_line('right-upper', (46, 10), (46, 25))
        self.add_line('right-lower', (46, 25), (46, 29))
        self.add_arc('se', (46, 29), (41, 34), radius_x=5, radius_y=5, sweep=True)
        self.add_line('bottom-right', (41, 34), (29, 34))
        self.add_line('bottom-mid', (29, 34), (19, 34))
        self.add_line('bottom-left', (19, 34), (7, 34))
        self.add_arc('sw', (7, 34), (2, 29), radius_x=5, radius_y=5, sweep=True)
        self.add_line('left-lower', (2, 29), (2, 25))
        self.add_line('left-upper', (2, 25), (2, 10))
        self.add_arc('nw', (2, 10), (7, 5), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('screen', 'top', 'ne', 'right-upper', 'right-lower', 'se', 'bottom-right', 'bottom-mid', 'bottom-left', 'sw', 'left-lower', 'left-upper', 'nw', closed=True)
        self.add_line('bezel', (2, 25), (46, 25))
        self.relate("connect", 'bezel', 'screen')
        self.add_line('leg-left', (19, 34), (17, 43))
        self.add_line('leg-right', (29, 34), (31, 43))
        self.add_line('foot-left', (13, 43), (17, 43))
        self.add_line('foot-mid', (17, 43), (31, 43))
        self.add_line('foot-right', (31, 43), (35, 43))
        self.add_contour('foot', 'foot-left', 'foot-mid', 'foot-right', closed=False)
        self.relate("connect", 'screen', 'leg-left')
        self.relate("connect", 'leg-left', 'foot')
        self.relate("connect", 'screen', 'leg-right')
        self.relate("connect", 'leg-right', 'foot')
