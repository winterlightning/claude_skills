"""Bow with broad loops and long ribbon tails. SQUARE (2,2)-(46,46) accommodates the trailing ends. Symmetric loops; central knot is simplified to a seam."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ebf421f-fe2f-5aa8-a306-a9c327dfebbc'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/accessories ribbon tie_7ebf421f-fe2f-5aa8-a306-a9c327dfebbc.svg'
AUTHOR = 'astra-chatgpt'


class RibbonBowWithTails(Solo48):
    icon_id = 'ribbon-bow-with-tails'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('ribbon', 'bow', 'gift', 'decoration', 'tie', 'accessory', 'present', 'wrapping')

    def build(self) -> None:
        self.add_line("left-top", (24, 12), (8, 2))
        self.add_arc("left-upper", (8, 2), (2, 8), radius_x=6, sweep=False)
        self.add_line("left-side", (2, 8), (2, 20))
        self.add_arc("left-lower", (2, 20), (6, 24), radius_x=4, sweep=False)
        self.add_line("left-return-1", (6, 24), (15, 22))
        self.add_line("left-return-2", (15, 22), (24, 20))
        self.add_line("knot", (24, 20), (24, 12))
        self.add_contour("left-loop", "left-top", "left-upper", "left-side", "left-lower", "left-return-1", "left-return-2", "knot", closed=True)
        self.add_line("right-top", (24, 12), (40, 2))
        self.add_arc("right-upper", (40, 2), (46, 8), radius_x=6)
        self.add_line("right-side", (46, 8), (46, 20))
        self.add_arc("right-lower", (46, 20), (42, 24), radius_x=4)
        self.add_line("right-return-1", (42, 24), (33, 22))
        self.add_line("right-return-2", (33, 22), (24, 20))
        self.add_contour("right-loop", "right-top", "right-upper", "right-side", "right-lower", "right-return-1", "right-return-2")
        self.add_polyline("tail-left", (15, 22), (7, 39), (17, 46), (24, 20))
        self.add_polyline("tail-right", (33, 22), (41, 39), (31, 46), (24, 20))
        self.relate("connect", "left-loop", "right-loop")
        self.relate("connect", "left-loop", "tail-left")
        self.relate("connect", "right-loop", "tail-right")
        self.relate("connect", "left-loop", "tail-right")
        self.relate("connect", "right-loop", "tail-left")
        self.relate("connect", "tail-left", "tail-right")
