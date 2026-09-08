"""An open circular magnifying lens with a detached plus at upper right.

SQUARE: visible extremes (0, 0)-(64, 64), centerlines (2, 2)-(62, 62).
The square envelope accommodates the lens, upper-right mark and diagonal handle.
Source: zoom-in-magnifying-glass-580cac85-8990-40c6-80df-33f62b17f63a.svg.
Retained the open lens, plus and handle; no defining details dropped.
Lucide zoom-in original and atomic-debug informed the circular arcs and crossing
plus strokes. The upper-right opening and lower-right handle retain the source's
intentional asymmetry. All lens arcs share center (27, 27) and radius 25.
Hosting measured with compose.py: plus does not pass MIC, heart does not pass MIC, check does not pass MIC.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class ZoomInMagnifyingGlass(Container64):
    icon_id = "zoom-in-magnifying-glass"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ("zoom-in-lens",)
    keywords = ("zoom", "magnify", "enlarge", "search", "lens", "plus")

    def build(self) -> None:
        self.add_arc("lens-left", (27, 2), (27, 52), radius_x=25, sweep=False)
        self.add_arc("lens-bottom-right", (27, 52), (42, 47), radius_x=25, sweep=False)
        self.add_arc("lens-right", (42, 47), (52, 27), radius_x=25, sweep=False)
        self.add_contour("lens", "lens-left", "lens-bottom-right", "lens-right")
        self.add_line("handle", (42, 47), (62, 62))
        self.relate("connect", "lens", "handle")
        self.add_line("plus-horizontal", (42, 11), (56, 11))
        self.add_line("plus-vertical", (49, 4), (49, 18))
        self.relate("connect", "plus-horizontal", "plus-vertical")
