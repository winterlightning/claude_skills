"""Electric Light Bulb Symbol: independently authored container.

Construction plan: Round globe flows into a narrow base with two bands; mirrored shoulders preserve the bulb.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/work/bulb_6a686616-2bfa-4c53-a2f5-9bfd97179c20.svg. Lucide lightbulb original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (light-bulb-container VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '6a686616-2bfa-4c53-a2f5-9bfd97179c20'
SOURCE_PATH = 'pictographic-primitives/work/bulb_6a686616-2bfa-4c53-a2f5-9bfd97179c20.svg'
AUTHOR = 'claude-opus-5-5'


class LightBulbContainer(Container64):
    icon_id = 'light-bulb-container'
    keyshape = Keyshape.VRECT_M
    category = 'work'
    categories = ('work', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('light', 'bulb', 'container')

    def build(self) -> None:
        self.add_line('bulb-0', (25, 44), (25, 40))
        self.add_arc('bulb-1', (25, 40), (12, 24), radius_x=20, radius_y=22)
        self.add_arc('bulb-2', (12, 24), (52, 24), radius_x=20)
        self.add_arc('bulb-3', (52, 24), (39, 40), radius_x=20, radius_y=22)
        self.add_line('bulb-4', (39, 40), (39, 44))
        self.add_line('base-1', (25, 44), (25, 52))
        self.add_line('base-2', (25, 52), (39, 52))
        self.add_line('base-3', (39, 52), (39, 44))
        self.add_line('base-4', (39, 44), (25, 44))
        self.add_line('tip-0', (27, 52), (26, 54))
        self.add_arc('tip-1', (26, 54), (38, 54), radius_x=6, sweep=False)
        self.add_line('tip-2', (38, 54), (37, 52))
        self.add_contour('bulb', 'bulb-0', 'bulb-1', 'bulb-2', 'bulb-3', 'bulb-4')
        self.add_contour('base', 'base-1', 'base-2', 'base-3', 'base-4')
        self.add_contour('tip', 'tip-0', 'tip-1', 'tip-2')
        self.relate('connect', 'base', 'bulb')
        self.relate('connect', 'tip', 'base')
