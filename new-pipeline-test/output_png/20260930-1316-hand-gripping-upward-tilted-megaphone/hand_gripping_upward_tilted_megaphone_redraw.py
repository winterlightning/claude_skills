"""hand-gripping-upward-tilted-megaphone (redraw of the new-pipeline traced SVG).

Subject: a flared megaphone tilted up to the right, held by a short handle
under its narrow end, with a simplified mitten fist around the handle and a
short forearm running down-left.

Plan (VRECT_L; centerline box (8,4)-(40,44)):
- Keyshape: the metrics suggest SQUARE, but its x axis only fills 86% and the
  stacked cone + 8-long handle + fist + forearm needs more height than the 36
  of SQUARE. VRECT_L (fill x 1.00, y 0.93 in the metrics) gives 40 of height,
  so the fist can be 12 tall instead of a flattened 8. Extremes: bell top
  (32,4), bell apex (40,20), upper forearm tip (8,40), lower forearm tip
  (16,44).
- Megaphone: one closed contour. The bell mouth is an r20 arc about (20,20)
  from (32,4) to (40,20); both ends are Pythagorean points, (40,20) is the
  arc's rightmost point, so the arc lands exactly on the keyshape. The top
  wall rises steeply from the narrow end (16,15); the bottom wall is nearly
  level from (40,20) back to (19,22), like the generated image. The narrow
  end (16,15)-(19,22) is short so the cone flares clearly.
- Handle: a vertical line hanging from the narrow-end corner (19,22) to the
  fist top (19,30), exactly 8 long, so the fist keeps the 8 centerline gap
  from the cone everywhere else.
- Hand: one open contour -- upper forearm (8,40)-(13,35) at 45 degrees, a
  rounded knuckle up to the flat grip top (16,30)-(19,30) that takes the
  handle, a round fist bulge out to x=31, the fist bottom, a wrist crease at
  (20,40), and the lower forearm (20,40)-(16,44), parallel to the upper one
  (x+y = 48 and 60, 8.5 apart on centerlines).

Metric issues:
- fixed: every clearance error (e0/e4, e1/e2, e1/e4, e1/e5, e2/e4, e3/e4,
  e4/e5, e5/e7). The trace's double-line handle, mouthpiece cap and the
  bell's inner ellipse are gone; all distinct parts keep >= 8 on
  centerlines, and the handle joins cone and hand on shared endpoints with
  relate("connect").
- fixed: both small holes (1.6 at the bell rim, 1.52 in the mouthpiece
  cap). The bell is a single outward arc instead of an ellipse beside the
  cone wall, and the mouthpiece cap is dropped (a cap needs a 10-wide
  centerline interior to hold a 6 hole, bigger than the cone's narrow end).
- fixed: loose joins (e0/e2, e0/e3, e2/e5, e3/e5, e5/e7): all joins are exact
  shared integer endpoints.
- fixed: stroke-count (8 strokes, budget 6): now 3 parts -- cone, handle,
  hand.
- fixed: keyshape-short-axis: VRECT_L is filled on all four sides exactly.
- fixed: stroke-width (info): rebuilt at stroke 4 with gaps budgeted for it.
- not applicable: no-head -- the subject is an isolated hand with no person,
  so there is no head or torso (no human figure flag).
Lucide: `megaphone` informed the handle construction (a separate stroke
hanging from the underside of the body); the flared cone and bell follow the
generated PNG instead of Lucide's boxy body.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape

SOURCE_ICON_ID = "dade40b3-c760-4793-8539-0b7a29c7d77c"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1316-hand-gripping-upward-tilted-megaphone/hand-gripping-upward-tilted-megaphone_raw.svg"
AUTHOR = "claude-opus-5-5"

BELL_TOP = (32, 4)
BELL_APEX = (40, 20)       # rightmost point of the r20 arc about (20,20)
BELL_R = 20
NARROW_TOP = (16, 15)
NARROW_BOTTOM = (19, 22)   # handle hangs from this corner
HANDLE_LEN = 8
GRIP = (NARROW_BOTTOM[0], NARROW_BOTTOM[1] + HANDLE_LEN)
UPPER_WRIST = ((8, 40), (13, 35))    # x + y = 48
LOWER_WRIST = ((20, 40), (16, 44))   # x + y = 60


class HandGrippingUpwardTiltedMegaphoneRedraw(Solo48):
    icon_id = "hand-gripping-upward-tilted-megaphone-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "communication"
    aliases = ("megaphone in hand", "bullhorn", "loudhailer")
    keywords = ("megaphone", "bullhorn", "hand", "announce", "announcement",
                "marketing", "promotion", "protest", "shout", "broadcast")

    def build(self) -> None:
        self.add_line("cone-top", NARROW_TOP, BELL_TOP)
        self.add_arc("bell", BELL_TOP, BELL_APEX, radius_x=BELL_R, sweep=True)
        self.add_line("cone-bottom", BELL_APEX, NARROW_BOTTOM)
        self.add_line("cone-narrow", NARROW_BOTTOM, NARROW_TOP)
        self.add_contour("cone", "cone-top", "bell", "cone-bottom", "cone-narrow", closed=True)

        self.add_line("handle", NARROW_BOTTOM, GRIP)

        self.add_line("wrist-top", *UPPER_WRIST)
        self.add_bezier("knuckle", UPPER_WRIST[1], ((14, 34), (14, 30), (16, 30)))
        self.add_line("grip-top", (16, 30), GRIP)
        self.add_bezier(
            "fist", GRIP,
            ((26, 30), (31, 32), (31, 36)),
            ((31, 39.5), (28, 41), (25, 41)),
            ((23, 41), (21.5, 40), LOWER_WRIST[0]),
        )
        self.add_line("wrist-bottom", *LOWER_WRIST)
        self.add_contour("hand", "wrist-top", "knuckle", "grip-top", "fist", "wrist-bottom")

        self.relate("connect", "cone", "handle")
        self.relate("connect", "handle", "hand")


if __name__ == "__main__":
    import subprocess
    import sys
    from pathlib import Path

    here = Path(__file__).resolve().parent
    icon = HandGrippingUpwardTiltedMegaphoneRedraw()
    report = icon.validate_icon()
    print(report.describe())
    svg = here / "hand-gripping-upward-tilted-megaphone_redraw.svg"
    svg.write_text(icon.to_svg())
    for px, name in ((512, "hand-gripping-upward-tilted-megaphone_redraw.png"),
                     (48, "hand-gripping-upward-tilted-megaphone_redraw-48.png")):
        subprocess.run(["rsvg-convert", "-w", str(px), "-h", str(px), "-b", "white",
                        str(svg), "-o", str(here / name)], check=True)
    sys.exit(0 if report.status == "valid" else 1)
