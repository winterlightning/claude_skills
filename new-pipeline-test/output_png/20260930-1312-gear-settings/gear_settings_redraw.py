"""gear-settings (redraw of the new-pipeline traced SVG).

Subject: a settings gear, one closed outline with six broad tapered teeth
and a hollow round hub in the middle.

Plan (CIRCLE, the suggested keyshape; centerline radius 20 about (24,24)):
- The outline is written for the right half, from the top tooth down to the
  bottom tooth, then mirrored about x=24. The lower right quarter is the upper
  right quarter mirrored about y=24, so the gear is exactly symmetric on both
  axes. Teeth sit at 90, 30, -30, -90, 150 and 210 degrees.
- Top/bottom tooth tips: r13 arcs (19,5)-(29,5), centre (24,17), apex (24,4),
  so the tip lands exactly on the r20 keyshape and cannot overshoot it.
- Side tooth tips: r15 arcs (38,10)-(43,19), apex r19.96, which stays inside
  r20 and has nearly the same sag as the top tips.
- Tooth flanks are straight lines that taper towards the tip: each tooth is
  about 12 across at the r15 base and 10 across at the tip. Roots are short
  r15 arcs on the body circle, bulging outward like the reference; (33,12)
  is a 9-12-15 lattice point.
- Hub: a full circle r6 about (24,24).

Metric issues:
- fixed: clearance e0/e1 7.35 < 8. The body circle now sits at r15 and the
  hub at r6, so the closest pair (root node (33,12), r15) is 9 from the hub
  on centerlines. That satisfies the 9-unit margin needed to certify a
  curved pair.
- fixed: stroke-width (info). The drawing is rebuilt at stroke 4 on the
  48 grid, and the gaps are budgeted for stroke 4 (tooth-to-tooth notch at
  the tips is 10.3 on centerlines, the hub hole is 8 across in ink).
Lucide: `settings` informed the construction (one closed toothed outline
plus a centred hub circle); the teeth follow the generated PNG's flat,
tapered teeth instead of Lucide's rounded lobes.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape

SOURCE_ICON_ID = "95406251-8b85-440b-813a-359dd10112c9"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1312-gear-settings/gear-settings_raw.svg"
AUTHOR = "claude-opus-5-5"

C = 24
HUB_R = 6
# Right half, top tooth to bottom tooth, in (dx, dy) from the centre with
# y pointing up. ("arc", radius) or ("line",) describe the segment that
# ends on the point.
UPPER_RIGHT = (
    ((5, 19), ("arc", 13)),    # top tip (starts at (-5, 19))
    ((6, 14), ("line",)),      # top tooth flank
    ((9, 12), ("arc", 15)),    # root
    ((14, 14), ("line",)),     # 30-degree tooth flank
    ((19, 5), ("arc", 15)),    # 30-degree tooth tip
    ((15, 2), ("line",)),      # flank
    ((15, -2), ("arc", 15)),   # root across 0 degrees
)


def to_xy(p):
    return (C + p[0], C - p[1])


class GearSettingsRedraw(Solo48):
    icon_id = "gear-settings-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ("settings", "cog", "gear")
    keywords = ("settings", "gear", "cog", "preferences", "options", "configuration")

    def build(self) -> None:
        # Right half: upper quarter, then its mirror about y=0 (reversed).
        right = list(UPPER_RIGHT)
        pts = [p for p, _ in UPPER_RIGHT]
        kinds = [k for _, k in UPPER_RIGHT]
        # Mirrored lower quarter: the segment ending on mirror(pts[i-1]) is
        # the mirror of the one ending on pts[i].
        for i in range(len(pts) - 3, -1, -1):
            right.append(((pts[i][0], -pts[i][1]), kinds[i + 1]))
        right.append(((-5, -19), kinds[0]))   # bottom tip
        # Left half: mirror of the right half about x=0, walked upward.
        path = list(right)
        rpts = [p for p, _ in right]
        rkinds = [k for _, k in right]
        for i in range(len(rpts) - 3, -1, -1):
            path.append(((-rpts[i][0], rpts[i][1]), rkinds[i + 1]))

        start = (-5, 19)
        members = []
        prev = start
        for n, (p, kind) in enumerate(path):
            name = f"outline-{n:02d}"
            if kind[0] == "arc":
                self.add_arc(name, to_xy(prev), to_xy(p), radius_x=kind[1], sweep=True)
            else:
                self.add_line(name, to_xy(prev), to_xy(p))
            members.append(name)
            prev = p
        assert prev == start, prev
        self.add_contour("gear", *members, closed=True)

        self.add_arc("hub-top", (C - HUB_R, C), (C + HUB_R, C), radius_x=HUB_R, sweep=True)
        self.add_arc("hub-bottom", (C + HUB_R, C), (C - HUB_R, C), radius_x=HUB_R, sweep=True)
        self.add_contour("hub", "hub-top", "hub-bottom", closed=True)


if __name__ == "__main__":
    import subprocess
    import sys
    from pathlib import Path

    here = Path(__file__).resolve().parent
    icon = GearSettingsRedraw()
    report = icon.validate_icon()
    print(report.describe())
    svg = here / "gear-settings_redraw.svg"
    svg.write_text(icon.to_svg())
    for px, name in ((512, "gear-settings_redraw.png"), (48, "gear-settings_redraw-48.png")):
        subprocess.run(["rsvg-convert", "-w", str(px), "-h", str(px), "-b", "white",
                        str(svg), "-o", str(here / name)], check=True)
    sys.exit(0 if report.status == "valid" else 1)
