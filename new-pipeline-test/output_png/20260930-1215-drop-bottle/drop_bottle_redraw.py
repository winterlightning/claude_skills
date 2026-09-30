"""drop-bottle (redraw of the new-pipeline traced SVG).

Plan: an upright dropper bottle on VRECT_M (centerline box (10,4)-(38,44)),
mirrored about x=24.
- bottle: one closed contour. Walls on x=10 / x=38 (the width extremes),
  r4 bottom corners onto the y=44 floor, 45 deg shoulders from (10,22) /
  (38,22) into a 12-wide neck (x=18..30) that rises to a flat cap top at y=10.
  The cap top is split at the axis so the spout shares its endpoint.
- spout: a solid stroke from the cap top (24,10) to the tip (24,4), the y=4
  extreme. At stroke 4 the narrow tapered nozzle reads as a solid spout.
- drop: one closed teardrop, r5 bottom arc centred (24,30) (x=19..29,
  bottom 35) and two mirrored cubics rising to the tip (24,20); vertical
  tangents at the arc ends keep the sides smooth.
Clearances (centerline): drop to walls 9, drop to floor 9, drop tip to cap top
10 and to the neck corners 8.5, drop sides to the shoulders >9.
Keyshape: the suggested VRECT_M; every extreme lands on its box.
Metric issues fixed: stroke-width 2.63 -> 4; keyshape-short-axis (47% x fill)
-> body widened to the full 28-wide box; clearance e0/e1 3.77 (nozzle vs
body) -> the spout joins the cap top at a declared T junction; clearance
e1/e3 2.54 (drop vs body wall) -> 9; the three undersized holes (cap band
3.98, drop 3.98, bottom corner 3.2) -> the cap band is merged into the bottle
silhouette (no separate collar hole) and the drop interior is >=6 wide.
Dropped: the separate collar band (a closed band needs 10 of height the 40-tall
box cannot spare beside the nozzle and drop) and the nozzle's hollow taper.
Lucide reference: `droplet` (round bottom, cubic sides to a point).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "48eb833d-db76-44ba-9351-6d92a11f756c"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1215-drop-bottle/drop-bottle_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                  # mirror axis
LW, RW = 10, 38          # body walls
FLOOR = 44
CORNER = 4               # bottom corner radius
SHOULDER_Y = 22          # wall top; shoulders rise 45 deg to the neck
NL, NR, NECK_Y = 18, 30, 14
CAP_Y = 10
TIP_Y = 4
DROP_CY, DROP_R, DROP_TIP = 30, 5, 20


class DropBottleRedraw(Solo48):
    icon_id = "drop-bottle-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/medical"
    aliases = ("dropper bottle", "eye drops", "drop bottle")
    keywords = ("bottle", "drop", "dropper", "eye drops", "liquid", "medicine", "glue")

    def build(self) -> None:
        self.add_line("floor", (LW + CORNER, FLOOR), (RW - CORNER, FLOOR))
        self.add_arc("corner-r", (RW - CORNER, FLOOR), (RW, FLOOR - CORNER),
                     radius_x=CORNER, sweep=False)
        self.add_line("wall-r", (RW, FLOOR - CORNER), (RW, SHOULDER_Y))
        self.add_line("shoulder-r", (RW, SHOULDER_Y), (NR, NECK_Y))
        self.add_line("neck-r", (NR, NECK_Y), (NR, CAP_Y))
        self.add_line("cap-r", (NR, CAP_Y), (AX, CAP_Y))
        self.add_line("cap-l", (AX, CAP_Y), (NL, CAP_Y))
        self.add_line("neck-l", (NL, CAP_Y), (NL, NECK_Y))
        self.add_line("shoulder-l", (NL, NECK_Y), (LW, SHOULDER_Y))
        self.add_line("wall-l", (LW, SHOULDER_Y), (LW, FLOOR - CORNER))
        self.add_arc("corner-l", (LW, FLOOR - CORNER), (LW + CORNER, FLOOR),
                     radius_x=CORNER, sweep=False)
        self.add_contour(
            "bottle", "floor", "corner-r", "wall-r", "shoulder-r", "neck-r",
            "cap-r", "cap-l", "neck-l", "shoulder-l", "wall-l", "corner-l",
            closed=True,
        )

        self.add_line("spout", (AX, CAP_Y), (AX, TIP_Y))
        self.relate("connect", "spout", "bottle")

        l, r = AX - DROP_R, AX + DROP_R
        self.add_arc("drop-bottom", (l, DROP_CY), (r, DROP_CY), radius_x=DROP_R, sweep=False)
        self.add_bezier("drop-r", (r, DROP_CY),
                        ((r, DROP_CY - 4), (AX + 2, DROP_TIP + 4), (AX, DROP_TIP)))
        self.add_bezier("drop-l", (AX, DROP_TIP),
                        ((AX - 2, DROP_TIP + 4), (l, DROP_CY - 4), (l, DROP_CY)))
        self.add_contour("drop", "drop-bottom", "drop-r", "drop-l", closed=True)


def main() -> None:
    from pathlib import Path
    import subprocess

    here = Path(__file__).resolve().parent
    icon = DropBottleRedraw()
    print(icon.validate_icon().describe())
    svg = here / "drop-bottle_redraw.svg"
    svg.write_text(icon.to_svg())
    for size, name in ((480, "drop-bottle_redraw.png"), (48, "drop-bottle_redraw-48.png")):
        subprocess.run(["rsvg-convert", "-w", str(size), "-h", str(size),
                        "-b", "white", "-o", str(here / name), str(svg)], check=True)


if __name__ == "__main__":
    main()
