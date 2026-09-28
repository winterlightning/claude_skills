"""Rightward skew of a rectangular shape, with its directional arrow.

SQUARE extremes (6,6)-(42,42). The diagram owns three shared vertices;
its upright and slanted edges retain intentional directional asymmetry.
The separate arrow uses Lucide move-right's shaft/open-chevron construction.
Source contributes the overlapping diagram and arrow above it. No details
are omitted; the extracted near-contact at the lower vertex is made exact.
The saved user classification requests the whole subject as SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "7a15f10b-7bfa-419f-9eca-3085ef1dd050"
SOURCE_PATH = "pictographic-primitives/design/transform right_7a15f10b-7bfa-419f-9eca-3085ef1dd050.svg"
AUTHOR = "gpt-6"


class SkewRightShapeTransformation(Solo48):
    icon_id = "skew-right-shape-transformation"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    categories = ("design", "primitives")
    aliases = ("transform right", "skew right")
    keywords = ("skew", "right", "shape", "transformation")

    def build(self):
        left, middle, right = 6, 24, 42
        top, bottom = 26, 42
        a, b, c = (left, bottom), (middle, top), (middle, bottom)
        self.add_polyline("outer", a, (left, top), b, (right, top), c, closed=True)
        self.add_line("diagonal", a, b)
        self.add_line("upright", b, c)
        self.relate("connect", "outer", "diagonal")
        self.relate("connect", "outer", "upright")
        self.relate("connect", "diagonal", "upright")
        tip = (36, 12)
        self.add_line("shaft", (12, 12), tip)
        self.add_polyline("arrowhead", (30, 6), tip, (30, 18))
        self.relate("connect", "shaft", "arrowhead")
