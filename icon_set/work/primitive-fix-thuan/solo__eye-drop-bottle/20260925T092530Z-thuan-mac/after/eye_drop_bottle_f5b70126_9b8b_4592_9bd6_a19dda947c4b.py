"""Eye-drop medicine: a squeeze bottle tipped on the diagonal, body at upper
right, collar and nozzle pointing down-left, with a drop falling below the
nozzle.

Symbol plan: the bottle is built on the 45-degree axis through (37,11)
heading (-1,1); ``at(s, w)`` places a point s along the axis and w across it.
One closed outline holds the body (half-width 5), the tapered shoulder and
the collar (half-width 3); the collar's back edge is a split cross-line; the
nozzle is a stroke from the collar's front centre. The drop is one closed
teardrop (pointed top, round bottom) at lower left, 8+ from the nozzle.
Mirror-symmetric about the bottle axis.
Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: droplet (pointed top, round base); the bottle follows
Lucide's milk/bottle construction (body, shoulder taper, cap band).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f5b70126-9b8b-4592-9bd6-a19dda947c4b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__eye-drop-bottle/20260925T092530Z-thuan-mac/reference/eye drop medicine_f5b70126-9b8b-4592-9bd6-a19dda947c4b.svg"
AUTHOR = "claude-opus-5-5"


def at(s, w):
    return (37 - s + w, 11 + s + w)


class EyeDropBottle(Solo48):
    icon_id = "eye-drop-bottle"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "medical"
    aliases = ("eye drops", "dropper bottle")
    keywords = ("eye", "drop", "medicine", "bottle", "dropper", "health")

    def build(self) -> None:
        body, collar = 5, 3
        self.add_polyline(
            "bottle",
            at(0, body), at(6, body), at(9, collar), at(15, collar), at(15, 0),
            at(15, -collar), at(9, -collar), at(6, -body), at(0, -body),
            closed=True,
        )
        self.add_line("collar-back", at(9, collar), at(9, -collar))
        self.add_line("nozzle", at(15, 0), at(17, 0))
        self.relate("connect", "bottle", "collar-back")
        self.relate("connect", "bottle", "nozzle")
        tip, bottom = (10, 28), (10, 42)
        self.add_bezier("drop", tip,
                        ((12, 32), (14, 35), (14, 38)),
                        ((14, 40.2), (12.2, 42), bottom),
                        ((7.8, 42), (6, 40.2), (6, 38)),
                        ((6, 35), (8, 32), tip))
        self.add_contour("drop-outline", "drop", closed=True)
