"""Empty clipboard container: a rounded board with a clip on its top edge.

VRECT_XL: centerline (6,2)-(58,62), visible (4,0)-(60,64).
Both blank clipboard references map to this concept. Lucide clipboard
informs the rounded board and centered clip; the shared bottom chord
reduces the overlapping clip detail to a clear connected enclosure.

Batch 01 hosting measured with compose.py: plus, heart, check pass.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class ClipboardContainer(Container64):
    icon_id = "clipboard"
    keyshape = Keyshape.VRECT_XL
    aliases = ("blank-clipboard", "blank-document-clipboard", "blank-office-clipboard", "rounded-office-clipboard")
    keywords = ("board", "clip", "blank", "page")

    def build(self) -> None:
        # An empty clipboard: a rounded board with a stadium clip centred on
        # its top edge. The board's top edge is split at the clip and closed
        # by a chord which doubles as the clip's bottom bar, so board and
        # clip share both endpoints -- one connected component, exactly what
        # keeps the spacing engine from reading the junction as crowding.
        # VRECT_XL-64 is (4,0)-(60,64) visible, (6,2)-(58,62) centerline.
        self.add_line("board-chord", (22, 10), (42, 10))
        self.add_line("board-top-right", (42, 10), (52, 10))
        self.add_arc("board-corner-ne", (52, 10), (58, 16), radius_x=6)
        self.add_line("board-right", (58, 16), (58, 56))
        self.add_arc("board-corner-se", (58, 56), (52, 62), radius_x=6)
        self.add_line("board-bottom", (52, 62), (12, 62))
        self.add_arc("board-corner-sw", (12, 62), (6, 56), radius_x=6)
        self.add_line("board-left", (6, 56), (6, 16))
        self.add_arc("board-corner-nw", (6, 16), (12, 10), radius_x=6)
        self.add_line("board-top-left", (12, 10), (22, 10))
        self.add_contour(
            "board",
            "board-chord", "board-top-right", "board-corner-ne", "board-right",
            "board-corner-se", "board-bottom", "board-corner-sw", "board-left",
            "board-corner-nw", "board-top-left",
            closed=True,
        )
        # Clip arch over the chord. The r=4 corners are quarter circles whose
        # centres sit on the grid, so each meets its vertical and the top bar
        # at a shared axis extreme: no kink anywhere on the arch.
        self.add_line("clip-left", (22, 10), (22, 6))
        self.add_arc("clip-corner-nw", (22, 6), (26, 2), radius_x=4)
        self.add_line("clip-top", (26, 2), (38, 2))
        self.add_arc("clip-corner-ne", (38, 2), (42, 6), radius_x=4)
        self.add_line("clip-right", (42, 6), (42, 10))
        self.add_contour(
            "clip",
            "clip-left", "clip-corner-nw", "clip-top", "clip-corner-ne",
            "clip-right",
        )
        self.relate("connect", "board", "clip")
