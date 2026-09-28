"""acro-yoga-folded-balance (redraw of the new-pipeline traced SVG).

Plan: an inverted stick figure in a tripod headstand with folded legs, on
VRECT_M (centerline box (10,4)-(38,44)), the metrics' suggested keyshape.
- head: r4 ring of four cardinal arcs, centre (24,40); bottom extreme y=44.
- torso: vertical on the axis x=24: neck (24,28) exactly 8 centerline units
  (4 ink) above the head outline, shoulder (24,24), hip (24,14). Split at
  the shoulder so the arms share an endpoint.
- arms: mirrored tripod, upper arm out to the elbow (11,32)/(37,32), forearm
  straight down to the floor at y=44; forearms 13 from the head centre.
- legs (deliberately asymmetric so it does not read as a glyph): one folded
  leg hip -> knee (16,4) (top extreme) -> foot (10,12) (left extreme), one
  extended leg hip -> toe (38,6) (right extreme).
References: icon_set/references/human_ref (round head, single-stroke limbs,
detached head with a 4-unit ink gap). No useful Lucide match: Lucide has no
inverted figure. The first draft (a forearm stand with the head beside the
neck, as in the trace) validated but read as "1" at 48 px, so the
clearer tripod headstand replaced it.

Metric issues fixed:
- clearance e0/e1 (6.1): the traced zig-zag legs became one folded leg
  (foot 9.7 from its thigh) and one extended leg meeting at the hip.
- clearance e1/e3 (7.7) and e1/e4 (2.59, torso running into the head): the
  torso is a vertical axis above a detached head at exactly 8; the arms stay
  13.6+ from the head centre.
- hole (3.1 inscribed head): the head is a true r4 ring (exempt small circle).
- loose-join e0/e2 and e1/e2: the stray hip tick (e2) is dropped; every
  join is a shared endpoint declared with relate("connect").
- keyshape-short-axis (y filled 95%): knee y=4 and head/hands y=44, foot
  x=10 and toe x=38 hit all four VRECT_M extremes exactly.
- no-head: the head is a circle, marked with mark_human_figure.
- stroke-width: redrawn at stroke 4 with every gap budgeted at 8.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "672c58c9-cf49-5d74-ba11-e6398667c047"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1636-acro-yoga-folded-balance/"
    "acro-yoga-folded-balance_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AX = 24                        # body axis
HEAD_C, HEAD_R = (AX, 40), 4   # bottom extreme y=44
NECK = (AX, 28)                # HEAD_C.y - HEAD_R - 8
SHOULDER = (AX, 24)
HIP = (AX, 14)
ARM_DX, ELBOW_Y = 13, 32       # elbows at x = 11 / 37, 13 from the head centre
KNEE, FOOT = (16, 4), (10, 12)  # folded leg: top and left extremes
TOE = (38, 6)                  # extended leg: right extreme


class AcroYogaFoldedBalanceRedraw(Solo48):
    icon_id = "acro-yoga-folded-balance-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("acro yoga pose", "headstand", "inverted yoga")
    keywords = ("acro yoga", "yoga", "balance", "inversion", "headstand", "pose")

    def build(self) -> None:
        cx, cy = HEAD_C
        r = HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        # Torso split at the shoulder so the arms share its endpoint.
        self.add_line("torso", NECK, SHOULDER)
        self.add_line("waist", SHOULDER, HIP)
        self.relate("connect", "torso", "waist")
        self.mark_human_figure("acrobat", head="head", torso="torso", torso_junction="start")

        # Tripod arms: upper arm out to the elbow, forearm straight to the floor.
        for side, sign in (("left", -1), ("right", 1)):
            x = AX + sign * ARM_DX
            self.add_polyline(f"arm-{side}", SHOULDER, (x, ELBOW_Y), (x, HEAD_C[1] + HEAD_R))
            self.relate("connect", f"arm-{side}", "torso")
            self.relate("connect", f"arm-{side}", "waist")
        self.relate("connect", "arm-left", "arm-right")

        self.add_polyline("leg-folded", HIP, KNEE, FOOT)
        self.add_line("leg-extended", HIP, TOE)
        self.relate("connect", "leg-folded", "waist")
        self.relate("connect", "leg-extended", "waist")
        self.relate("connect", "leg-folded", "leg-extended")
