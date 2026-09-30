"""insect-head-with-antennae (redraw of the new-pipeline traced SVG).

Plan: SQUARE, centerline box (6,6)-(42,42); a front-facing insect head,
mirrored about x=24, keeping the trace's composition: a tapering shield head
narrower than the spread of its antennae.
- head: one closed contour. A shallow crown arc (r25, apex (24,16)) runs
  between the antenna roots J=(17,17) and (31,17). Cubic shoulders leave it
  on the arc's tangent and drop to vertical-tangent cheeks at (8,26)/(40,26),
  then cubic chins taper to a rounded point at (24,42), where both sides
  arrive level, so the bottom is smooth rather than a kink.
- eyes: two filled vertical ovals (zero-width strokes (19,25)-(19,29) and
  (29,25)-(29,29), painting 4 x 8 ovals of ink), 10 apart and more than 8
  from every part of the head outline.
- antennae: one cubic per side from the root J, rising steeply, then bending
  outward to a level tip at (6,6)/(42,6), the icon's top corners. They are
  connected to the head at J (shared endpoint).
Extremes: x 6/42 and y 6 from the antenna tips, y 42 from the chin point.
Metric issues fixed:
- clearance e0/e3 and e0/e4 (eyes 2.0 / 3.1 from the head outline): each eye
  is now more than 8 from the head outline on centerlines.
- clearance e1/e4 and e2/e3 (antenna roots 4.5 / 4.1 from the eyes): the
  roots sit on the crown, more than 8 from the eyes, and the antennae rise
  away from them.
- hole at (31.2,25.8), 1.41 wide (the right eye's sliver): the eyes are solid,
  so there are no slivers; the only hole is the head interior.
- keyshape-short-axis (y filled 87%): the antenna tips reach y=6 and the
  chin reaches y=42, so the drawing fills SQUARE exactly on both axes.
- stroke-width (trace 2.4): authored at stroke 4, with every gap budgeted
  on centerlines.
Not kept as traced:
- hollow eyes: two ring eyes 8 apart and 8 from the head need 36 of head
  width even as the smallest exempt r3 circle. That forces a boxy full-width
  head. At 48 px the r3 rings also paint as solid dots with a 2-unit pinhole,
  which svg_metrics flags as undersized holes. That variant validated but was
  rejected at native size. The eyes are filled ovals instead.
Lucide: no insect-head match (`bug` is a full body with a separate head
cap); construction follows Lucide's mirrored single-contour outlines.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "48b9ec2f-d1e5-4c68-a4c7-5794c4616469"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1515-insect-head-with-antennae/"
    "insect-head-with-antennae_raw.svg"
)
AUTHOR = "claude-opus-5-5"

# Left-half anchors; the right half mirrors about x=24.
ROOT = (17, 17)          # antenna root on the crown
TIP = (6, 6)             # antenna tip, top-left extreme
CHEEK = (8, 26)          # widest point of the head, vertical tangent
CHIN = (24, 42)
CROWN_RADIUS = 25        # chord 14, sagitta 1 -> apex (24,16)
EYE_X, EYE_TOP, EYE_BOTTOM = 19, 25, 29


def mirror(point: tuple[float, float]) -> tuple[float, float]:
    return (48 - point[0], point[1])


class InsectHeadWithAntennaeRedraw(Solo48):
    icon_id = "insect-head-with-antennae-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ("insect head", "ant head", "bug face", "insect face")
    keywords = ("insect", "bug", "ant", "antennae", "head", "eyes", "animal", "nature")

    def build(self) -> None:
        # -- head: crown arc, right side, left side (one closed contour) ----
        # The shoulder control lies on the crown arc's tangent at the root
        # ((24,-7)/25), so the shoulder leaves the crown without a kink.
        shoulder = ((12.2, 18.4), (8, 21))
        chin = ((8, 34), (18, 42))
        self.add_arc("head-crown", ROOT, mirror(ROOT), radius_x=CROWN_RADIUS)
        self.add_bezier(
            "head-right", mirror(ROOT),
            (mirror(shoulder[0]), mirror(shoulder[1]), mirror(CHEEK)),
            (mirror(chin[0]), mirror(chin[1]), CHIN),
        )
        self.add_bezier(
            "head-left", CHIN,
            (chin[1], chin[0], CHEEK),
            (shoulder[1], shoulder[0], ROOT),
        )
        self.add_contour("head", "head-crown", "head-right", "head-left", closed=True)

        # -- antennae ------------------------------------------------------
        antenna = ((15, 10), (11, 6))
        self.add_bezier("antenna-left", ROOT, (*antenna, TIP))
        self.add_bezier(
            "antenna-right", mirror(ROOT),
            (mirror(antenna[0]), mirror(antenna[1]), mirror(TIP)),
        )
        self.relate("connect", "antenna-left", "head")
        self.relate("connect", "antenna-right", "head")

        # -- eyes: filled vertical ovals -----------------------------------
        self.add_line("eye-left", (EYE_X, EYE_TOP), (EYE_X, EYE_BOTTOM))
        self.add_line("eye-right", (48 - EYE_X, EYE_TOP), (48 - EYE_X, EYE_BOTTOM))
