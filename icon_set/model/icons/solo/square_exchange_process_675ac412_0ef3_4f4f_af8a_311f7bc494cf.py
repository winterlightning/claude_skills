"""Two rounded squares exchange through an S-shaped double-ended arrow.

SQUARE centerline envelope (6,6)-(42,42). The root owns two identical
9x9 rounded squares (r2) and one S arrow. All paired features have
180-degree symmetry about (24,24); one shared square definition and one
arrowhead definition emit both instances. The continuous shaft owns its
two radius-6 semicircular turns, each tangent to its horizontal runs.
The supplied SVG contributes the diagonal squares and S exchange path.
Lucide replace contributes rounded-square corners and an arrowhead joined
to a coherent turning shaft. No defining features omitted; squares are
reduced to retain 4-unit ink clearance around the exchange path.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "675ac412-0ef3-4f4f-af8a-311f7bc494cf"
SOURCE_PATH = "pictographic-primitives/_uncategorized_01/actions authentication squares arrow_675ac412-0ef3-4f4f-af8a-311f7bc494cf.svg"
AUTHOR = "gpt-6"


class SquareExchangeProcess(Solo48):
    icon_id = "square-exchange-process"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/uncategorized"
    aliases = ("square exchange", "exchange process", "swap squares")
    keywords = ("exchange", "process", "squares", "swap", "transfer", "arrows")

    def build(self):
        rotate = lambda p: (48-p[0], 48-p[1])
        for name, transform in (("first-square", lambda p: p),
                                ("second-square", rotate)):
            lo, hi, radius = 6, 15, 2
            points = ((lo+radius,lo),(hi-radius,lo),(hi,lo+radius),
                      (hi,hi-radius),(hi-radius,hi),(lo+radius,hi),
                      (lo,hi-radius),(lo,lo+radius),(lo+radius,lo))
            members = []
            for index, (start, end) in enumerate(zip(points, points[1:])):
                part = f"{name}-{index}"
                if index % 2:
                    self.add_arc(part, transform(start), transform(end), radius_x=radius)
                else:
                    self.add_line(part, transform(start), transform(end))
                members.append(part)
            self.add_contour(name, *members, closed=True)

        upper_tip = (26,12)
        upper_turn = (36,12)
        middle_right = (36,24)
        middle_left = rotate(middle_right)
        lower_turn = rotate(upper_turn)
        self.add_line("shaft-upper", upper_tip, upper_turn)
        self.add_arc("turn-right", upper_turn, middle_right, radius_x=6)
        self.add_line("shaft-middle", middle_right, middle_left)
        self.add_arc("turn-left", middle_left, lower_turn, radius_x=6, sweep=False)
        self.add_line("shaft-lower", lower_turn, rotate(upper_tip))
        self.add_contour("exchange-shaft", "shaft-upper", "turn-right",
                         "shaft-middle", "turn-left", "shaft-lower")

        for name, transform in (("upper", lambda p: p), ("lower", rotate)):
            self.add_polyline(f"{name}-arrowhead", transform((30,8)),
                              transform(upper_tip), transform((30,16)))
            self.relate("connect", "exchange-shaft", f"{name}-arrowhead")
