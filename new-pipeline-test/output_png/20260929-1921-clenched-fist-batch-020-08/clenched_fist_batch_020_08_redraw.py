"""clenched-fist-batch-020-08 (redraw of the new-pipeline traced SVG).

Plan: an upright raised fist on SQUARE (centerline box (6,6)-(42,42)), the
suggested keyshape (source aspect 0.87, the nearest fit).
- knuckles: four equal r4 semicircles, centres on y=10 at x=14/22/30/38,
  each split at its apex so the finger tops sit on y=6 exactly; three short
  separators drop from the cusps (x=18/26/34) and stop at y=16, 8 above
  the thumb.
- hand: one open contour from the left wrist, up the palm, over a r4
  thumb-base bulge (the x=6 extreme), up the index wall x=10, across the
  knuckles, down the little-finger wall x=42 and back to the right wrist.
  The palm-to-wrist ends are mirrored cubics about x=24 that land vertical on
  the 20-wide wrist (x=14..34, bottom y=42), so the neck of the wrist is
  smooth rather than cornered.
- thumb: folded across the lower fingers; it leaves the thumb-base arc
  tangentially at (10,24), runs to a r4 rounded tip and returns along y=32
  to a free end at x=20, so the thumb is open to the palm (no pocket).
- Deliberate asymmetry: the thumb and its base bulge sit on the left, as in
  the generated image; only the wrist/palm curves are mirrored.
Dropped: the thumb crease curve (e0) and each finger's closed lower end; at
stroke 4 they made 3.5-wide pockets and crowded the thumb.
References: the generated PNG (upright fist, four knuckles, folded thumb,
short wrist). Lucide hand-fist informed the construction (round finger tops,
thumb as one open stroke crossing the fingers); no coordinates taken.

Metric issues (clenched-fist-batch-020-08_metrics.json):
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- stroke-count (10 vs 6): fixed, 5 strokes (hand, thumb, 3 separators).
- keyshape-short-axis (x fill 87%): fixed, x=6 (thumb base), x=42 (little
  finger), y=6 (knuckles) and y=42 (wrist) all sit on the SQUARE box.
- all 17 clearance errors (e0..e9, 1.5 to 7.9 apart): fixed; distinct parts
  are >= 8 apart and the spacing engine certifies them, joined parts share
  exact endpoints with declared connects.
- narrow-join e4/e0 (22 deg wedge): fixed, the crease that made it is gone;
  the thumb meets the hand tangentially.
- loose-join e5/e8, e8/e9 (0.36 / 0.39 short): fixed, knuckles are one
  contour with exact shared nodes.
- 4 holes 3.4-3.6 wide (< 6 inscribed): fixed, the fingers are open to the
  space above the thumb, so the drawing has no enclosed pocket.
Nothing left unrepaired. validate_icon: valid; build_gate: PASS, 0 warnings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f9cc745f-989b-5241-9fd0-090475a8c137"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1921-clenched-fist-batch-020-08/clenched-fist-batch-020-08_raw.svg"
AUTHOR = "claude-opus-5-5"

# knuckles: FINGERS semicircles of radius FR, centres on KY, first at FX0
FX0, FR, KY, FINGERS = 14, 4, 10, 4
SEP_END = 16                # separators stop 8 above the thumb top edge
LEFT, RIGHT = 6, 42         # palm extremes (thumb-base bulge / little finger)
THUMB_Y, THUMB_W = 24, 8    # thumb top edge and width (centerline)
TIP_X = 26                  # centre of the thumb tip arc
THUMB_END = 20              # free end of the thumb's lower edge
PALM_Y = 28                 # where the side walls start curving to the wrist
WRIST_L, WRIST_R, WRIST_Y, BOTTOM = 14, 34, 38, 42


class ClenchedFistBatch02008Redraw(Solo48):
    icon_id = "clenched-fist-batch-020-08-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/gestures"
    aliases = ("raised fist", "closed fist", "hand fist")
    keywords = ("fist", "clenched", "hand", "knuckles", "power", "solidarity", "strength", "protest")

    def build(self) -> None:
        wall_l = FX0 - FR                      # index-finger wall x=10
        cusps = [FX0 + FR + 2 * FR * i for i in range(FINGERS - 1)]

        # Hand outline, left wrist -> knuckles -> right wrist.
        self.add_line("wrist-l", (WRIST_L, BOTTOM), (WRIST_L, WRIST_Y))
        self.add_bezier("palm-l", (WRIST_L, WRIST_Y),
                        ((WRIST_L, WRIST_Y - 3), (LEFT, PALM_Y + 6), (LEFT, PALM_Y)))
        # Thumb base: quarter circle from the x=6 extreme to the thumb edge.
        self.add_arc("thumb-base", (LEFT, PALM_Y), (wall_l, THUMB_Y), radius_x=wall_l - LEFT, sweep=True)
        self.add_line("index-wall", (wall_l, THUMB_Y), (wall_l, KY))
        knuckles = []
        for i in range(FINGERS):
            cx = FX0 + 2 * FR * i
            # split at the apex so each finger top lands on y=6 exactly
            self.add_arc(f"knuckle-{i}a", (cx - FR, KY), (cx, KY - FR), radius_x=FR, sweep=True)
            self.add_arc(f"knuckle-{i}b", (cx, KY - FR), (cx + FR, KY), radius_x=FR, sweep=True)
            knuckles += [f"knuckle-{i}a", f"knuckle-{i}b"]
        self.add_line("little-wall", (RIGHT, KY), (RIGHT, PALM_Y))
        self.add_bezier("palm-r", (RIGHT, PALM_Y),
                        ((RIGHT, PALM_Y + 6), (WRIST_R, WRIST_Y - 3), (WRIST_R, WRIST_Y)))
        self.add_line("wrist-r", (WRIST_R, WRIST_Y), (WRIST_R, BOTTOM))
        self.add_contour("hand", "wrist-l", "palm-l", "thumb-base", "index-wall",
                         *knuckles, "little-wall", "palm-r", "wrist-r")

        # Finger separators hang from the knuckle cusps.
        for i, x in enumerate(cusps):
            self.add_line(f"finger-sep-{i}", (x, KY), (x, SEP_END))
            self.relate("connect", f"finger-sep-{i}", "hand")

        # Thumb folded across the fingers, open at its lower-left end.
        r = THUMB_W // 2
        self.add_line("thumb-top", (wall_l, THUMB_Y), (TIP_X, THUMB_Y))
        self.add_arc("thumb-tip", (TIP_X, THUMB_Y), (TIP_X, THUMB_Y + THUMB_W), radius_x=r, sweep=True)
        self.add_line("thumb-bottom", (TIP_X, THUMB_Y + THUMB_W), (THUMB_END, THUMB_Y + THUMB_W))
        self.add_contour("thumb", "thumb-top", "thumb-tip", "thumb-bottom")
        self.relate("connect", "thumb", "hand")


if __name__ == "__main__":
    import sys
    from pathlib import Path

    here = Path(__file__).resolve().parent
    icon = ClenchedFistBatch02008Redraw()
    print(icon.validate_icon().describe())
    if "--export" in sys.argv:
        stem = "clenched-fist-batch-020-08_redraw"
        icon.export_icon_to(here / f"{stem}.svg")
