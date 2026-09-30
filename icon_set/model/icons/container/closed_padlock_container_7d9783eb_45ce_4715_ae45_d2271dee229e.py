"""Raise the body top and shorten the shackle while keeping the closed lock.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (closed-padlock-container VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '7d9783eb-45ce-4715-ae45-d2271dee229e'
SOURCE_PATH = 'pictographic-primitives/interface-essential/lock_7d9783eb-45ce-4715-ae45-d2271dee229e.svg'
AUTHOR = 'claude-opus-5-5'


class ClosedPadlockContainer(Container64):
    icon_id = 'closed-padlock-container'
    keyshape = Keyshape.VRECT_L
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('body-0', (15, 20), (49, 20))
        self.add_arc('body-1', (49, 20), (54, 25), radius_x=5)
        self.add_line('body-2', (54, 25), (54, 55))
        self.add_arc('body-3', (54, 55), (49, 60), radius_x=5)
        self.add_line('body-4', (49, 60), (15, 60))
        self.add_arc('body-5', (15, 60), (10, 55), radius_x=5)
        self.add_line('body-6', (10, 55), (10, 25))
        self.add_arc('body-7', (10, 25), (15, 20), radius_x=5)
        self.add_line('shackle-0', (23, 20), (23, 16))
        self.add_arc('shackle-1', (23, 16), (41, 16), radius_x=9, radius_y=12)
        self.add_line('shackle-2', (41, 16), (41, 20))
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_contour('shackle', 'shackle-0', 'shackle-1', 'shackle-2')
        self.relate('connect', 'shackle', 'body')
