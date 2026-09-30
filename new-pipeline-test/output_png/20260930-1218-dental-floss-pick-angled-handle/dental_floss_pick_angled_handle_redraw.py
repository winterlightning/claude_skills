"""dental-floss-pick-angled-handle (redraw of the new-pipeline traced SVG).

Plan: a diagonal floss pick on VRECT_L (centerline box (8,4)-(40,44)).
- fork: one open contour tilted on the 1:2 axis d=(1,2). Two parallel prongs
  12 apart across the axis (offset (12,-6)) run down into a semicircular U of
  radius sqrt(45) centred (19,17): two quarter cubics (kappa 0.5523) through
  the apex A=(22,23), tangent-continuous with both prongs and split at A so
  the handle can share it. Prong tips (20,4) and (8,10) are the y=4 and x=8
  extremes.
- floss: a straight line between the prongs at (22,8)-(10,14), 4.5 below the
  prong tips so the prongs read as a fork; each prong is split there and the
  T junction declared.
- handle: one solid stroke from the apex A to (40,44), the x=40 / y=44
  extremes. It leaves at ~49 deg against the fork's 63 deg axis, which is the
  "angled handle" bend.
Clearances: the only hole (floss / prongs / U) is ~13 wide on centerlines,
~9 inscribed in ink; the handle leaves the U at ~76 deg from its tangent.
Keyshape: the suggested VRECT_L; all four extremes land on its box.
Metric issues fixed: stroke-width 2.46 -> 4; keyshape-short-axis (y 94%) ->
the prong tip sits on y=4 and the handle end on y=44; hole 4.92 at the fork
head -> one D-shaped hole >=6 inscribed; holes 0.57 (floss/prong notch) and
0.89 (handle outline tip) -> removed, the floss meets the prongs at declared
T junctions and the handle is a single stroke.
Dropped: the hollow outline of the fork arms and handle (a hollow handle needs
two walls 8 apart plus the fork, which does not fit the head at 48 px).
Lucide reference: no floss-pick match; construction follows Lucide's
single-stroke tools (e.g. `wrench`, `utensils`: round-capped strokes, one
tangent U).
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "21cf1c02-7236-41aa-acb9-d73e1822103e"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1218-dental-floss-pick-angled-handle/dental-floss-pick-angled-handle_raw.svg"
AUTHOR = "claude-opus-5-5"

APEX = (22, 23)                 # U bottom, handle root
P_R, P_L = (25, 14), (13, 20)   # prong bottoms (U ends), centre (19,17)
FLOSS_R, FLOSS_L = (22, 8), (10, 14)
TIP_R, TIP_L = (20, 4), (8, 10)
HANDLE_END = (40, 44)
K = 0.5523 * math.sqrt(45) / math.sqrt(5)   # control run along d=(1,2) / (2,-1)


def _add(p, v, s=1.0):
    return (p[0] + v[0] * s, p[1] + v[1] * s)


class DentalFlossPickAngledHandleRedraw(Solo48):
    icon_id = "dental-floss-pick-angled-handle-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/hygiene"
    aliases = ("floss pick", "flosser", "dental flosser")
    keywords = ("dental", "floss", "pick", "teeth", "tooth", "hygiene", "oral care", "dentist")

    def build(self) -> None:
        d, n = (1, 2), (2, -1)
        self.add_line("prong-r-tip", TIP_R, FLOSS_R)
        self.add_line("prong-r", FLOSS_R, P_R)
        self.add_bezier("u-r", P_R, (_add(P_R, d, K), _add(APEX, n, K), APEX))
        self.add_bezier("u-l", APEX, (_add(APEX, n, -K), _add(P_L, d, K), P_L))
        self.add_line("prong-l", P_L, FLOSS_L)
        self.add_line("prong-l-tip", FLOSS_L, TIP_L)
        self.add_contour("fork", "prong-r-tip", "prong-r", "u-r", "u-l",
                         "prong-l", "prong-l-tip")

        self.add_line("floss", FLOSS_R, FLOSS_L)
        self.relate("connect", "floss", "fork")

        self.add_line("handle", APEX, HANDLE_END)
        self.relate("connect", "handle", "fork")


def main() -> None:
    from pathlib import Path
    import subprocess

    here = Path(__file__).resolve().parent
    icon = DentalFlossPickAngledHandleRedraw()
    print(icon.validate_icon().describe())
    svg = here / "dental-floss-pick-angled-handle_redraw.svg"
    svg.write_text(icon.to_svg())
    for size, name in ((480, "dental-floss-pick-angled-handle_redraw.png"),
                       (48, "dental-floss-pick-angled-handle_redraw-48.png")):
        subprocess.run(["rsvg-convert", "-w", str(size), "-h", str(size),
                        "-b", "white", "-o", str(here / name), str(svg)], check=True)


if __name__ == "__main__":
    main()
