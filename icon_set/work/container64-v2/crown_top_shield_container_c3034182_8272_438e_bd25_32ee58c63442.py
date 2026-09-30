"""Protective Security Shield: independently authored container.

Construction plan: Crown-like upper edge joins one broad pointed shield bowl; keep the interior blank as in source.
Keyshape VRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/protection/shield_c3034182-8272-438e-bd25-32ee58c63442.svg. Lucide cross original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (4, 0, 60, 64).
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (crown-top-shield-container VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'c3034182-8272-438e-bd25-32ee58c63442'
SOURCE_PATH = 'pictographic-primitives/protection/shield_c3034182-8272-438e-bd25-32ee58c63442.svg'
AUTHOR = 'claude-opus-5-5'


class CrownTopShieldContainer(Container64):
    icon_id = 'crown-top-shield-container'
    keyshape = Keyshape.VRECT_L
    category = 'protection'
    categories = ('protection', 'primitives')
    aliases = ()
    keywords = ('crown', 'top', 'shield', 'container')

    def build(self) -> None:
        self.add_line('shield-0', (10, 4), (20, 12))
        self.add_line('shield-1', (20, 12), (32, 4))
        self.add_line('shield-2', (32, 4), (44, 12))
        self.add_line('shield-3', (44, 12), (54, 4))
        self.add_line('shield-4', (54, 4), (54, 30))
        self.add_arc('shield-5', (54, 30), (32, 60), radius_x=25, radius_y=32)
        self.add_arc('shield-6', (32, 60), (10, 30), radius_x=25, radius_y=32)
        self.add_line('shield-7', (10, 30), (10, 4))
        self.add_contour('shield', 'shield-0', 'shield-1', 'shield-2', 'shield-3', 'shield-4', 'shield-5', 'shield-6', 'shield-7', closed=True)
