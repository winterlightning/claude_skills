"""An open circular magnifying lens with a circled plus badge at upper right.

SQUARE: visible extremes (0, 0)-(64, 64), centerlines (2, 2)-(62, 62).
The square envelope accommodates the lens, upper-right mark and diagonal handle.
Source: zoom-in-magnifying-glass-8c808b60-d700-43fb-906a-d37f0488edef.svg.
Retained the open lens, plus badge ring and handle; no defining details dropped.
Lucide zoom-in original and atomic-debug informed the circular arcs and crossing
plus strokes. The upper-right opening and lower-right handle retain the source's
intentional asymmetry. All lens arcs share center (27, 27) and radius 25.
Hosting measured with compose.py: plus does not pass MIC, heart does not pass MIC, check does not pass MIC.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (zoom-in-magnifying-glass-with-plus-badge SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-repaired after the fit: lens r20 on 3-4-5 nodes, badge r11, plus arms 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class ZoomInMagnifyingGlassWithPlusBadge(Container64):
    icon_id = 'zoom-in-magnifying-glass-with-plus-badge'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('magnifying-glass-with-plus-badge',)
    keywords = ('zoom', 'magnify', 'enlarge', 'search', 'lens', 'plus')

    def build(self) -> None:
        self.add_arc('lens-left', (26, 6), (26, 46), radius_x=20, sweep=False)
        self.add_arc('lens-bottom-right', (26, 46), (38, 42), radius_x=20, sweep=False)
        self.add_arc('lens-right', (38, 42), (44, 34), radius_x=20, sweep=False)
        self.add_line('handle', (38, 42), (58, 58))
        self.add_arc('badge-top', (36, 17), (58, 17), radius_x=11)
        self.add_arc('badge-bottom', (58, 17), (36, 17), radius_x=11)
        self.add_line('plus-horizontal', (43, 17), (51, 17))
        self.add_line('plus-vertical', (47, 13), (47, 21))
        self.add_contour('lens', 'lens-left', 'lens-bottom-right', 'lens-right')
        self.add_contour('badge', 'badge-top', 'badge-bottom', closed=True)
        self.relate('connect', 'lens', 'handle')
        self.relate('connect', 'plus-horizontal', 'plus-vertical')
