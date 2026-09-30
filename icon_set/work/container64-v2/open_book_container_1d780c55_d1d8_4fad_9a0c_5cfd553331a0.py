"""Give the right page more width, keeping a narrower visible left page and curved binding.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (open-book-container HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '1d780c55-d1d8-4fad-9a0c-5cfd553331a0'
SOURCE_PATH = 'pictographic-primitives/content/book open 1_1d780c55-d1d8-4fad-9a0c-5cfd553331a0.svg'
AUTHOR = 'claude-opus-5-5'


class OpenBookContainer(Container64):
    icon_id = 'open-book-container'
    keyshape = Keyshape.HRECT_L
    category = 'content'
    categories = ('primitives', 'content')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_arc('outline-0', (4, 10), (21, 16), radius_x=17, radius_y=6)
        self.add_arc('outline-1', (21, 16), (60, 10), radius_x=39, radius_y=6)
        self.add_line('outline-2', (60, 10), (60, 48))
        self.add_arc('outline-3', (60, 48), (21, 54), radius_x=39, radius_y=6, sweep=False)
        self.add_arc('outline-4', (21, 54), (4, 48), radius_x=17, radius_y=6, sweep=False)
        self.add_line('outline-5', (4, 48), (4, 10))
        self.add_line('spine', (21, 16), (21, 54))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', closed=True)
        self.relate('connect', 'spine', 'outline')
