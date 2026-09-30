"""Automotive Car Battery Unit: independently authored container.

Construction plan: Rectangular battery housing and two matching terminal tabs; no charge glyph.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/transportation/car battery_51dcd939-bf74-4e07-8d2a-7009bab5f793.svg. Lucide battery-charging original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (car-battery-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '51dcd939-bf74-4e07-8d2a-7009bab5f793'
SOURCE_PATH = 'pictographic-primitives/transportation/car battery_51dcd939-bf74-4e07-8d2a-7009bab5f793.svg'
AUTHOR = 'claude-opus-5-5'


class CarBatteryContainer(Container64):
    icon_id = 'car-battery-container'
    keyshape = Keyshape.SQUARE
    category = 'transportation'
    categories = ('transportation', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('car', 'battery', 'container')

    def build(self) -> None:
        self.add_line('body-0', (10, 14), (54, 14))
        self.add_arc('body-1', (54, 14), (58, 18), radius_x=4)
        self.add_line('body-2', (58, 18), (58, 54))
        self.add_arc('body-3', (58, 54), (54, 58), radius_x=4)
        self.add_line('body-4', (54, 58), (10, 58))
        self.add_arc('body-5', (10, 58), (6, 54), radius_x=4)
        self.add_line('body-6', (6, 54), (6, 18))
        self.add_arc('body-7', (6, 18), (10, 14), radius_x=4)
        self.add_line('terminal-10-1', (14, 14), (14, 6))
        self.add_line('terminal-10-2', (14, 6), (24, 6))
        self.add_line('terminal-10-3', (24, 6), (24, 14))
        self.add_line('terminal-42-1', (40, 14), (40, 6))
        self.add_line('terminal-42-2', (40, 6), (50, 6))
        self.add_line('terminal-42-3', (50, 6), (50, 14))
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_contour('terminal-10', 'terminal-10-1', 'terminal-10-2', 'terminal-10-3')
        self.add_contour('terminal-42', 'terminal-42-1', 'terminal-42-2', 'terminal-42-3')
        self.relate('connect', 'body', 'terminal-10')
        self.relate('connect', 'body', 'terminal-42')
