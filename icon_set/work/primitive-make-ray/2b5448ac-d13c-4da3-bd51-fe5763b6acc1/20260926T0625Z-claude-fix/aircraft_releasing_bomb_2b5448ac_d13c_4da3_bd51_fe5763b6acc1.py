"""Aircraft releasing a bomb: a military drone flying left, a falling bomb below it.

Symbol plan: two closed silhouettes that share one nose construction. Each nose is
the same radius-4 semicircle (two quarter arcs) at x=6, so the drone's nose curves
exactly like the bomb's. The drone body runs 8 tall from the nose to the tail at
the right edge; on its top a swept wing rises to the top edge and, 8 further back,
a swept tail fin rises to y=8 before the vertical tail end. The bomb is a capsule
whose rear tapers to a point; two short fins cross behind it, forming the
reference's fish tail.
Deliberate asymmetry: directional flight.
Revision (reviewer: "Make the nose of the airplane curve at the same angle as the
nose of the bomb"): the pointed drone nose is replaced by the bomb's r4 semicircle.
Lucide construction: 'plane' (swept wing and fin on a straight body) and 'bomb'
(rounded capsule); no combined match.
Keyshape SQUARE: centerline x 6 (noses) .. 42 (tail, fins), y 6 (wing) .. 42 (bomb).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2b5448ac-d13c-4da3-bd51-fe5763b6acc1"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__aircraft-releasing-bomb/20260926T061914Z-thuan-mac/reference/military drone attack_2b5448ac-d13c-4da3-bd51-fe5763b6acc1.svg"
AUTHOR = "claude-opus-5-5"

NOSE_R = 4


class AircraftReleasingBomb(Solo48):
    icon_id = "aircraft-releasing-bomb"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "war"
    aliases = ("military-drone-attack", "drone-strike")
    keywords = ("aircraft", "drone", "bomb", "military", "attack", "airstrike", "war")

    def nose(self, name: str, top: int) -> tuple[str, str]:
        """Shared r4 semicircle nose: from the bottom (10, top+8) round to the top (10, top)."""
        cx, cy = 6 + NOSE_R, top + NOSE_R
        self.add_arc(f"{name}-nose-lower", (cx, cy + NOSE_R), (6, cy), radius_x=NOSE_R, sweep=True)
        self.add_arc(f"{name}-nose-upper", (6, cy), (cx, top), radius_x=NOSE_R, sweep=True)
        return f"{name}-nose-lower", f"{name}-nose-upper"

    def segments(self, name: str, *points: tuple[int, int]) -> list[str]:
        """Joined straight segments for a larger contour (no contour of their own)."""
        names = []
        for i, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f"{name}-{i}", a, b)
            names.append(f"{name}-{i}")
        return names

    def build(self) -> None:
        top, bottom = 17, 25
        lower, upper = self.nose("drone", top)
        outline = self.segments("drone-edge", (10, top), (13, top), (19, 6), (28, 6), (24, top),
                                (32, top), (38, 8), (42, 8), (42, bottom), (10, bottom))
        self.add_contour("drone", lower, upper, *outline, closed=True)

        btop, bbot, tip = 34, 42, (28, 38)
        lower, upper = self.nose("bomb", btop)
        shell = self.segments("bomb-shell", (10, btop), (24, btop), tip, (24, bbot), (10, bbot))
        self.add_contour("bomb", lower, upper, *shell, closed=True)
        self.add_line("fin-upper", tip, (32, 34))
        self.add_line("fin-lower", tip, (32, 42))
        self.relate("connect", "bomb", "fin-upper")
        self.relate("connect", "bomb", "fin-lower")
