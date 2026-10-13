"""Electric Light Bulb Symbol: independently authored container.

Construction plan: Round globe flows into a narrow base with two bands; mirrored shoulders preserve the bulb.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/work/bulb_6a686616-2bfa-4c53-a2f5-9bfd97179c20.svg. Lucide lightbulb original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (light-bulb-container VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): the shape caps it below 24, now it takes a 20 symbol with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '6a686616-2bfa-4c53-a2f5-9bfd97179c20'
SOURCE_PATH = 'pictographic-primitives/work/bulb_6a686616-2bfa-4c53-a2f5-9bfd97179c20.svg'
AUTHOR = 'claude-opus-5-5'


class LightBulbContainer(Container64):
    icon_id = 'light-bulb-container'
    keyshape = Keyshape.VRECT_L
    category = 'work'
    categories = ('work', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('light', 'bulb', 'container')

    def build(self) -> None:
        # VRECT_L (was VRECT_M): glass r22 about (32,26) (was r20) over an 8-tall screw base with a rounded tip, so the
        # glass holds a symbol of 20 with a 4 px gap (was 18). Mirrored about x = 32.
        self.add_arc('bulb-0', (25, 46), (10, 26), radius_x=23)
        self.add_arc('bulb-1', (10, 26), (32, 4), radius_x=22)
        self.add_arc('bulb-2', (32, 4), (54, 26), radius_x=22)
        self.add_arc('bulb-3', (54, 26), (39, 46), radius_x=23)
        self.add_contour('bulb', 'bulb-0', 'bulb-1', 'bulb-2', 'bulb-3')
        self.add_line('base-1', (25, 46), (25, 54))
        self.add_line('base-3', (39, 54), (39, 46))
        self.add_line('base-4', (39, 46), (25, 46))
        self.add_arc('tip', (25, 54), (39, 54), radius_x=7, radius_y=6, sweep=False)
        self.add_contour('base', 'base-1', 'tip', 'base-3', 'base-4', closed=True)
        self.relate('connect', 'base', 'bulb')
