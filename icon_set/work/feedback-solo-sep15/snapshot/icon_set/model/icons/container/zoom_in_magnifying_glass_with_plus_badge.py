"""An open circular magnifying lens with a circled plus badge at upper right.

SQUARE: visible extremes (0, 0)-(64, 64), centerlines (2, 2)-(62, 62).
The square envelope accommodates the lens, upper-right mark and diagonal handle.
Source: zoom-in-magnifying-glass-8c808b60-d700-43fb-906a-d37f0488edef.svg.
Retained the open lens, plus badge ring and handle; no defining details dropped.
Lucide zoom-in original and atomic-debug informed the circular arcs and crossing
plus strokes. The upper-right opening and lower-right handle retain the source's
intentional asymmetry. All lens arcs share center (27, 27) and radius 25.
Hosting measured with compose.py: plus does not pass MIC, heart does not pass MIC, check does not pass MIC.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class ZoomInMagnifyingGlassWithPlusBadge(Container64):
    icon_id = "zoom-in-magnifying-glass-with-plus-badge"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ("magnifying-glass-with-plus-badge",)
    keywords = ("zoom", "magnify", "enlarge", "search", "lens", "plus")

    def build(self) -> None:
        self.add_arc("lens-left", (27, 2), (27, 52), radius_x=25, sweep=False)
        self.add_arc("lens-bottom-right", (27, 52), (42, 47), radius_x=25, sweep=False)
        self.add_arc("lens-right", (42, 47), (51, 34), radius_x=25, sweep=False)
        self.add_contour("lens", "lens-left", "lens-bottom-right", "lens-right")
        self.add_line("handle", (42, 47), (62, 62))
        self.relate("connect", "lens", "handle")
        self.add_arc("badge-top", (36, 15), (62, 15), radius_x=13)
        self.add_arc("badge-bottom", (62, 15), (36, 15), radius_x=13)
        self.add_contour("badge", "badge-top", "badge-bottom", closed=True)
        self.add_line("plus-horizontal", (43, 15), (55, 15))
        self.add_line("plus-vertical", (49, 9), (49, 21))
        self.relate("connect", "plus-horizontal", "plus-vertical")
