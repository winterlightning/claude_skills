"""gear-with-branching-lines (redraw of the new-pipeline traced SVG).

Subject: a six-tooth settings gear on the left whose shaft runs right into
a branching connector: a spine that forks into three horizontal arms with
rounded top and bottom corners (automation / workflow / process branching).

Plan (HRECT_M, the suggested keyshape; centerline box (4,10)-(44,38)):
- gear: one closed contour about G=(15,24), exactly symmetric about both
  axes through G. Teeth at 90/30/-30/-90/150/210 degrees as in the image:
  flat tips 4 wide at r~12, bases 6 wide at r~9, short r9 root arcs. The
  upper-right quarter is written once and mirrored. The 150/210-degree tips
  reach x=4 (the keyshape's left edge); the 0-degree side is a root at x=24,
  where the shaft leaves the gear (as in the image).
- hub: the image's hub ring cannot fit. A ring needs r>=5 for a 6-wide hole
  and the root would then have to sit at r>=13, making the gear 32 tall and
  leaving no width for the branches. The hub is a centre dot instead,
  8.5+ from every root on centerlines.
- branches: shaft (24,24)-(34,24) into a junction J=(34,24) on a vertical
  spine x=34. The spine turns into the top and bottom arms with r4 quarter
  arcs (centres (38,14) and (38,38-4)), and the arms run to x=44 at y=10
  and y=38 (the keyshape's top, bottom and right edges). The middle arm
  continues from J to (44,24). Arms are 14 apart. The branch is mirrored
  about y=24.
- The spine sits 8 right of the 30-degree tooth tips (26,20)/(26,28), and J
  is 8.9 from them, so only the shaft touches the gear.

Metric issues (gear-with-branching-lines-batch-013_metrics.json):
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- keyshape-short-axis (warn, y fill 66%): the top and bottom arms now sit on
  y=10 and y=38, the arm ends on x=44 and the left teeth on x=4, so all four
  HRECT_M extremes are exact.
- clearance e0/e2, e0/e3 (gear 5.9-6.4 from the branch curves): the spine
  is 8 from the nearest tooth tips and J 8.9; the branch touches the gear
  only through the shaft, which shares the root node (24,24) (connect).
- clearance e0/e4, e1/e4 (the hub ring 3.5-4.5 from the gear and the shaft):
  the ring is replaced by a centre dot 8.5+ from the gear on centerlines.
- loose-join e2/e3: the spine, corner arcs and outer arms are one contour;
  the shaft and middle arm share the exact node J with it (connect).
- hole x6 (1.4-2.6 wide): the tooth notches no longer close into holes;
  the only enclosed area is the gear interior, with the dot 8.5+ from its
  walls (ink gap 4.5 around the dot, 13 across).
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape

SOURCE_ICON_ID = "20a1fb0b-4458-4956-9328-ab0e436276f4"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1315-gear-with-branching-lines-batch-013/gear-with-branching-lines-batch-013_raw.svg"
AUTHOR = "claude-opus-5-5"

G = (15, 24)          # gear centre
ROOT_R = 9            # root arc radius
# Upper-right gear quarter, (dx, dy) from G with y up, walked clockwise from
# the top tooth's left tip corner (-2, 12). Each entry is the segment that
# ends on the point.
UPPER_RIGHT = (
    ((2, 12), "line"),    # top tip
    ((3, 9), "line"),     # top tooth flank
    ((6, 6), "arc"),      # root
    ((9, 8), "line"),     # 30-degree tooth flank
    ((11, 4), "line"),    # 30-degree tip
    ((9, 2), "line"),     # flank
    ((9, -2), "arc"),     # root across 0 degrees (shaft node at its middle)
)
SPINE_X = 34          # junction / spine
ARM_END = 44
TOP_Y, MID_Y, BOT_Y = 10, 24, 38
CORNER_R = 4


def gxy(p):
    return (G[0] + p[0], G[1] - p[1])


class GearWithBranchingLinesRedraw(Solo48):
    icon_id = "gear-with-branching-lines-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ("gear branch", "settings workflow", "process branching")
    keywords = ("gear", "cog", "settings", "branch", "workflow", "automation", "process", "pipeline", "integration")

    def _gear_path(self):
        pts = [p for p, _ in UPPER_RIGHT]
        kinds = [k for _, k in UPPER_RIGHT]
        right = list(UPPER_RIGHT)
        # Lower-right quarter: mirror about y, walked downward.
        for i in range(len(pts) - 3, -1, -1):
            right.append(((pts[i][0], -pts[i][1]), kinds[i + 1]))
        right.append(((-2, -12), kinds[0]))           # bottom tip
        rpts = [p for p, _ in right]
        rkinds = [k for _, k in right]
        path = list(right)
        for i in range(len(rpts) - 3, -1, -1):          # left half, walked upward
            path.append(((-rpts[i][0], rpts[i][1]), rkinds[i + 1]))
        return path

    def build(self) -> None:
        start = (-2, 12)
        prev = start
        members = []
        for n, (p, kind) in enumerate(self._gear_path()):
            if p == (9, -2) and prev == (9, 2):
                # Split the 0-degree root at the shaft node (24,24).
                mid = (ROOT_R, 0)
                self.add_arc(f"gear-{n:02d}a", gxy(prev), gxy(mid), radius_x=ROOT_R, sweep=True)
                self.add_arc(f"gear-{n:02d}b", gxy(mid), gxy(p), radius_x=ROOT_R, sweep=True)
                members += [f"gear-{n:02d}a", f"gear-{n:02d}b"]
            elif kind == "arc":
                self.add_arc(f"gear-{n:02d}", gxy(prev), gxy(p), radius_x=ROOT_R, sweep=True)
                members.append(f"gear-{n:02d}")
            else:
                self.add_line(f"gear-{n:02d}", gxy(prev), gxy(p))
                members.append(f"gear-{n:02d}")
            prev = p
        assert prev == start, prev
        self.add_contour("gear", *members, closed=True)
        self.add_dot("hub", G)

        shaft_start = gxy((ROOT_R, 0))
        j = (SPINE_X, MID_Y)
        self.add_line("shaft", shaft_start, j)
        self.add_line("arm-mid", j, (ARM_END, MID_Y))

        cx = SPINE_X + CORNER_R
        self.add_line("arm-top", (ARM_END, TOP_Y), (cx, TOP_Y))
        self.add_arc("corner-top", (cx, TOP_Y), (SPINE_X, TOP_Y + CORNER_R), radius_x=CORNER_R, sweep=False)
        self.add_line("spine-top", (SPINE_X, TOP_Y + CORNER_R), j)
        self.add_line("spine-bottom", j, (SPINE_X, BOT_Y - CORNER_R))
        self.add_arc("corner-bottom", (SPINE_X, BOT_Y - CORNER_R), (cx, BOT_Y), radius_x=CORNER_R, sweep=False)
        self.add_line("arm-bottom", (cx, BOT_Y), (ARM_END, BOT_Y))
        self.add_contour("branch", "arm-top", "corner-top", "spine-top", "spine-bottom",
                         "corner-bottom", "arm-bottom")

        self.relate("connect", "gear", "shaft")
        self.relate("connect", "shaft", "branch")
        self.relate("connect", "shaft", "arm-mid")
        self.relate("connect", "arm-mid", "branch")


if __name__ == "__main__":
    import subprocess
    import sys
    from pathlib import Path

    here = Path(__file__).resolve().parent
    slug = "gear-with-branching-lines-batch-013"
    icon = GearWithBranchingLinesRedraw()
    report = icon.validate_icon()
    print(report.describe())
    svg = here / f"{slug}_redraw.svg"
    svg.write_text(icon.to_svg())
    for px, name in ((512, f"{slug}_redraw.png"), (48, f"{slug}_redraw-48.png")):
        subprocess.run(["rsvg-convert", "-w", str(px), "-h", str(px), "-b", "white",
                        str(svg), "-o", str(here / name)], check=True)
    sys.exit(0 if report.status == "valid" else 1)
