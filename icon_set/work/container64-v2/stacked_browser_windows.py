"""Remove the secondary header divider while retaining its indicator and the rear window.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (stacked-browser-windows SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class StackedBrowserWindows(Container64):
    icon_id = 'stacked-browser-windows'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('front-0', (20, 6), (52, 6))
        self.add_arc('front-1', (52, 6), (58, 12), radius_x=6)
        self.add_line('front-2', (58, 12), (58, 42))
        self.add_arc('front-3', (58, 42), (52, 48), radius_x=6)
        self.add_line('front-4', (52, 48), (20, 48))
        self.add_arc('front-5', (20, 48), (14, 42), radius_x=6)
        self.add_line('front-6', (14, 42), (14, 12))
        self.add_arc('front-7', (14, 12), (20, 6), radius_x=6)
        self.add_line('indicator', (24, 14), (28, 14))
        self.add_line('back-0', (14, 18), (12, 18))
        self.add_arc('back-1', (12, 18), (6, 24), radius_x=6, sweep=False)
        self.add_line('back-2', (6, 24), (6, 52))
        self.add_arc('back-3', (6, 52), (12, 58), radius_x=6, sweep=False)
        self.add_line('back-4', (12, 58), (42, 58))
        self.add_arc('back-5', (42, 58), (48, 52), radius_x=6, sweep=False)
        self.add_line('back-6', (48, 52), (48, 48))
        self.add_contour('front', 'front-0', 'front-1', 'front-2', 'front-3', 'front-4', 'front-5', 'front-6', 'front-7', closed=True)
        self.add_contour('back', 'back-0', 'back-1', 'back-2', 'back-3', 'back-4', 'back-5', 'back-6')
        self.relate('connect', 'back', 'front')
