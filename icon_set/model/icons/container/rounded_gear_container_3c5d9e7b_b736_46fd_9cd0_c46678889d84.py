"""Rounded Mechanical Gear Wheel: independently authored container.

Construction plan: Eight repeated rounded teeth around a circular enclosure; one continuous outline, no hub absent from source.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/interface-essential/cog 1_3c5d9e7b-b736-46fd-9cd0-c46678889d84.svg. Lucide cog original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart passes, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (rounded-gear-container SQUARE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '3c5d9e7b-b736-46fd-9cd0-c46678889d84'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cog 1_3c5d9e7b-b736-46fd-9cd0-c46678889d84.svg'
AUTHOR = 'claude-opus-5-5'


class RoundedGearContainer(Container64):
    icon_id = 'rounded-gear-container'
    keyshape = Keyshape.CIRCLE
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('rounded', 'gear', 'container')

    def build(self) -> None:
        self.add_arc('gear-0', (28, 10), (36, 10), radius_x=4, radius_y=6)
        self.add_arc('gear-1', (36, 10), (40, 14), radius_x=4, sweep=False)
        self.add_line('gear-2', (40, 14), (46, 14))
        self.add_arc('gear-3', (46, 14), (50, 18), radius_x=4)
        self.add_line('gear-4', (50, 18), (50, 24))
        self.add_arc('gear-5', (50, 24), (54, 28), radius_x=4, sweep=False)
        self.add_arc('gear-6', (54, 28), (54, 36), radius_x=6, radius_y=4)
        self.add_arc('gear-7', (54, 36), (50, 40), radius_x=4, sweep=False)
        self.add_line('gear-8', (50, 40), (50, 46))
        self.add_arc('gear-9', (50, 46), (46, 50), radius_x=4)
        self.add_line('gear-10', (46, 50), (40, 50))
        self.add_arc('gear-11', (40, 50), (36, 54), radius_x=4, sweep=False)
        self.add_arc('gear-12', (36, 54), (28, 54), radius_x=4, radius_y=6)
        self.add_arc('gear-13', (28, 54), (24, 50), radius_x=4, sweep=False)
        self.add_line('gear-14', (24, 50), (18, 50))
        self.add_arc('gear-15', (18, 50), (14, 46), radius_x=4)
        self.add_line('gear-16', (14, 46), (14, 40))
        self.add_arc('gear-17', (14, 40), (10, 36), radius_x=4, sweep=False)
        self.add_arc('gear-18', (10, 36), (10, 28), radius_x=6, radius_y=4)
        self.add_arc('gear-19', (10, 28), (14, 24), radius_x=4, sweep=False)
        self.add_line('gear-20', (14, 24), (14, 18))
        self.add_arc('gear-21', (14, 18), (18, 14), radius_x=4)
        self.add_line('gear-22', (18, 14), (24, 14))
        self.add_arc('gear-23', (24, 14), (28, 10), radius_x=4, sweep=False)
        self.add_contour('gear', 'gear-0', 'gear-1', 'gear-2', 'gear-3', 'gear-4', 'gear-5', 'gear-6', 'gear-7', 'gear-8', 'gear-9', 'gear-10', 'gear-11', 'gear-12', 'gear-13', 'gear-14', 'gear-15', 'gear-16', 'gear-17', 'gear-18', 'gear-19', 'gear-20', 'gear-21', 'gear-22', 'gear-23', closed=True)
