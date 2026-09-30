"""An open circular magnifying lens with a detached plus at upper right.

SQUARE: visible extremes (0, 0)-(64, 64), centerlines (2, 2)-(62, 62).
The square envelope accommodates the lens, upper-right mark and diagonal handle.
Source: zoom-in-magnifying-glass-580cac85-8990-40c6-80df-33f62b17f63a.svg.
Retained the open lens, plus and handle; no defining details dropped.
Lucide zoom-in original and atomic-debug informed the circular arcs and crossing
plus strokes. The upper-right opening and lower-right handle retain the source's
intentional asymmetry. All lens arcs share center (27, 27) and radius 25.
Hosting measured with compose.py: plus does not pass MIC, heart does not pass MIC, check does not pass MIC.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (zoom-in-magnifying-glass SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class ZoomInMagnifyingGlass(Container64):
    icon_id = 'zoom-in-magnifying-glass'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('zoom-in-lens',)
    keywords = ('zoom', 'magnify', 'enlarge', 'search', 'lens', 'plus')

    def build(self) -> None:
        self.add_arc('lens-left-a', (31, 6), (6, 31), radius_x=25, sweep=False)
        self.add_arc('lens-left-b', (6, 31), (31, 56), radius_x=25, sweep=False)
        self.add_arc('lens-bottom-right', (31, 56), (46, 51), radius_x=25, sweep=False)
        self.add_arc('lens-right', (46, 51), (56, 31), radius_x=25, sweep=False)
        self.add_line('handle', (46, 51), (58, 58))
        self.add_line('plus-horizontal', (45, 12), (55, 12))
        self.add_line('plus-vertical', (50, 7), (50, 17))
        self.add_contour('lens', 'lens-left-a', 'lens-left-b', 'lens-bottom-right', 'lens-right')
        self.relate('connect', 'lens', 'handle')
        self.relate('connect', 'plus-horizontal', 'plus-vertical')
