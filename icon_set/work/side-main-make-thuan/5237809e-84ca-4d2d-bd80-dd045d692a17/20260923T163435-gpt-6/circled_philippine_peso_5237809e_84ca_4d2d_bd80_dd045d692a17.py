from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5237809e-84ca-4d2d-bd80-dd045d692a17'
SOURCE_PATH = 'pictographic-primitives/other/circle peso_5237809e-84ca-4d2d-bd80-dd045d692a17.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A circular coin enclosing the source single-bar peso P.

    Plan: Circle root; P owns stem x20, bowl y14..24 with elliptical round right end, and the source bar extending left at y24. Stem and bar split at their common node.
    References: Source preserves its distinctive single lower crossbar. Lucide circle-dollar-sign original and atoms inform a circular enclosure with an independent currency mark. Peso glyph follows the supplied drawing.
    """
    icon_id = 'circled-philippine-peso'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/other'
    aliases = ()
    keywords = ()

    def build(self):
        cx, cy, radius = 24, 24, 20
        self.add_arc("coin-top", (cx-radius,cy), (cx+radius,cy), radius_x=radius)
        self.add_arc("coin-bottom", (cx+radius,cy), (cx-radius,cy), radius_x=radius)
        self.add_contour("coin", "coin-top", "coin-bottom", closed=True)
        node = (20,24)
        self.add_line("stem-upper", node, (20,14))
        self.add_line("bowl-top", (20,14), (26,14))
        self.add_arc("bowl-round", (26,14), (26,24), radius_x=6, radius_y=5)
        self.add_line("bowl-bottom", (26,24), node)
        self.add_contour("bowl", "stem-upper", "bowl-top", "bowl-round", "bowl-bottom", closed=True)
        self.add_line("stem-lower", node, (20,34))
        self.add_line("bar-extension", (16,24), node)
        self.relate("connect", "bowl", "stem-lower")
        self.relate("connect", "bowl", "bar-extension")
        self.relate("connect", "stem-lower", "bar-extension")
